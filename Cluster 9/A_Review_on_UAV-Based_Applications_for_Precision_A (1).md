# A_Review_on_UAV-Based_Applications_for_Precision_A (1).pdf

## Page 1

information
Review
A Review on UAV-Based Applications for
Precision Agriculture †
Dimosthenis C. Tsouros *, Stamatia Bibi and Panagiotis G. Sarigiannidis
Department of Electrical and Computer Engineering, University of Western Macedonia, 50100 Kozani, Greece;
sbibi@uowm.gr (S.B.); psarigiannidis@uowm.gr (P.G.S.)
*
Correspondence: dtsouros@uowm.com or dtsouros@uowm.gr
†
This paper is an extended version of our paper published in IoT4 2019 Workshop, co-located with IEEE
DCOSS 2019.
Received: 7 October 2019; Accepted: 7 November 2019; Published: 11 November 2019


Abstract: Emerging technologies such as Internet of Things (IoT) can provide signiﬁcant potential
in Smart Farming and Precision Agriculture applications, enabling the acquisition of real-time
environmental data. IoT devices such as Unmanned Aerial Vehicles (UAVs) can be exploited
in a variety of applications related to crops management, by capturing high spatial and
temporal resolution images. These technologies are expected to revolutionize agriculture, enabling
decision-making in days instead of weeks, promising signiﬁcant reduction in cost and increase in the
yield. Such decisions enable the effective application of farm inputs, supporting the four pillars of
precision agriculture, i.e., apply the right practice, at the right place, at the right time and with the
right quantity. However, the actual proliferation and exploitation of UAVs in Smart Farming has not
been as robust as expected mainly due to the challenges confronted when selecting and deploying
the relevant technologies, including the data acquisition and image processing methods. The main
problem is that still there is no standardized workﬂow for the use of UAVs in such applications, as it
is a relatively new area. In this article, we review the most recent applications of UAVs for Precision
Agriculture. We discuss the most common applications, the types of UAVs exploited and then we
focus on the data acquisition methods and technologies, appointing the beneﬁts and drawbacks of
each one. We also point out the most popular processing methods of aerial imagery and discuss the
outcomes of each method and the potential applications of each one in the farming operations.
Keywords: remote sensing; IoT; UAV; UAS; Unmanned Aerial Vehicle; Unmanned Aerial System;
image processing; Precision Agriculture; Smart Farming; review
1. Introduction
In the last ﬁve years, the total volume of investments in the agricultural sector has increased by
80%. The goal of these investments is to achieve productivity growth of at least 70% by 2050 [1] to meet
the increased needs of the population of the Earth considering the fact that the area under cultivation
will decrease. Emerging technologies such as Internet of Things (IoT) can provide signiﬁcant potential
in Precision Agriculture and Smart Farming, enabling the long-term increase in productivity [2].
The IoT (Internet of Things) paradigm offers a new perspective for precision agriculture enabling the
real- time and site speciﬁc management of the cultivated ﬁelds. In IoT-based Smart farming, a system
is built for monitoring the crops targeting in the automation of various important farming operations
such as monitoring of the growth, irrigation process, application of fertilizers, disease detection, etc.
In this context, technologies such as IoT can assist in the acquisition of real-time information from the
agricultural ﬁelds. This information can be timely processed and exploited to support critical decisions
regarding the management of the crops.
Information 2019, 10, 349; doi:10.3390/info10110349
www.mdpi.com/journal/information

## Page 2

Information 2019, 10, 349
2 of 26
Remote sensing is generally considered one of the most important technologies for Precision
Agriculture and Smart Farming. It is commonly used for monitoring cultivated ﬁelds, providing
effective solutions for Precision Agriculture in the last 35 years [3]. Remote sensing can monitor many
crops and vegetation parameters through images at various wavelengths. In the past, remote sensing
was often based on satellite images [4,5] or images acquired by using manned aircraft in order to
monitor vegetation status at speciﬁc growth stages. However, satellite imagery is often not the best
option because of the low spatial resolution of images acquired and the restrictions of the temporal
resolutions as satellites are not always available to capture the necessary images. In addition, it is often
required to wait long periods between acquisition and reception of images. In addition, environmental
conditions, such as clouds, often hinder their reliable use. Considering the use of manned aircrafts,
usually it results in high costs, and many times it is not possible to carry out multiple ﬂights to obtain
more than a few crop images.
The development of UAV-based remote sensing systems have taken remote sensing and Precision
Agriculture (PA) one step further. The use of UAVs to monitor crops offers great possibilities to acquire
ﬁeld data in an easy, fast and cost-effective way compared to previous methods. UAV-based IoT
technology is considered as the future of remote sensing in Precision Agriculture. UAVs’ ability to ﬂy
at a low altitude results in ultra-high spatial resolution images of the crops (i.e., a few centimeters).
This signiﬁcantly improves the performance of the monitoring systems. Furthermore, UAV-based
monitoring systems have high temporal resolution as they can be used at the user’s will. This enhances
the ﬂexibility of the image acquisition process. In addition, UAVs are a lot simpler to use and also
cheaper than manned aircrafts. Moreover, they are more efﬁcient than the ground systems as they can
cover a large ﬁeld in a short amount of time and in a non-destructive way, which is very important.
UAVs are not a recent technology since the ﬁrst attempt to construct a powered UAV was recorded
in 1916 [6]. UAVs were initially exploited for military purposes; however, in recent years, their use has
rapidly expanded to other types of applications (commercial, scientiﬁc, agricultural, etc.). The wider
use of UAVs was led by the technology advancements and the miniaturization of the associated
hardware during the 1980s and 1990s.
Unmanned Aerial Systems (UAS) are now very commonly used in remote sensing applications
for Precision Agriculture. Equipped with sensors of different types, UAVs can be exploited to identify
which zones of the crops need different management, e.g. some kind of input. This gives the farmers the
ability to react on time in any problem detected. UAS can be used in a plethora of different applications
on Precision Agriculture, such as health monitoring and disease detection, growth monitoring and
yield estimation, weed management and detection, etc. As the use of UAVs in PA applications is very
frequent in the last years and it is considered the future of remote sensing, it is a ﬁeld that draws a
lot of attention. Thus, several reviews exist for their application in Precision Agriculture and Smart
Farming. Most of the reviews focus mainly on the different types of applications that UAVs can have in
agricultural crops [7–12] or environmental monitoring in general [13]. In [14], the authors reviewed the
hyperspectral imagery and the techniques used in these cases. Maes et al. [15] focused on the suitability
of the different available sensors for each application, providing with important perspectives for the
use of UAVs in PA. However, this work does not review the techniques used for exploiting the acquired
information. In addition, a survey that discusses the use of Deep Learning in agricultural data has
been conducted [16].
To the best of the authors knowledge, a review focusing also on the most frequently used
techniques exploiting and processing UAV imagery from agricultural ﬁelds is currently missing from
the literature, despite its necessity. We believe that it is very important mainly because the absence of a
standardized workﬂow is one of the major drawbacks that affects the wider use of UAV systems in
commercial PA applications. This fact results in the adoption of a variety of heterogeneous procedures
and methods by different researchers, for the same goal. This results to not always having the best
outcome. Furthermore, we believe that a study reviewing the most recent works is of paramount
importance, as it is a research area that is advancing really quickly. In this work we extend [17],

## Page 3

Information 2019, 10, 349
3 of 26
reviewing the most recent studies about UAV-based applications for PA, focusing on the most common
techniques applied on UAV imagery in recent works to monitor crop ﬁelds in Precision Agriculture.
The goal is to identify the most used sensors and practices for each type of application.
To properly perform a review on UAV applications in Precision Agriculture, we formulated the
following research questions (RQs):
1.
Which are the different types of UAV applications in Precision Agriculture? In this research
question, we aim to explore the current trends in the application of UAVs in precision agriculture.
The initial goal of UAVs in their early application in agriculture was to derive direct image-based
products.
Nowadays, this has changed, and the applications of UAVs in agriculture are
intelligence-based oriented products that process images and provide informed decision-making
applications to the farmers. In this question, we provide a thorough description of the different
types of applications that UAVs can support based on the different operational needs of
agriculture ﬁelds.
2.
What types of crops are monitored by UAV systems? In this research question, our target is
to record the different types of crops that have been monitored so far with the help of UAVs.
Additionally, we provide general information regarding the geographical distribution of these
crops, their size and the different stages of growth where monitoring can take place. By answering
this research question, we can identify how the different characteristics of each crop and its life
cycle affect the use of UAVs.
3.
Which UAV system technologies are adopted in Precision Agriculture?
In this research
question, we identify the system characteristics of UAV-based applications for Precision
Agriculture. By answering this question we can locate the speciﬁc UAV types and sensors
that can be used for monitoring crops.
4.
What types of data can be acquired by UAVs? In this research question, we record the different
types of data that can be acquired by UAVs based on the sensor technology employed. We also
provide a review of the advantages and disadvantages of the different types of data that can be
gathered with the help of different sensors based on the associated cost and the types of the ﬁeld
operations applied.
5.
Which data processing methods can be used to exploit the agricultural data acquired by UAVs?
In this research question, we identify the methods that are used for image analysis in agricultural
crops. We distinguish between three types of data processing methods that can be used alone or
complementary so as to gain insights regarding a ﬁeld namely: (a) Photogrammetric techniques;
(b) Machine Learning techniques; and (c) Vegetation Indices.
To answer these research questions, we reviewed 100 recent papers [18–117] published during the
2017–2019 period.
The rest of the article is organized as follows. Section 2 describes the basic UAV-based applications
for Precision Agriculture, including the types of crops being monitored, the application domains and
the UAV technologies being used for Precision Agriculture purposes. In Section 3, we focus on the
basics of UAV-based data acquisition and the types of sensors used. Section 4 discusses the most
used image processing methods that stood out in the literature: the photogrammetry techniques, the
vegetation indices calculation and machine learning. Next, Section 5 focuses on the limitations in the
use of UAVs for Precision Agriculture. Finally, Section 6 discusses the results of the review and make
some concluding remarks.
2. UAV-Based Monitoring of Crops
In this section, we introduce the applications of UAVs for Precision Agriculture, along with the
types of crops being monitored and the UAV technologies adopted.

## Page 4

Information 2019, 10, 349
4 of 26
2.1. Types of UAV Applications in Precision Agriculture
To date, UAV technologies have been successfully employed in a variety of applications for
Precision Agriculture such as site-speciﬁc herbicide applications, water deﬁciency identiﬁcation,
detection of diseases, etc. Using the information acquired by the UAVs several decisions can be made
to handle the problem(s) detected and/or optimize harvesting by estimating the yield.
The most common applications of UAVs for Precision Agriculture, as recorded in the literature,
are the following:
•
Weed mapping and management [70,98]
•
Vegetation growth monitoring and yield estimation [48,65,87]
•
Vegetation health monitoring and diseases detection [46,77]
•
Irrigation management [64,118]
•
Corps spraying [89,95]
Among the most popular application of UAVs in Precision Agriculture is Weed mapping.
Weeds are not desirable plants, which grow in agricultural crops and can cause several problems.
They are competing for available resources such as water or even space, causing losses to crop yields
and in their growth. In addition to the problems in the growth of the crops, weeds can cause problems
at harvesting. The use of herbicides is the dominant choice for weed control. In conventional farming,
the most common practice of weed management is to spray the same amounts of herbicides over the
entire ﬁeld, even within the weed-free areas. However, the overuse of herbicides can result in the
evolution of herbicide-resistant weeds and it can affect the growth and yield of the crops. In addition,
it poses a heavy pollution threat to the environment. In addition, the above practice signiﬁcantly
increases the cost. To overcome the above problems, in Precision Agriculture practices, Site-Speciﬁc
Weed Management (SSWM) is used. SSWM refers to the spatially variable application of herbicides
rather than spraying them in the whole ﬁeld. In this context, the ﬁeld is divided into management
zones that each one receives a customized management, as usually weed plants spread through only
few spots of the ﬁeld. To achieve this goal, it is necessary to generate an accurate weed cover map for
precise spraying of herbicide. UAVs can gather images and derive data from the whole ﬁeld that can
be used to generate a precise weed cover map depicting the spots where the chemicals are needed:
(a) the most; (b) the least; or (c) they should not be applied at all.
UAVs are also frequently used for Monitoring the growth of the vegetation and providing
estimation regarding the yield. The lack of means for systematically monitoring the progress of
cultivation is considered as one of the major obstacles to increasing the agricultural productivity
and quality. This problem is also compounded by the variability of weather conditions that alter the
micro-climate of crops jeopardizing the agricultural production. Regular collection of information
and visualization of crops using UAVs, provides increased opportunities to monitor crop growth
and record the variability observed in several parameters of the ﬁeld. Many recent works focus on
monitoring the biomass and nitrogen status of the crops along with yield estimation. Biomass is the
most common crop parameter, which together with information related to nitrogen content can be
used to determine the need for additional fertilizer or other actions. In addition, the information
acquired by the UAVs can be used for the creation of three-dimensional digital maps of the crop, and
for the measurement of various parameters, such as crop height, distance between rows or between
plants, and the index Leaf Area Index (LAI). UAVs offer the potential to systematically collect crop
information, therefore farmers can plan in a controlled manner the crop management, use of inputs
(e.g., use of nutrients), timing of harvesting and soil and yield pathogens, or even identify possible
management errors.
UAVs are also used to monitor vegetation health. Crop health is a very important factor that
needs to be monitored, as diseases in crops can cause signiﬁcant economic loss due to the reduced yield
and the reduction of quality. Crops should be monitored constantly to detect the diseases in time and
avoid spreading problems. Traditionally, this task is performed by human experts directly in the ﬁeld.

## Page 5

Information 2019, 10, 349
5 of 26
However, this can be very time consuming, as it can require months to inspect an entire crop preventing
the potentials of “continuous” monitoring. Another common disease control method is the application
of pesticides in certain dates. Such a strategy incurs a high cost and also increases the likelihood of
ground water contamination as pesticide residues in the products. In Precision Agriculture, site-speciﬁc
disease control takes place. PA practices adopt a decision-based disease management strategy, in which
automated non-destructive crops disease detection plays a very important role. Disease detection
is feasible as diseases induce changes in biophysical and biochemical characteristics of the crops.
UAV-based data processing technologies use crop imaging information to identify changes in plant
biomass and their health. Therefore, diseases can be detected in their early stages enabling farmers
to intervene in order to reduce losses. In this context, UAVs can be used in the two different stages
of disease control: (a) at the initial stage of infection by collecting crop health relevant information,
during which UAVs can detect a possible infection before visual indications appear and map the size of
the infection to different parts of a culture; and (b) during the treatment of infection when farmers can
use UAVs for targeted spraying as well as for accurately monitoring the course of their intervention.
Crop irrigation management is a very important area of application of UAV technologies in
Precision Agriculture. Currently, 70% of the water consumed worldwide is used for the irrigation of
crops [119,120], a fact that highlights the need for precision irrigation techniques. Precision irrigation
techniques can improve the efﬁciency of water use, so that the resource is applied effectively: (a) in
the right places; (b) at the right time; and (c) in the right quantity. The detection of the areas where
major irrigation is needed can help the farmers to save time and water resources. At the same time,
such precision farming techniques can lead to increased crop productivity and quality. In the context
of precision agriculture, the ﬁeld is divided in different irrigation zones, to precisely manage the
resources. The use of Unmanned Aerial Vehicles incorporating suitable sensor types makes it possible
to identify parts of a crop that need more water. At the same time, the above technologies allow for the
production of specialized maps that illustrate the morphology of the soil, thus supporting the more
efﬁcient irrigation planning of each crop separately.
An application of UAVs in precision agriculture that is more rarely met is Crop spraying. The main
spraying equipment used in conventional farming are the manual air-pressure and battery-powered
knapsack sprayers. However, these conventional sprayers can cause major pesticide losses. In addition,
the operators need to be present when spraying, which leads to exposure of the operators. In addition,
it may be time-consuming to spray the entire ﬁeld, which is not only limiting the resources but also can
lead to not-timely spraying. In this manner, UAVs can be useful due to the lower operator exposure
and improved ability to apply chemicals in a timely and highly spatially resolved manner. The use
of precision systems for measuring distances allows UAVs to follow the morphology of the ground,
keeping their height constant. Therefore, an aircraft has the ability to spray the appropriate amount
of herbicide spatially, adjusting both its height and the amount it sprays depending on the crop site
in which it is located. Crop spraying is particularly important in cases where diseases have been
identiﬁed where it is important to reduce pesticide use without affecting crop yield. In conclusion,
UAV-based systems can make a decisive contribution to crop spray management.
In addition to the common applications mentioned above, UAVs have also been used for soil
analysis [108,112], cotton genotype selection [48], mammal detection [24], and assessment of soil
electrical conductivity [66].
2.2. Types and Properties of Crops Monitored by UAV-Based Systems
In the recent years, UAV technologies have been employed to monitor a variety of different types
of crops, located in several countries all over the world. UAV applications in Precision Agriculture
have been carried out in 29 different countries. The majority of applications are located in economically
developed countries, with the US and China standing out. Lately, however, the applications in Europe
have increased as well.

## Page 6

Information 2019, 10, 349
6 of 26
Regarding the different types of crop species that can be monitored with the help of UAVs, more
than 30 different species were identiﬁed. Among the most common crop species monitored by UAV
technologies are Maize, Wheat, Cotton, Vineyards, Rice and Soya. In addition, we observe that these
technologies have been used to monitor crops with completely different characteristics, such as olive
trees and rice crops.
Another observation is that the monitoring of crops can take place during the different stages
of growth, even at the early ones before being able to draw inferences from soil characteristics.
The purpose of constant and continuous monitoring of crops at different stages of development
is to record various factors that may affect the ﬁnal performance of crops, as well as to evaluate
the effectiveness of actions taken to address problems identiﬁed at an earlier stage of development.
Regarding the size of the crops monitored we observe in this review that it is possible:
•
To monitor large ﬁelds (>10 ha), where data are collected from all areas.
•
To monitor small farms or small parts of a ﬁeld.
•
To monitor areas of great heterogeneity. This is achieved by using a UAV equipped with automatic
pilot systems and ground-level sensors.
2.3. UAV System Technologies
An Unmanned Aerial System that applies to Precision Agriculture usually includes the following
key elements [121]:
•
One or more UAVs: Flying vehicles that have no operator on their spindle but operate either
autonomously or remotely.
•
A Ground Control Station (GCS): It is a computer that either communicates with the UAV Control
System or controls and monitors the UAV directly. The GCS monitors information related to the
ﬂight of the UAV. The user has the ability to receive data relevant to the ﬂight of the aircraft, but
also data recorded by the sensors that support the ﬂight (i.e., ground-based sensors or sensors
embedded in the aircraft). In addition, the GCS contains the software required for the processing
of data acquired by the UAV and the extraction of the information needed by the system operator
for the crop monitoring.
•
UAV Control System (UAV CS): It is used to control the UAV. It can be either a two-way data
link, such as a remote control, or a built-in computer (usually with a built in GPS). The UAV CS
includes the ﬂight control system and/or the autopilot system, which controls the operation of
the UAV. This system receives and processes data from the autopilot or ﬂight control system for
the proper operation of the UAV. It usually contains sensors to monitor the ﬂight properties, such
as sensors for measuring distance from ground, air force, etc. The control system has the ability to
process information from sensors to correct any problems that may arise, and to communicate
with the GCC wireless and in real time by sending and receiving the necessary information.
•
Sensors for data acquisition: They are cameras intended to collect the information needed. The
next section provides a detailed presentation of possible ways of collecting information and the
technologies exploited. In the case that UAVs are not intended to collect information but are used
for another purpose, such as spraying, the sensors are replaced with the necessary components.
Focusing on the UAV technologies being used for PA, the types of Unmanned Aerial Vehicles can
be divided into ﬁve basic categories, based on their design characteristics (see Figure 1).

## Page 7

Information 2019, 10, 349
7 of 26
(a)
(b)
(c)
(d)
(e)
(f)
Figure 1.
(a) Fixed-wing (eBeeTM) [23]; (b) helicopter (Hornet Maxi) [122]; (c) octocopter [25];
(d) blimp [123]; (e) ﬂapping-wing (SmartBird) [122]; and (f) parafoil-wing (Tetracam) [90].
1.
Fixed-wing: These are unmanned planes with wings that require a runway to take off from
the ground or a catapult. This type of UAVs has high endurance as well as the ability to
ﬂy at high speeds. In addition, ﬁxed-wing UAVs have the ability to cover large areas on
each ﬂight and can carry more payload. However, they are more expensive than the other
types. In the works reviewed, 22% used ﬁxed-wing UAVs. One type of ﬁxed-wing UAVs that
has not been identiﬁed in the reviewed literature, but is a very promising technology, is the
solar-powered UAVs [124]. Solar-powered UAVs offer signiﬁcantly increased ﬂight times because
they exploit and store the sun’s energy during the day. This is the reason that they are preferred
for long-endurance operations.
2.
Rotary-wing: The rotary-wing UAVS, also called rotorcrafts or Vertical Take-Off and Landing
(VTOL), offer the advantages of steady ﬂying at one place while keeping the maneuverability
attribute. These features are useful for many different types of missions. However, they cannot
ﬂy at very high speed or stay in the air for a long time. They are generally the most widely used
UAVs in all kinds of applications, but especially in Precision Agriculture. One reason for this
is the fact that they present lower cost compared to the other types of UAVs. In addition, this
type of UAVs is suitable when the monitored crops are not very large, which is usually the case.
A UAV of this type may be:
•
An unmanned helicopter: They include main and tail rotors such as conventional helicopters.
Overall, 4% of the works used this type.
•
Multi-rotor: This category includes rotary-wing UAVs with four or more rotors (quadcopter,
hexacopter, octocopter, etc.). These aircraft are generally more stable in ﬂight than unmanned
helicopters. Overall, 72% of the works used this type.
3.
Blimps: This type of UAV is lighter than air, has high endurance, ﬂies at low speeds and is
generally larger in size compared to the other types. Their manufacturing characteristics allows
them to remain in the air even in the event of a total loss of power, while being considered
relatively safe in the event of a collision. Usually, they are not used in Precision Agriculture
applications. In the recent works reviewed, no application was found using this type of UAVs.

## Page 8

Information 2019, 10, 349
8 of 26
4.
Flapping wing: These UAVs are very small and they have ﬂexible, shaped little wings inspired by
the way birds and insects ﬂy. They are not often used in Precision Agriculture as they require
high energy consumption due to their size. No work was found in the literature review using
this type of UAVs.
5.
Parafoil-wing. Usually aircrafts of this type have one or more propellers at the back in order to
control the course of their ﬂight, but at the same time for harnessing the power of the air to ﬂy
without consuming much energy. They are also capable of carrying a larger payload. They are
not usually exploited for PA applications. Only 2% of the works analyzed use this type.
In addition to the above classiﬁcation, UAVs can also be categorized according to their size [121].
However, the categorization used in this study is more common, as it takes into account more factors
affecting the performance of UAVs and their use in Precision Agriculture.
The majority of the recent works in Precision Agriculture use multi-rotor UAVs. This is mainly
due to the fact that in most applications the area under consideration is not very large. For this reason,
it is not necessary to use UAVs with high speed and the ability to cover large areas in a few ﬂights, such
as ﬁxed-wing UAVs. Thus, rotary-wing aircraft are preferred because of the following advantages:
•
Easy to operate
•
Slower speeds
•
Ability to maneuver
•
Relatively low cost
These advantages provide greater opportunities for collecting information from crops through
imaging, which is the main use of UAVs in vegetation monitoring. In cases where the monitoring area
is relatively large, ﬁxed-wing aircraft are preferred, which enable the monitoring of the entire area in a
short time.
3. UAV Data Acquisition
Equipped with specialized sensors, UAVs are becoming powerful sensing systems that
complement the IoT-based techniques. The role of the sensors is to capture images of high-spatial and
temporal resolution, which can assist in monitoring many different characteristics of the vegetation.
A variety of different types of sensors can be used in an agricultural UAV depending on the different
crop parameters that should be monitored [9]. However, the needs for low payload capacity and the
utilization of small platforms pose several limitations on the selection s of the sensor(s) to be used.
The main criteria that the sensors have to meet are the low weight, the low energy consumption
and the small size. Of course, all of the above must be combined with the ability to capture high
resolution images.
Modern commercial on-board sensors complying with the above restrictions that are used for PA ,
mainly belong to the following four types:
•
Visible light sensors (RGB)
•
Multispectral sensors
•
Hyperspectral sensors
•
Thermal sensors
In addition to the above types of sensors, other types of sensors can be used, such as laser
scanners, also mentioned in the literature as light detection and ranging (LiDAR). Laser scanners
are a well-established technology used extensively for environmental sciences, however they are
mostly used for terrestrial scanning. Airborne laser scanning has been exploited since 1994 [125], when
commercial systems became available. However, they were not widely used in the studies reviewed,
mainly due to the increased cost compared to other types of sensors used for data acquisition [84].
Each sensor type can monitor different characteristics of the vegetation, such as the color and
texture of vegetation or the geometric outline of the crops. In addition, some sensors can measure

## Page 9

Information 2019, 10, 349
9 of 26
the radiation in certain wavelengths. The data acquired by these sensors can be further processed to
monitor plant biomass, vegetation health, soil moisture and other important crop characteristics at the
different growth stages. Figure 2 presents examples of the main types of sensors used.
(a)
(b)
(c)
(d)
Figure 2. Examples of sensors used by UAVs for PA: (a) thermal sensor [103]; (b) RGB sensor [59];
(c) multispectral sensor [26]; and (d) hyperspectral sensor [88].
•
Visible light sensors (RGB): RGB sensors are the most frequently used sensors by UAV systems
for Precision Agriculture applications. They are relatively low cost compared to the other types
and can acquire high resolution images. In addition, they are easy to use and operate and they
are lightweight. In addition, the information acquired requires simple processing. The images
can be acquired in different conditions, on both sunny and cloudy days, but a speciﬁc time frame
is required based on weather conditions to avoid inadequate or excessive exposure of the image.
Considering the drawbacks of these sensors, the main disadvantage is the fact that they are
inadequate for analyzing a lot of vegetation parameters that require spectral information in the
non-visible spectrum. They are commonly used in tandem with the other types of sensors.
•
By using multispectral or hyperspectral imaging sensors, UAVs can acquire information about
the vegetation’s spectral absorption and reﬂection on several bands. Spectral information can
be signiﬁcantly helpful in assessing a lot of biological and physical characteristics of the crops.
For example, unhealthy parts of the crops can be discriminated in an image, as visible radiation
in the red channel is absorbed by chlorophyll, while near infrared (NIR) radiation is strongly
reﬂected. Thus, even if it is not yet visible in the red channel, it can be identiﬁed by the information
in the NIR channel. Spectral information can be used to calculate several vegetation indices and
monitor several crop characteristics based on them.
Multispectral and hyperspectral sensors are frequently used, despite their higher costs. However, a
drawback of these sensors arises from the fact that it is required to apply more complex
pre-processing methods in order to extract useful information from the captured images.
The pre-processing procedure of spectral images often contains the radiometric calibration,

## Page 10

Information 2019, 10, 349
10 of 26
geometric correction, image fusion and image enhancement. The main difference between
multispectral and hyperspectral sensors is the number of bands (or channels) that each sensor
can capture and the width of the bands. Multispectral sensors capture 5–12 channels while
hyperspectral images can usually capture hundreds or thousands bands, but in a narrower
bandwidth. Although in the recent works studied multispectral sensors are used a lot more
frequently than hyperspectral because of their lower cost, hyperspectral technology seems to have
a lot of potential and is considered as the future trend for crop phenotyping research [9].
•
Thermal infrared sensors capture information about the temperature of the objects and generate
images displaying them based on this information and not their visible properties. Thermal
cameras use infrared sensors and an optical lens to receive infrared energy. All objects warmer
than absolute zero (−273 ◦C/−459 ◦F) emit infrared radiation at speciﬁc wavelengths (LWIR and
MWIR bands) in an amount proportional to their temperature. Hence, thermal cameras focus
and detect the radiation in these wavelengths and usually translate it into a grayscale image for
the heat representation. Many thermal imaging sensors can also generate colored images. These
images often show warmer objects as yellow and cooler objects as blue. This type of sensors
is used for very speciﬁc applications (e.g., irrigation management). As a result, they are not
frequently used in PA applications of UAV systems that focus on monitoring other characteristics
of the crops.
In the image acquisition by UAVs, it is typical to acquire several overlapping images of the
crops. In the most cases they capture both front and side overlapping images. This is desired as the
overlapping images can be used for the construction of 3D models and/or orthophotos of the crops, as
the next section discusses. The rate of the overlap depends on the type of the application. The front
overlap usually ranges 60–95% while the side overlap ranges 40–95% to generate three-dimensional
models and 25–40% for other uses.
In addition, the altitude of the UAV ﬂights varies according to the application and spatial accuracy
of the information we want to collect. The distance between the target (crop) to be visualized and the
UAV plays an important role in determining the detail of the information acquired. This is something
that depends on both the sensors and the resolution they offer. In the majority of cases, depending on
the purpose of the application, the spatial resolution of the photographs is between 0.5 cm/pixel and
10 cm/pixel.
Quite often, RGB sensors are modiﬁed to acquire information about the radiation in other bands
too, usually the Near Infrared (NIR) or the Red Edge (RE) band. This approach is observed when
the stakeholders want to avoid the higher costs of buying multispectral cameras. This is achieved by
replacing one of the original optical ﬁlters with one that enables the perception of near-infrared channel,
resulting often in a hybrid (e.g., NIR-RGB) sensor. The visible channel that is no longer captured by
the modiﬁed RGB sensor is often captured by using another embedded RGB sensor. The use of both
multispectral and visible sensors was observed in many cases [22,23,27,31,33,49,50,55,56,61,65,69,72,
87,103,107,113,117].
4. UAS Data Processing
This section focuses on the data processing techniques utilized to analyze the UAV imagery. To be
more precise, we discuss the different ways the information UAVs capture can be exploited to study
different vegetation features. The most common features that can be monitored with UAV-based
remote sensing for Precision Agriculture are presented in Table 1:

## Page 11

Information 2019, 10, 349
11 of 26
Table 1. Crop features that can be monitored with UAVs.
Crop Features
Vegetation
biomass [22,103]
nitrogen status [22,99,103,110]
moisture content [109,110]
vegetation color [49,54]
spectral behavior of chlorophyll [64,99]
temperature [64,69]
spatial position of an object [32,106]
size and shape of different elements and plants
vegetation indices [54–56]
Soil
moisture content [109,112]
temperature [66,69]
electrical conductivity [66]
With the use of specialized sensors, UAVs can acquire information for various features of the
cultivated ﬁeld. However, as mentioned above, there is still no standardized workﬂow or well
established techniques to follow for analyzing and visualizing the information acquired. The most
commonly used image processing methods y to analyze UAV imagery for Precision Agriculture
purposes are the following:
•
Photogrammetry techniques: Photogrammetry regards the accurate reconstruction of a scene or
an object from several overlapping pictures. Photogrammetric techniques can process the 2D data
and establish the geometric relationships between the different images and the object(s), obtaining
3D models. To construct the 3D models, photogrammetry requires at least two overlapping
images of the same scene and/or object(s), captured from different points of view. These kind of
techniques can be used for extracting three-dimensional digital surface or terrain models [37,40,43]
and/or orthophotos [50,55]. UAV low-altitude data acquisition enables the construction of 3D
models with a much higher spatial resolution compared to other remote sensing technologies
(such as satellites). However, the collection of many images is required to have information for
the entire ﬁeld under study. Thus, in most cases, it is necessary to collect many overlapping
images to construct Digital Elevation Models (DEMs) of the crops and/or create orthophotos
(also referred to as orthomosaics). The 3D models and the orthophotos include information about
the 3D characteristics of the crops based on the structure of the vegetation (e.g., the vegetation
height, the canopy, the density, etc.) and can be very useful for applications that can exploit only
RGB imagery. The works reviewed showed that photogrammetric techniques are very commonly
used in all types of applications as they are also required to create vegetation indices maps.
In addition, the 3D information they include is very important and is often used in tandem with
other techniques.
•
Machine learning methods: Machine Learning (ML) has been used to process the data acquired,
for prediction and/or identiﬁcation purposes, with great results in many domains, such as medical
systems [126,127], marketing [128], biology [129], etc. Machine learning techniques are often
been applied in Precision Agriculture to exploit the information from the large amount of data
acquired by the UAVs. ML is able to estimate some parameters regarding the crop growth rate,
detect diseases or even to identify/discriminate objects in the images. Machine learning usage
has increased a lot recently due to the fast advancements taking place especially in the deep
learning ﬁeld.
•
Vegetation Indices calculation: Vegetation Indices (VIs) are one of the most popular products
of remote sensing applications for Precision Agriculture.
They use different mathematical
combinations/transformations of at least two spectral bands of the electromagnetic spectrum,
designed to maximize the contribution of the vegetation characteristics while minimizing the
external confounding factors. They can deliver reliable spatial and temporal information about the

## Page 12

Information 2019, 10, 349
12 of 26
agricultural crops monitored. In most cases, many VIs are extracted and used to draw conclusions.
They can be calculated based on information of either each photograph individually or after the
production of orthophotos depicting the whole crop. Calculating vegetation indices may serve
in the identiﬁcation of useful crop characteristics, such as biological and physical parameters of
the vegetation.
Since the processing of data may be time consuming, several software tools and techniques have
been developed to enable faster data processing. The most commonly adopted software solutions in
the works reviewed to support and accelerate the data analysis procedure are summarized in Table 2.
In addition to the software tools referenced in the table, there are several other promising software
tools that can assist in the data analysis process, such as Erdas Imagine [130], eCognition [131], and
PixelWrench 2 [132].
Table 2. Most common software tools used in the literature for image processing.
Software Tool
Description
Adobe Photoshop [21,100]
Applied to correct distortion/use of other image processing methods
Agisoft Photoscan [22,36,37]
Exploited for the construction of 3D models and orthomosaics. It also
allows the calculation of vegetation indices
QGIS [23,55]
Usually exploited for the calculation of the vegetation indices from
multispectral data
MATLAB [35,100]
Applied mainly for the calculation of vegetation indices. It can also be
exploited for other image processing methods
Pix4D [29,35,55]
The most commonly used tool. It can be used for calculating VIs and/or
constructing of 3D models and orthomosaics
In the following subsections, we provide the details of the three most commonly used data
processing techniques to analyze data acquired from UAV ﬂights in the agricultural domain.
4.1. Photogrammetric Techniques
Photogrammetric techniques are mainly be applied for the construction of orthomosaics and/or
Digital Elevation Models (DEMs) in order to exploit the 3D information regarding the vegetation.
As mentioned above, this can be done by acquiring many overlapping images of the agricultural crops
monitored. The advancements in computer vision and photogrammetric techniques have lead to many
different techniques and algorithms that are able to match large numbers of overlapping images and
detect common objects and scenes in them. The images are processed by applying aerial triangulation
and adjusting camera orientation. Computer vision methods are used for matching the overlapping
images and the common characteristics. To achieve object tracking as well as to identify the scale and
the orientation of a particular image; in some cases, Ground Control Points (GCPs) are being used.
GCPs distributed in the cultivated ﬁeld can be identiﬁed within the overlapping images: (a) to link the
images; and (b) to identify the coordinates of each image and its slope. However, recent advancements
have made this redundant, as many techniques can be used without GCPs, with similar precision.
The construction of the 3D Digital Elevation Models can provide to the producer information
about the altitude of the earth surface, the natural and artiﬁcial objects/structures on the surface, the
density of the vegetation, and their growth, among others. There are two types of DEMs used:
•
The Digital Terrain Model (DTM) represents the altitude of the surface of the Earth, i.e., of the
terrain. These models do not take into account either artiﬁcial or natural (e.g., trees, vegetation,
buildings) objects that exist in the ﬁeld. DTMs just present the elevation of the bare Earth. Figure 3
shows a Digital Terrain Model from Ronchetti et al. [79].
•
The Digital Surface Model (DSM) represents the altitude of the surface that is ﬁrst encountered by
the remote sensing system (i.e., when the aerial image captures the top of a building, tree, the

## Page 13

Information 2019, 10, 349
13 of 26
vegetation etc.). Hence, the elevation model generated includes the elevation of the bare Earth
along with artiﬁcial and natural objects that may exist in the ﬁeld.
The DEMS constructed can be exploited either for the extraction of 3D information directly
or to construct orthomosaics of the crops. An orthoimage, orthomosaic or orthophoto is an aerial
photograph that is orthorectiﬁed (i.e., geometrically corrected). Thus, the scale of the constructed
image is uniform. As a result, the ﬁnal orthophoto has the same lack of distortion as a map. In contrast
with a simple aerial image of a ﬁeld, an orthophoto can be used to measure true distances as it contains
the 3D characteristics of the crops.
The use of photogrammetry techniques have the following procedure: create point cloud
representations of the 3D surface and either combine all objects into a single Digital Elevation Model
or use the DEMs to generate an orthophoto. The most commonly used set of algorithms for this
purpose is Structure from Motion (SfM) [133]. The main advantage of SfM is that it does not require
any information regarding the camera parameters or the environmental settings.
(a)
(b)
Figure 3. (a) A Digital Terrain Model [79]; and (b) a Digital Surface Model [109].
Photogrammetric techniques are commonly used in all types of applications as they are also
required for constructing the vegetation indices maps. Photogrammetric techniques are used in the
majority of recent works (93%) to exploit and extract information regarding the 3D characteristics of
the crops. However, photogrammetric techniques are in most cases used to compliment other types of
data processing methods.
4.2. Using Machine Learning
Machine Learning (ML) and Data Mining methods are widely used in PA to exploit the
information acquired by the UAVs. Taking into account the large amounts of data collected from
agricultural ﬁelds, machine learning can be applied to enhance the performance of UAV-based systems
for PA, by extracting knowledge for several parameters of the vegetation. ML is used in many cases
and for different purposes. Both unsupervised and supervised learning techniques are being exploited,
via clustering, classiﬁcation and regression methods.
Regression methods are widely used in UAV applications for PA for a variety of purposes.
Regression has been used to estimate spectral vegetation indices by analyzing data acquired from RGB
images [35], presenting generally good results. Additionally, regression has been used to examine the
correlation of some vegetation indices with vegetation features such as nitrogen [22,38,99], leaf are
index [36,103], and biomass [22,36,103]. For this purpose, both linear (simple and multiple) regression

## Page 14

Information 2019, 10, 349
14 of 26
and nonlinear regression methods have been used. In a comparison of different regression algorithms,
for estimating leaf nitrogen content, Random Forests presents the best results among 14 algorithms,
with the coefﬁcient of determination (R2) being up to 0.79 [38]. Regression methods are also used
to predict crop water status, by using information derived from RGB, multispectral and thermal
sensors [64,92,104]. In this context, Artiﬁcial Neural Networks present generally good results (R2 up
to 0.87 by using and information from some spectral bands).
Classiﬁcation methods are also very commonly used for weed mapping [18,33,44,73,106,111] and
disease detection [46,77,97]. The most popular and precise classiﬁcation techniques are the Artiﬁcial
Neural Networks (ANNs) family [18,44,73,104] and the Random Forest algorithm [22,38,49]. These
algorithms directly use the RGB colors, the intensity, spectral information or other features derived
from the image acquired. In some cases, data about the neighborhood of each pixel are also considered.
Apart from the above data, classiﬁcation algorithms can also use vegetation indices as features in
the model to achieve higher accuracy. In general, ANNs present higher accuracy, compared to other
classiﬁcation algorithms, that reaches up to 99% for weed mapping in some cases [98]. The accuracy
of the method depends on the type of the crops monitored [73] as expected. Convolutional Neural
Networks (CNNs), is among the most used family of algorithms. CNNs belong to deep learning
algorithms that have been proved to be very effective in object detection in large datasets.
The use of Deep Learning (DL) in Precision Agriculture applications is a recent, modern and
promising technique, having increasing popularity. Deep learning techniques extend typical ML by
adding more complexity into the derived models. DL techniques transform the data using various
functions that allow data representation in a hierarchical way, through several levels of abstraction.
Advancements and applications of Deep Learning into other domains indicate its large potential.
As indicated in [16,134], the use of Machine Learning and more particular Deep Learning will be even
more widespread in the next years.
A very common application of Machine Learning methods in PA is Object Based Image Analysis
(OBIA). The purpose of OBIA is to discriminate objects within agricultural images obtained from
UAVs [32,43].
In contrast to traditional pixel-based image classiﬁcation, which classiﬁes each
pixel, OBIA groups small pixels together into vector objects. With the higher spatial resolution
of UAV imagery, pixel-based classiﬁcations have become much less effective.
That is due to
the fact that the relationship between the pixel size and the object size has changed signiﬁcantly.
Therefore, object-oriented classiﬁcation methods are increasing in popularity. They use segmentation
methods to divide the image pixels into homogeneous segments/groups. Then, these segments/objects
are arranged into classes based on their geometric, spectral, textural and other characteristics.
OBIA is usually composed of two main steps:
1.
Image segmentation
2.
Feature extraction and classiﬁcation
These methods are exploited to recognize and detect weeds or discriminate different species in
the ﬁeld. A detailed review of algorithms and challenges for OBIA, from a remote sensing perspective,
was reported by Hossain and Chen [135].
4.3. Vegetation Indices
Vegetation Indices (VIs) have been widely used in remote sensing applications for Precision
Agriculture. They are considered to be very effective for monitoring the growth and health of crops
in qualitative and quantitative vegetation analysis [25,29,30]. Vegetation Indices are based on the
absorption of electromagnetic radiation by the vegetation.
They are mathematical transformations of the absorption and scattering in different bands of
the electromagnetic spectrum. The reﬂectance in several bands is affected by parameters such as
vegetation biochemical and physical properties, environmental effects, soil background properties,
moisture content, etc. The understanding of the spectral behavior of the vegetation is fundamental

## Page 15

Information 2019, 10, 349
15 of 26
to remote sensing applications to monitor various vegetation features (e.g., biomass [22], nitrogen
status [19,22], vegetation health [46], etc.) It has been shown that certain VIs are signiﬁcantly related
with different parameters of the vegetation.
Simple Vegetation Indices that can combine RGB information and some spectral bands such as
NIR and RE have signiﬁcantly improved the ability to detect green and healthy vegetation. Several VIs
have been developed, as different environments have their own complex characteristics, which needs
to be taken into account when using a Vegetation Index. Thus, each VI has its own speciﬁc combination
of the reﬂectance in different bands, in order to detect vegetation. Hence, its VI is suitable for speciﬁc
uses. The main concept is to combine the reﬂections of different bands to decrease the “noise” from
external factors (e.g., sensors calibration, lighting, atmosphere, soil properties, etc.). For example, as
mentioned in the previous section, visible radiation to the red is absorbed by the chlorophyll while the
radiation in the NIR band is strongly reﬂected. In this way, vegetation can be discriminated by the soil
in an image. In way, unhealthy vegetation can also be detected.
Vegetation Indices that are based on the radiation in the Red and NIR channels, such as the RVI
or the NDVI index, are designed to increase the contrast between the vegetation and the soil. The
relationship between the reﬂections of the two zones allows the elimination of disturbances by factors
that affect the radiation of each zone in the same way.
The effort to model the biophysical parameters of vegetation has led to the creation of several
different vegetation indices [136–139]. The vegetation indices can be divided into two main categories:
1.
Vegetation Indices based on multispectral or hyperspectral data. Most of the developed Vegetation
Indices use multispectral and/or hyperspectral information that can combine several bands.
2.
Vegetation Indices based on information from the visible spectrum. Several VIs in the visible
spectrum have been developed and are widely used due to the high cost of multispectral and
hyperspectral sensors.
A list of the most used vegetation indices is presented in Table 3. For the interpretation of
the following formulas, the following abbreviations represent the reﬂection in the respective color
or spectrum:
•
R: Red (620–670 nm)
•
G: Green (500–560 nm)
•
B: Blue (430–500 nm)
•
NIR: Near Infrared (720–1500 nm)
•
RE: Red Edge (670–720 nm)
Concerning the multispectral vegetation indices, one of the ﬁrst well-known indices was Ratio
Vegetation Index (RVI). This index enhances the contrast among vegetation and soil. However, it is
sensitive to the optical properties of ground. The best known and most widely used vegetation index
is the Normalized Difference Vegetation Index (NDVI), which is the evolution of RVI and is calculated
by the visible and near infrared light reﬂected from the vegetation. Unhealthy or sparse vegetation
reﬂects more visible light and less near infrared light, making it easy to monitor the growth and health
of many agricultural crops. It is based on absorption in Red due to chlorophyll and reﬂectance in NIR.
RVI and NDVI are calculated as shown in Table 3.

## Page 16

Information 2019, 10, 349
16 of 26
Table 3. Most used vegetation indices.
Vegetation Index
Abbreviation
Formula
Vegetation Indices derived from multispectral information
Ratio Vegetation Index
RVI
NIR
R
Normalized Difference Vegetation Index
NDVI
NIR −R
NIR + R
Normalized Difference Red Edge Index
NDRE
NIR −RE
NIR + RE
Green Normalized Difference Vegetation Index
GNDVI
NIR −G
NIR + G
RGB-based Vegetation Indices
Excess Greenness Index
ExG
2 ∗G −R −B
Normalized Difference Index
NDI
G −R
G + R
Several other VIs have been developed based on NDVI. NDRE uses the method of NDVI to
normalize the ratio of NIR radiation with Red Edge (RE) radiation. The same applies for GNDVI with
NIR and Green (G) bands.
Figure 4 shows examples of crop maps constructed from information of spectral VIs (NDVI and
NDRE) in different growth stages. We can see that the difference in the maps while the vegetation
grows is quite clear.
(a)
(b)
Figure 4.
Vegetation indices maps of crops in different growth stages [29]:
(a) NDVI maps;
and (b) NDRE maps
Focusing on the VIs extracted from RGB images, Excess Greenness Index (ExG) and Normalized
Difference Index (NDI) are the most used indices. ExG is based on the assumption that plants display
a clear high degree of greenness, and soil is the only background element. Thus, it is calculated
by doubling the radiation in the Green channel minus the radiation in Red and Blue channels.
NDI was proposed to separate plants from soil and residue background images, using only green and
red channels.

## Page 17

Information 2019, 10, 349
17 of 26
Although the VIs that use information in the visible light can be useful for crop monitoring,
they cannot provide information for several parameters of the vegetation and also they are sensitive
to working environment properties such as the atmosphere, lighting, etc. Hyperspectral remote
sensing is expected to be the future trend in crop monitoring and this is mainly because it allows the
development of new bands combination of vegetation indices. In many cases, it has been proved that
hyperspectral vegetation indices are less sensitive to saturation, change in viewing/lighting geometry,
and atmospheric contamination. The combination of new bands can eliminate noise from the working
environment and in the same time exploit the information of certain bands and extract information for
more biophysical features of the vegetation.
5. Limitations in the Use of UAVs for Precision Agriculture
Although the use of UAVs for PA is expanding there are several limitations that prevent their
wider use. The absence of a standardized workﬂow leads to the adoption of ad-hoc procedures for
deploying PA applications, a fact that discourages the relevant stakeholders. In addition, as PA requires
data-intensive procedures for the exploitation of the images acquired, skilled and expert personnel
is usually needed. This means that an average farmer may need training or even been forced to hire
experts to assist with the image processing, which may be costly. This fact may prohibit the adoption
of UAV technologies from individual farmers with only a few and small agricultural ﬁelds.
The high investment cost to purchase the Unmanned Aerial System is another prohibitive factor.
Producers with larger cultivated areas and higher proﬁt rates are able to use more sophisticated,
high-cost systems, though this is not the case for the majority of the ﬁelds in Europe. There were
10.5 million agricultural holdings in the EU in 2016, two-thirds of which were less than 5 hectares in
size, as shown in the Eurostat survey [140].
Another drawback stems from UAV technology limitations. Most commercial UAVs have a short
ﬂight time, ranging from 20 min to 1 h, covering a very restricted area at every ﬂight. UAVs that can
offer longer ﬂight time are relatively expensive. In addition, the effective use of UAVs is prone to
climatic conditions. For example, on a very windy or rainy day, the ﬂight should be postponed.
As the use of UAVs for agriculture purposes is considered to be commercial, UAV ﬂights should
also adhere to the related legislation and national rules. However, the EU regulations [141,142] for the
use of UAVs will replace national rules from July 2020. In practice, these regulations report that, once
an UAV pilot has received the appropriate authorization, he/she will be allowed to freely use UAVs in
the EU. The EU legislation will cover all types of possible UAVs operations, fostering the development
of innovative applications (e.g., for PA).
The EU regulations consider three categories of operations:
1.
Open category: Operations in this category do not require authorization or pilot license.
This category is limited to operations: in visual line of sight (VLOS), up to 120 m ﬂight height and
performed with UAVs compliant with some technical requirements deﬁned.
2.
Speciﬁc category: This is the second level of operations, which covers operations that are not
compliant to the restrictions of the open category and are considered “medium risk” operations.
Operators must perform a risk assessment (using a standardized method) and deﬁne mitigation
measures. Operations involving UAVs of more than 25 kg or not operated in VLOS will typically
fall under this category. The technical requirements for this category depend on the speciﬁc
authorized operation.
3.
Certiﬁed category: This category is considered high risk and includes operations involving large
drones in controlled air-spaces. Rules applicable to this category will be the same as for manned
aviation. This category does not concern the use of UAVs for Precision Agriculture.
Taking into account the rapid developments in UAV technology and the sensors use in PA,
the cost of the Unmanned Aerial Systems will be reduced in the near future. Practical limitations,
such as the short ﬂight time, are also expected to be solved by the advancements in technology.

## Page 18

Information 2019, 10, 349
18 of 26
These improvements will ensure that farmers can reap more from the use of UAVs for remote sensing
in Precision Agriculture.
6. Discussion and Conclusions
In this work, we review 100 recent applications of UAVs for Precision Agriculture. We present the
most frequent applications, the UAV types used and the Unmanned Aerial systems architecture for
PA. Then, we focus on the most used sensors for monitoring the crops and the processing methods
exploiting UAV imagery. We show that UAVs can have several applications, however monitoring crop
growth is the one that stands out. The following three main processing techniques stand out in the
literature for exploiting the information acquired:
1.
Photogrammetry techniques are used to construct Orthophotos or DEMs from the overlapping
images acquired. They are used in most of the applications to create vegetation maps considering
several characteristics; however, they are also used standalone mainly when only RGB sensors
are available, to exploit the 3D characteristics of the vegetation.
2.
Machine Learning methods can be used to monitor several different characteristics of the crops.
They can exploit RGB and/or multispectral/hyperspectral images. A very frequent technique
exploited in the literature is the Object Based Image Analysis.
3.
Vegetation Indices use combinations of the reﬂection of several bands obtained by RGB or spectral
sensors. They are proved to be most effective when multispectral or hyperspectral information is
used. They have been used in many recent studies. They have been proved to be very effective in
monitoring various parameters of the crops, by using different combinations of spectral bands.
In Figure 5, we present some statistics for the use of sensors and processing methods for the
different applications.
Figure 5. The use of sensors and processing techniques in the different UAVs applications.
We can observe that there is no standardized workﬂow in most cases and different techniques
are used to exploit UAV-acquired information for the same type of application. For example, looking
at the sensors and techniques used for monitoring the health of the crops, we can see that it is
relatively premature. Disease detection is mainly applied through temporal analysis of the vegetation’s
growth. However, multispectral and hyperspectral sensors seem to have great potential in this
context. An approach using multispectral sensing technologies could reliably deliver Vegetation
Indices, discriminating healthy and unhealthy portions of the vegetation. In such an approach, the
farmer could locate the “weak” corps ﬁeld areas and take timely decisions to save the parts of the crop
production that seem unhealthy.
On the contrary, considering weed mapping, we can see that some studies use machine learning
techniques to detect weeds, mainly OBIA, while others use the 3D characteristics of the crops though
DEMs, VIs or other processing methods. Weed detection with UAVs based on object-based image
analysis seems to be at an advanced stage and can be used for site-speciﬁc weed management. We can
see that machine learning techniques are exploited in 62.50% of the applications that used RGB sensors
and in all the applications with multispectral sensors.

## Page 19

Information 2019, 10, 349
19 of 26
Focusing on UAV-based growth monitoring, many different methods are really promising but it
seems that their integration in a standardized workﬂow can improve its applicability and efﬁciency.
Growth monitoring and yield prediction is most commonly performed with the use of RGB (30%)
and multispectral (59%) sensors. The information acquired is exploited for estimating the density of
production and the biomass. The ﬁndings of this review appoint that combining information coming
from Vegetation Indices with the 3D characteristics of the crops coming from RGB images can improve
the accuracy of growth and yield estimation methods.
In contrast with the above, the use of UAV systems for irrigation management is closer to
a standard workﬂow, which involves the use of thermal and/or multispectral sensors to monitor the
needs of water of different parts of the crops. Equipped with thermal sensors, the Unmanned Aerial
Vehicles are able to detect possible deﬁciencies in the irrigation of different sites. This information
can be processed through photogrammetry techniques into a single high-resolution vegetation map,
highlighting the stressed areas. A map in this context can be constructed though the use of some VIs
when multispectral imagery is used. Thus, a map such as this can support the producers to apply
Variable Rate Irrigation (VRI) applications.
Funding: This research was co-funded by the European Union and Greek national funds through the Operational
Program Competitiveness, Entrepreneurship, and Innovation, grant number T1EDK-04873.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
FAO. Declaration of the World Summit on Food Security; FAO: Rome, Italy, 2009.
2.
Mylonas, P.; Voutos, Y.; Sofou, A. A Collaborative Pilot Platform for Data Annotation and Enrichment in
Viticulture. Information 2019, 10, 149. [CrossRef]
3.
Mulla, D.J. Twenty ﬁve years of remote sensing in precision agriculture: Key advances and remaining
knowledge gaps. Biosyst. Eng. 2013, 114, 358–371. [CrossRef]
4.
Bauer, M.E.; Cipra, J.E. Identiﬁcation of Agricultural Crops by Computer Processing of ERTS MSS Data; LARS
Technical Reports; Purdue University: West Lafayette, IN, USA 1973; p. 20.
5.
Mora, A.; Santos, T.; Lukasik, S.; Silva, J.; Falcao, A.; Fonseca, J.; Ribeiro, R. Land cover classiﬁcation from
multispectral data using computational intelligence tools: A comparative study. Information 2017, 8, 147.
[CrossRef]
6.
Taylor, J.; William, R.; Munson, K. Jane’s Pocket Book of Remotely Piloted Vehicles: Robot Aircraft Today; Collier
Books: New York, NY, USA, 1977.
7.
Zhang, C.; Kovacs, J.M. The application of small unmanned aerial systems for precision agriculture: A review.
Precis. Agric. 2012, 13, 693–712. [CrossRef]
8.
Yang, S.; Yang, X.; Mo, J. The application of unmanned aircraft systems to plant protection in China.
Precis. Agric. 2018, 19, 278–292. [CrossRef]
9.
Yang, G.; Liu, J.; Zhao, C.; Li, Z.; Huang, Y.; Yu, H.; Xu, B.; Yang, X.; Zhu, D.; Zhang, X.; et al. Unmanned aerial
vehicle remote sensing for ﬁeld-based crop phenotyping: Current status and perspectives. Front. Plant Sci.
2017, 8, 1111. [CrossRef] [PubMed]
10.
Mogili,
U.R.;
Deepak,
B.
Review on application of drone systems in precision agriculture.
Procedia Comput. Sci. 2018, 133, 502–509. [CrossRef]
11.
Puri, V.; Nayyar, A.; Raja, L. Agriculture drones: A modern breakthrough in precision agriculture. J. Stat.
Manag. Syst. 2017, 20, 507–518. [CrossRef]
12.
Kulbacki, M.; Segen, J.; Knie´c, W.; Klempous, R.; Kluwak, K.; Nikodem, J.; Kulbacka, J.; Serester, A. Survey
of Drones for Agriculture Automation from Planting to Harvest. In Proceedings of the 2018 IEEE 22nd
International Conference on Intelligent Engineering Systems (INES), Las Palmas de Gran Canaria, Spain,
21–23 June 2018; pp. 000353–000358.
13.
Manfreda, S.; McCabe, M.; Miller, P.; Lucas, R.; Pajuelo Madrigal, V.; Mallinis, G.; Ben Dor, E.; Helman,
D.; Estes, L.; Ciraolo, G.; et al. On the use of unmanned aerial systems for environmental monitoring.
Remote Sens. 2018, 10, 641. [CrossRef]

## Page 20

Information 2019, 10, 349
20 of 26
14.
Adão, T.; Hruška, J.; Pádua, L.; Bessa, J.; Peres, E.; Morais, R.; Sousa, J. Hyperspectral imaging: A review on
UAV-based sensors, data processing and applications for agriculture and forestry. Remote Sens. 2017, 9, 1110.
[CrossRef]
15.
Maes, W.H.; Steppe, K.
Perspectives for remote sensing with unmanned aerial vehicles in precision
agriculture. Trends Plant Sci. 2019, 24, 152–164. [CrossRef] [PubMed]
16.
Kamilaris, A.; Prenafeta-Boldu, F.X. Deep learning in agriculture: A survey. Comput. Electron. Agric. 2018,
147, 70–90. [CrossRef]
17.
Tsouros, D.C.; Triantafyllou, A.; Bibi, S.; Sarigannidis, P.G. Data acquisition and analysis methods in
UAV-based applications for Precision Agriculture. In Proceedings of the 2019 IEEE 15th International
Conference on Distributed Computing in Sensor Systems (DCOSS), Santorini Island, Greece, 29–31 May
2019; pp. 377–384
18.
Huang, H.; Deng, J.; Lan, Y.; Yang, A.; Deng, X.; Zhang, L. A fully convolutional network for weed mapping
of unmanned aerial vehicle (UAV) imagery. PLoS ONE 2018, 13, 1–19. [CrossRef] [PubMed]
19.
Hunt, E.R.; Horneck, D.A.; Spinelli, C.B.; Turner, R.W.; Bruce, A.E.; Gadler, D.J.; Brungardt, J.J.; Hamm, P.B.
Monitoring nitrogen status of potatoes using small unmanned aerial vehicles. Precis. Agric. 2018, 19, 314–333.
[CrossRef]
20.
Zhang, J.; Basso, B.; Price, R.F.; Putman, G.; Shuai, G. Estimating plant distance in maize using Unmanned
Aerial Vehicle (UAV). PLoS ONE 2018, 13, e0195223. [CrossRef] [PubMed]
21.
Wang, J.J.; Ge, H.; Dai, Q.; Ahmad, I.; Dai, Q.; Zhou, G.; Qin, M.; Gu, C. Unsupervised discrimination
between lodged and non-lodged winter wheat: A case study using a low-cost unmanned aerial vehicle. Int.
J. Remote Sens. 2018, 39, 2079–2088. [CrossRef]
22.
Näsi, R.; Viljanen, N.; Kaivosoja, J.; Alhonoja, K.; Hakala, T.; Markelin, L.; Honkavaara, E. Estimating Biomass
and Nitrogen Amount of Barley and Grass Using UAV and Aircraft Based Spectral and Photogrammetric 3D
Features. Remote Sens. 2018, 10, 1082. [CrossRef]
23.
Yonah, I.B.; Mourice, S.K.; Tumbo, S.D.; Mbilinyi, B.P.; Dempewolf, J. Unmanned aerial vehicle-based
remote sensing in monitoring smallholder, heterogeneous crop ﬁelds in Tanzania. Int. J. Remote Sens. 2018,
39, 5453–5471. [CrossRef]
24.
Kellenberger, B.; Marcos, D.; Tuia, D. Detecting mammals in UAV images: Best practices to address
a substantially imbalanced dataset with deep learning. Remote Sens. Environ. 2018, 216, 139–153. [CrossRef]
25.
Mozgeris, G.; Jonikaviˇcius, D.; Jovarauskas, D.; Zinkeviˇcius, R.; Petkeviˇcius, S.; Steponaviˇcius, D.
Imaging from manned ultra-light and unmanned aerial vehicles for estimating properties of spring wheat.
Precis. Agric. 2018, 19, 876–894. [CrossRef]
26.
Deng, L.; Mao, Z.; Li, X.; Hu, Z.; Duan, F.; Yan, Y. UAV-based multispectral remote sensing for precision
agriculture: A comparison between different cameras. ISPRS J. Photogramm. Remote Sens. 2018, 146, 124–136.
[CrossRef]
27.
Zheng, H.; Cheng, T.; Li, D.; Zhou, X.; Yao, X.; Tian, Y.; Cao, W.; Zhu, Y. Evaluation of RGB, color-infrared and
multispectral images acquired from unmanned aerial systems for the estimation of nitrogen accumulation in
rice. Remote Sens. 2018, 10, 824. [CrossRef]
28.
Tewes, A.; Schellberg, J. Towards remote estimation of radiation use efﬁciency in maize using uav-based
low-cost camera imagery. Agronomy 2018, 8, 16. [CrossRef]
29.
Raeva, P.L.; Šedina, J.; Dlesk, A. Monitoring of crop ﬁelds using multispectral and thermal imagery from
UAV. Eur. J. Remote Sens. 2019, 52, 192–201. [CrossRef]
30.
Huang, Y.; Reddy, K.N.; Fletcher, R.S.; Pennington, D. UAV low-altitude remote sensing for precision weed
management. Weed Technol. 2018, 32, 2–6. [CrossRef]
31.
Gracia-Romero, A.; Vergara-Díaz, O.; Thierfelder, C.; Cairns, J.; Kefauver, S.; Araus, J.
Phenotyping
conservation agriculture management effects on ground and aerial remote sensing assessments of maize
hybrids performance in Zimbabwe. Remote Sens. 2018, 10, 349. [CrossRef]
32.
De Castro, A.I.; Torres-Sánchez, J.; Peña, J.M.; Jiménez-Brenes, F.M.; Csillik, O.; López-Granados, F.
An Automatic Random Forest-OBIA Algorithm for Early Weed Mapping between and within Crop Rows
Using UAV Imagery. Remote Sens. 2018, 10, 285. [CrossRef]
33.
Lambert, J.; Hicks, H.; Childs, D.; Freckleton, R. Evaluating the potential of Unmanned Aerial Systems
for mapping weeds at ﬁeld scales: A case study with Alopecurus myosuroides. Weed Res. 2018, 58, 35–45.
[CrossRef] [PubMed]

## Page 21

Information 2019, 10, 349
21 of 26
34.
Uddin, M.A.; Mansour, A.; Jeune, D.L.; Ayaz, M.; Aggoune, E.-H.M. UAV-assisted dynamic clustering of
wireless sensor networks for crop health monitoring. Sensors 2018, 18, 555. [CrossRef] [PubMed]
35.
Khan, Z.; Rahimi-Eichi, V.; Haefele, S.; Garnett, T.; Miklavcic, S.J. Estimation of vegetation indices for
high-throughput phenotyping of wheat using aerial imaging.
Plant Methods 2018, 14, 20. [CrossRef]
[PubMed]
36.
Fan, X.; Kawamura, K.; Xuan, T.D.; Yuba, N.; Lim, J.; Yoshitoshi, R.; Minh, T.N.; Kurokawa, Y.; Obitsu, T.
Low-cost visible and near-infrared camera on an unmanned aerial vehicle for assessing the herbage biomass
and leaf area index in an Italian ryegrass ﬁeld. Grassl. Sci. 2018, 64, 145–150. [CrossRef]
37.
Ziliani, M.; Parkes, S.; Hoteit, I.; McCabe, M. Intra-Season Crop Height Variability at Commercial Farm
Scales Using a Fixed-Wing UAV. Remote Sens. 2018, 10, 2007. [CrossRef]
38.
Zheng, H.; Li, W.; Jiang, J.; Liu, Y.; Cheng, T.; Tian, Y.; Zhu, Y.; Cao, W.; Zhang, Y.; Yao, X. A Comparative
Assessment of Different Modeling Algorithms for Estimating Leaf Nitrogen Content in Winter Wheat Using
Multispectral Images from an Unmanned Aerial Vehicle. Remote Sens. 2018, 10, 2026. [CrossRef]
39.
Han, X.; Thomasson, J.A.; Bagnall, G.C.; Pugh, N.; Horne, D.W.; Rooney, W.L.; Jung, J.; Chang, A.;
Malambo, L.; Popescu, S.C.; et al.
Measurement and calibration of plant-height from ﬁxed-wing UAV
images. Sensors 2018, 18, 4092. [CrossRef] [PubMed]
40.
Torres-Sánchez, J.; de Castro, A.I.; Peña, J.M.; Jiménez-Brenes, F.M.; Arquero, O.; Lovera, M.;
López-Granados, F. Mapping the 3D structure of almond trees using UAV acquired photogrammetric
point clouds and object-based image analysis. Biosyst. Eng. 2018, 176, 172–184. [CrossRef]
41.
Comba, L.; Biglia, A.; Aimonino, D.R.; Gay, P. Unsupervised detection of vineyards by 3D point-cloud UAV
photogrammetry for precision agriculture. Comput. Electron. Agric. 2018, 155, 84–95. [CrossRef]
42.
Su, J.; Liu, C.; Coombes, M.; Hu, X.; Wang, C.; Xu, X.; Li, Q.; Guo, L.; Chen, W.H. Wheat yellow rust
monitoring by learning from multispectral UAV aerial imagery. Comput. Electron. Agric. 2018, 155, 157–166.
[CrossRef]
43.
De Castro, A.; Jiménez-Brenes, F.; Torres-Sánchez, J.; Peña, J.; Borra-Serrano, I.; López-Granados, F. 3-D
characterization of vineyards using a novel UAV imagery-based OBIA procedure for precision viticulture
applications. Remote Sens. 2018, 10, 584. [CrossRef]
44.
Bah, M.D.; Haﬁane, A.; Canals, R. Deep Learning with Unsupervised Data Labeling for Weed Detection in
Line Crops in UAV Images. Remote Sens. 2018, 10, 1690. [CrossRef]
45.
Wierzbicki, D.; Fryskowska, A.; Kedzierski, M.; Wojtkowska, M.; Delis, P. Method of radiometric quality
assessment of NIR images acquired with a custom sensor mounted on an unmanned aerial vehicle. J. Appl.
Remote Sens. 2018, 12, 015008. [CrossRef]
46.
Kerkech, M.; Haﬁane, A.; Canals, R. Deep leaning approach with colorimetric spaces and vegetation indices
for vine diseases detection in UAV images. Comput. Electron. Agric. 2018, 155, 237–243. [CrossRef]
47.
Latif, M.A.; Cheema, M.J.M.; Saleem, M.F.; Maqsood, M. Mapping wheat response to variations in N, P, Zn,
and irrigation using an unmanned aerial vehicle. Int. J. Remote Sens. 2018, 39, 7172–7188. [CrossRef]
48.
Jung, J.; Maeda, M.; Chang, A.; Landivar, J.; Yeom, J.; McGinty, J. Unmanned aerial system assisted
framework for the selection of high yielding cotton genotypes. Comput. Electron. Agric. 2018, 152, 74–81.
[CrossRef]
49.
Wan, L.; Li, Y.; Cen, H.; Zhu, J.; Yin, W.; Wu, W.; Zhu, H.; Sun, D.; Zhou, W.; He, Y. Combining UAV-Based
Vegetation Indices and Image Classiﬁcation to Estimate Flower Number in Oilseed Rape. Remote Sens. 2018,
10, 1484. [CrossRef]
50.
Sa, I.; Popovi´c, M.; Khanna, R.; Chen, Z.; Lottes, P.; Liebisch, F.; Nieto, J.; Stachniss, C.; Walter, A.; Siegwart, R.
Weedmap: A large-scale semantic weed mapping framework using aerial multispectral imaging and deep
neural network for precision farming. Remote Sens. 2018, 10, 1423. [CrossRef]
51.
Ballesteros, R.; Ortega, J.F.; Hernandez, D.; Moreno, M.A. Onion biomass monitoring using UAV-based RGB
imaging. Precis. Agric. 2018, 19, 840–857. [CrossRef]
52.
Simic Milas, A.; Romanko, M.; Reil, P.; Abeysinghe, T.; Marambe, A. The importance of leaf area index
in mapping chlorophyll content of corn under different agricultural treatments using UAV images. Int. J.
Remote Sens. 2018, 39, 5415–5431. [CrossRef]
53.
Mesas-Carrascosa, F.J.; Pérez-Porras, F.; Meroño de Larriva, J.; Mena Frau, C.; Agüera-Vega, F.;
Carvajal-Ramírez, F.; Martínez-Carricondo, P.; García-Ferrer, A.
Drift correction of lightweight
microbolometer thermal sensors on-board unmanned aerial vehicles. Remote Sens. 2018, 10, 615. [CrossRef]

## Page 22

Information 2019, 10, 349
22 of 26
54.
Varela, S.; Dhodda, P.; Hsu, W.; Prasad, P.; Assefa, Y.; Peralta, N.; Grifﬁn, T.; Sharda, A.; Ferguson, A.;
Ciampitti, I. Early-season stand count determination in corn via integration of imagery from unmanned
aerial systems (UAS) and supervised learning techniques. Remote Sens. 2018, 10, 343. [CrossRef]
55.
Marino, S.; Alvino, A. Detection of homogeneous wheat areas using multi-temporal UAS images and ground
truth data analyzed by cluster analysis. Eur. J. Remote Sens. 2018, 51, 266–275. [CrossRef]
56.
Marcial-Pablo,
M.d.J.;
Gonzalez-Sanchez,
A.;
Jimenez-Jimenez,
S.I.;
Ontiveros-Capurata,
R.E.;
Ojeda-Bustamante, W. Estimation of vegetation fraction using RGB and multispectral images from UAV.
Int. J. Remote Sens. 2019, 40, 420–438. [CrossRef]
57.
Oliveira, H.C.; Guizilini, V.C.; Nunes, I.P.; Souza, J.R. Failure detection in row crops from UAV images using
morphological operators. IEEE Geosci. Remote Sens. Lett. 2018, 15, 991–995. [CrossRef]
58.
Mafanya, M.; Tsele, P.; Botai, J.O.; Manyama, P.; Chirima, G.J.; Monate, T. Radiometric calibration framework
for ultra-high-resolution UAV-derived orthomosaics for large-scale mapping of invasive alien plants in
semi-arid woodlands: Harrisia pomanensis as a case study.
Int. J. Remote Sens. 2018, 39, 5119–5140.
[CrossRef]
59.
Hassanein, M.; Lari, Z.; El-Sheimy, N. A new vegetation segmentation approach for cropped ﬁelds based on
threshold detection from hue histograms. Sensors 2018, 18, 1253. [CrossRef] [PubMed]
60.
Jeong, S.; Ko, J.; Choi, J.; Xue, W.; Yeom, J.-m. Application of an unmanned aerial system for monitoring
paddy productivity using the GRAMI-rice model. Int. J. Remote Sens. 2018, 39, 2441–2462. [CrossRef]
61.
Iwasaki, K.; Torita, H.; Abe, T.; Uraike, T.; Touze, M.; Fukuchi, M.; Sato, H.; Iijima, T.; Imaoka, K.; Igawa, H.
Spatial pattern of windbreak effects on maize growth evaluated by an unmanned aerial vehicle in Hokkaido,
northern Japan. Agrofor. Syst. 2019, 93, 1133–1145. [CrossRef]
62.
Li, Y.; Qian, M.; Liu, P.; Cai, Q.; Li, X.; Guo, J.; Yan, H.; Yu, F.; Yuan, K.; Yu, J.; et al. The recognition of rice
images by UAV based on capsule network. Clust. Comput. 2018, 1–10. [CrossRef]
63.
Aasen, H.; Bolten, A.
Multi-temporal high-resolution imaging spectroscopy with hyperspectral 2D
imagers–From theory to application. Remote Sens. Environ. 2018, 205, 374–389. [CrossRef]
64.
Quebrajo, L.; Perez-Ruiz, M.; Pérez-Urrestarazu, L.; Martínez, G.; Egea, G. Linking thermal imaging and soil
remote sensing to enhance irrigation management of sugar beet. Biosyst. Eng. 2018, 165, 77–87. [CrossRef]
65.
Han, L.; Yang, G.; Yang, H.; Xu, B.; Li, Z.; Yang, X. Clustering ﬁeld-based maize phenotyping of plant-height
growth and canopy spectral dynamics using a UAV remote-sensing approach. Front. Plant Sci. 2018, 9, 1638.
[CrossRef] [PubMed]
66.
Kˇrížová, K.; Kroulík, M.; Haberle, J.; Lukáš, J.; Kumhálová, J. Assessment of soil electrical conductivity using
remotely sensed thermal data. Agron. Res. 2018, 16, 784–793.
67.
Huang, C.-y.; Wei, H.L.; Rau, J.Y.; Jhan, J.P. Use of principal components of UAV-acquired narrow-band
multispectral imagery to map the diverse low stature vegetation fAPAR. GISci. Remote Sens. 2019, 56, 605–623.
[CrossRef]
68.
Souza, I.R.; Escarpinati, M.C.; Abdala, D.D. A curve completion algorithm for agricultural planning.
In Proceedings of the 33rd Annual ACM Symposium on Applied Computing, Pau, France, 9–13 April 2018;
pp. 284–291.
69.
Pascuzzi, S.; Anifantis, A.S.; Cimino, V.; Santoro, F. Unmanned aerial vehicle used for remote sensing on an
apulian farm in southern Italy. In Proceedings of the 17th International Scientiﬁc Conference Engineering for
Rural Development, Jelgava, Latvia, 23–25 May 2018; pp. 23–25.
70.
Bah, M.D.; Haﬁane, A.; Canals, R. Weeds detection in UAV imagery using SLIC and the hough transform.
In Proceedings of the 2017 Seventh International Conference on Image Processing Theory, Tools and
Applications (IPTA), Montreal, QC, Canada, 28 November–1 December 2017; pp. 1–6.
71.
Pantelej, E.; Gusev, N.; Voshchuk, G.; Zhelonkin, A. Automated ﬁeld monitoring by a group of light
aircraft-type UAVs. In Proceedings of the International Conference on Intelligent Information Technologies
for Industry, Sochi, Russia, 17–21 September 2018; Springer: Cham, Switzerland, 2018; pp. 350–358.
72.
Parraga, A.; Doering, D.; Atkinson, J.G.; Bertani, T.; de Oliveira Andrades Filho, C.; de Souza, M.R.Q.;
Ruschel, R.; Susin, A.A. Wheat Plots Segmentation for Experimental Agricultural Field from Visible and
Multispectral UAV Imaging. In Proceedings of the SAI Intelligent Systems Conference, London, UK,
6–7 September 2018; Springer: Cham, Switzerland, 2018; pp. 388–399.

## Page 23

Information 2019, 10, 349
23 of 26
73.
Bah, M.D.; Dericquebourg, E.; Haﬁane, A.; Canals, R. Deep Learning Based Classiﬁcation System for
Identifying Weeds Using High-Resolution UAV Imagery. In Proceedings of the Science and Information
Conference, London, UK, 10–12 July 2018; Springer: Cham, Switzerland, 2018; pp. 176–187.
74.
Mancini, A.; Frontoni, E.; Zingaretti, P. Improving Variable Rate Treatments by Integrating Aerial and
Ground Remotely Sensed Data. In Proceedings of the 2018 International Conference on Unmanned Aircraft
Systems (ICUAS), Dallas, TX, USA, 12–15 June 2018; pp. 856–863.
75.
Palomino, W.; Morales, G.; Huamán, S.; Telles, J. PETEFA: Geographic Information System for Precision
Agriculture. In Proceedings of the 2018 IEEE XXV International Conference on Electronics, Electrical
Engineering and Computing (INTERCON), Lima, Peru, 8–10 August 2018; pp. 1–4.
76.
De Oca, A.M.; Arreola, L.; Flores, A.; Sanchez, J.; Flores, G. Low-cost multispectral imaging system for crop
monitoring. In Proceedings of the 2018 International Conference on Unmanned Aircraft Systems (ICUAS),
Dallas, TX, USA, 12–15 June 2018; pp. 443–451.
77.
Montero, D.; Rueda, C. Detection of palm oil bud rot employing artiﬁcial vision. In IOP Conference Series:
Materials Science and Engineering; IOP Publishing: Bristol, UK, 2018; Volume 437, p. 012004.
78.
Wang, X.; Sun, H.; Long, Y.; Zheng, L.; Liu, H.; Li, M. Development of Visualization System for Agricultural
UAV Crop Growth Information Collection. IFAC-PapersOnLine 2018, 51, 631–636. [CrossRef]
79.
Ronchetti, G.; Pagliari, D.; Sona, G. DTM Generation Through UAV Survey With a FISHEYE Camera On a
Vineyard. Int. Arch. Photogramm. Remote Sens. Spat. Inf. Sci. 2018, 42, 2. [CrossRef]
80.
Hassanein, M.; El-Sheimy, N. An efﬁcient weed detection procedure using low-cost UAV imagery system for
precision agriculture applications. Int. Arch. Photogramm. Remote Sens. Spat. Inf. Sci. 2018. [CrossRef]
81.
Lussem, U.; Bolten, A.; Gnyp, M.; Jasper, J.; Bareth, G. Evaluation of RGB-based vegetation indices from
UAV imagery to estimate forage yield in Grassland. ISPRS-Int. Arch. Photogramm. Remote Sens. Spat. Inf. Sci.
2018, 1215–1219. [CrossRef]
82.
Rudd, J.D.; Roberson, G.T. Using unmanned aircraft systems to develop variable rate prescription maps
for cotton defoliants. In Proceedings of the 2018 ASABE Annual International Meeting, Detroit, MI, USA,
29 July–1 August 2018; American Society of Agricultural and Biological Engineers: St. Joseph, MI, USA,
2018; p. 1.
83.
Soares, G.A.; Abdala, D.D.; Escarpinati, M. Plantation Rows Identiﬁcation by Means of Image Tiling and
Hough Transform. In Proceedings of the 13th International Joint Conference on Computer Vision, Imaging
and Computer Graphics Theory and Applications (VISIGRAPP 2018), Madeira, Portugal, 27–29 January
2018; pp. 453–459.
84.
Zhao, T.; Niu, H.; de la Rosa, E.; Doll, D.; Wang, D.; Chen, Y. Tree canopy differentiation using instance-aware
semantic segmentation. In Proceedings of the 2018 ASABE Annual International Meeting, Detroit, MI, USA,
29 July–1 August 2018; American Society of Agricultural and Biological Engineers: St. Joseph, MI, USA,
2018; p. 1.
85.
Zhao, T.; Yang, Y.; Niu, H.; Wang, D.; Chen, Y. Comparing U-Net convolutional network with mask R-CNN
in the performances of pomegranate tree canopy segmentation. Proc. SPIE 2018, 10780, 107801J.
86.
Pap, M.; Kiraly, S. Comparison of segmentation methods on images of energy plants obtained by UAVs.
In Proceedings of the 2018 IEEE International Conference on Future IoT Technologies (Future IoT), Eger,
Hungary, 18–19 January 2018; pp. 1–8.
87.
Wahab, I.; Hall, O.; Jirström, M. Remote Sensing of Yields: Application of UAV Imagery-Derived NDVI for
Estimating Maize Vigor and Yields in Complex Farming Systems in Sub-Saharan Africa. Drones 2018, 2, 28.
[CrossRef]
88.
Bhandari, S.; Raheja, A.; Chaichi, M.R.; Green, R.L.; Do, D.; Pham, F.H.; Ansari, M.; Wolf, J.G.; Sherman, T.M.;
Espinas, A. Effectiveness of UAV-Based Remote Sensing Techniques in Determining Lettuce Nitrogen and
Water Stresses. In Proceedings of the 14th International Conference in Precision Agriculture, Montreal, QC,
Canada, 24–27 June 2018.
89.
Xue, X.; Lan, Y.; Sun, Z.; Chang, C.; Hoffmann, W.C. Develop an unmanned aerial vehicle based automatic
aerial spraying system. Comput. Electron. Agric. 2016, 128, 58–66. [CrossRef]
90.
Hunt, E., Jr.; Horneck, D.; Hamm, P.; Gadler, D.; Bruce, A.; Turner, R.; Spinelli, C.; Brungardt, J. Detection
of nitrogen deﬁciency in potatoes using small unmanned aircraft systems. In Proceedings of the 12th
International Conference on Precision Agriculture, Sacramento, CA, USA, 20–23 July 2014.

## Page 24

Information 2019, 10, 349
24 of 26
91.
Bellvert, J.; Zarco-Tejada, P.J.; Marsal, J.; Girona, J.; González-Dugo, V.; Fereres, E. Vineyard irrigation
scheduling based on airborne thermal imagery and water potential thresholds. Aust. J. Grape Wine Res. 2016,
22, 307–315. [CrossRef]
92.
Romero, M.; Luo, Y.; Su, B.; Fuentes, S. Vineyard water status estimation using multispectral imagery from
an UAV platform and machine learning algorithms for irrigation scheduling management. Comput. Electron.
Agric. 2018, 147, 109–117. [CrossRef]
93.
Wang, G.; Lan, Y.; Qi, H.; Chen, P.; Hewitt, A.; Han, Y. Field evaluation of an unmanned aerial vehicle (UAV)
sprayer: Effect of spray volume on deposition and the control of pests and disease in wheat. Pest Manag. Sci.
2019, 75, 1546–1555. [CrossRef] [PubMed]
94.
Hentschke, M.; Pignaton de Freitas, E.; Hennig, C.; Girardi da Veiga, I. Evaluation of Altitude Sensors for
a Crop Spraying Drone. Drones 2018, 2, 25. [CrossRef]
95.
Garre, P.; Harish, A. Autonomous Agricultural Pesticide Spraying UAV. In IOP Conference Series: Materials
Science and Engineering; IOP Publishing: Bristol, UK, 2018; Volume 455, p. 012030.
96.
Lan, Y.; Chen, S. Current status and trends of plant protection UAV and its spraying technology in China.
Int. J. Precis. Agric. Aviat. 2018, 1, 1–9. [CrossRef]
97.
Albetis, J.; Jacquin, A.; Goulard, M.; Poilvé, H.; Rousseau, J.; Clenet, H.; Dedieu, G.; Duthoit, S. On the
potentiality of UAV multispectral imagery to detect Flavescence dorée and Grapevine Trunk Diseases.
Remote Sens. 2019, 11, 23. [CrossRef]
98.
Dos Santos Ferreira, A.; Freitas, D.M.; da Silva, G.G.; Pistori, H.; Folhes, M.T. Weed detection in soybean
crops using ConvNets. Comput. Electron. Agric. 2017, 143, 314–324. [CrossRef]
99.
Ballester, C.; Hornbuckle, J.; Brinkhoff, J.; Smith, J.; Quayle, W. Assessment of in-season cotton nitrogen
status and lint yield prediction from unmanned aerial system imagery. Remote Sens. 2017, 9, 1149. [CrossRef]
100. Gnädinger, F.; Schmidhalter, U. Digital counts of maize plants by unmanned aerial vehicles (UAVs).
Remote Sens. 2017, 9, 544. [CrossRef]
101. Percival, D.; Gallant, D.; Harrington, T.; Brown, G. Potential for commercial unmanned aerial vehicle
use in wild blueberry production. In XI International Vaccinium Symposium 1180; International Society for
Horticultural Science (ISHS): Orlando, FL, USA, 2016; pp. 233–240.
102. Yao, X.; Wang, N.; Liu, Y.; Cheng, T.; Tian, Y.; Chen, Q.; Zhu, Y. Estimation of wheat LAI at middle to
high levels using unmanned aerial vehicle narrowband multispectral imagery. Remote Sens. 2017, 9, 1304.
[CrossRef]
103. Maimaitijiang, M.; Ghulam, A.; Sidike, P.; Hartling, S.; Maimaitiyiming, M.; Peterson, K.; Shavers, E.;
Fishman, J.; Peterson, J.; Kadam, S.; et al. Unmanned Aerial System (UAS)-based phenotyping of soybean
using multi-sensor data fusion and extreme learning machine. ISPRS J. Photogramm. Remote Sens. 2017,
134, 43–58. [CrossRef]
104. Poblete, T.; Ortega-Farías, S.; Moreno, M.; Bardeen, M. Artiﬁcial neural network to predict vine water status
spatial variability using multispectral information obtained from an unmanned aerial vehicle (UAV). Sensors
2017, 17, 2488. [CrossRef] [PubMed]
105. Jermthaisong, P.; Kingpaiboon, S.; Chawakitchareon, P.; Kiyoki, Y. Relationship between vegetation indices
and SPAD values of waxy corn using an unmanned aerial vehicle. Inf. Model. Knowl. Bases XXX 2019,
312, 312.
106. Gao, J.; Liao, W.; Nuyttens, D.; Lootens, P.; Vangeyte, J.; Pižurica, A.; He, Y.; Pieters, J.G. Fusion of pixel
and object-based features for weed mapping using unmanned aerial vehicle imagery. Int. J. Appl. Earth
Obs. Geoinf. 2018, 67, 43–53. [CrossRef]
107. Iqbal, F.; Lucieer, A.; Barry, K. Poppy crop capsule volume estimation using UAS remote sensing and random
forest regression. Int. J. Appl. Earth Obs. Geoinf. 2018, 73, 362–373. [CrossRef]
108. Huuskonen, J.; Oksanen, T. Soil sampling with drones and augmented reality in precision agriculture.
Comput. Electron. Agric. 2018, 154, 25–35. [CrossRef]
109. Jorge, J.; Vallbé, M.; Soler, J.A. Detection of irrigation inhomogeneities in an olive grove using the NDRE
vegetation index obtained from UAV images. Eur. J. Remote Sens. 2019, 52, 169–177. [CrossRef]
110. Bhandari, S.; Raheja, A.; Chaichi, M.R.; Green, R.L.; Do, D.; Pham, F.H.; Ansari, M.; Wolf, J.G.; Sherman, T.M.;
Espinas, A. Lessons Learned from UAV-Based Remote Sensing for Precision Agriculture. In Proceedings of
the 2018 International Conference on Unmanned Aircraft Systems (ICUAS), Dallas, TX, USA, 12–15 June
2018; pp. 458–467.

## Page 25

Information 2019, 10, 349
25 of 26
111. Franco, C.; Guada, C.; Rodríguez, J.T.; Nielsen, J.; Rasmussen, J.; Gómez, D.; Montero, J. Automatic detection
of thistle-weeds in cereal crops from aerial RGB images. In International Conference on Information Processing
and Management of Uncertainty in Knowledge-Based Systems; Springer: Cham, Switzerland, 2018; pp. 441–452.
112. Sobayo, R.; Wu, H.H.; Ray, R.; Qian, L. Integration of Convolutional Neural Network and Thermal Images
into Soil Moisture Estimation. In Proceedings of the 2018 1st International Conference on Data Intelligence
and Security (ICDIS), South Padre Island, TX, USA, 8–10 April 2018; pp. 207–210.
113. Oliveira, R.; Khoramshahi, E.; Suomalainen, J.; Hakala, T.; Viljanen, N.; Honkavaara, E. Real-time and
post-processed georeferencing for hyperpspectral drone remote sensing. Int. Arch. Photogramm. Remote Sens.
Spat. Inf. Sc. 2018, 42, 789–795. [CrossRef]
114. Liu, J.; Chen, P.; Xu, X. Estimating Wheat Coverage Using Multispectral Images Collected by Unmanned
Aerial Vehicles and a New Sensor.
In Proceedings of the 2018 7th International Conference on
Agro-geoinformatics (Agro-geoinformatics), Hangzhou, China, 6–9 August 2018; pp. 1–5.
115. Maurya, A.K.; Singh, D.; Singh, K. Development of Fusion Approach for Estimation of Vegetation Fraction
Cover with Drone and Sentinel-2 Data. In Proceedings of the IGARSS 2018-2018 IEEE International
Geoscience and Remote Sensing Symposium, Valencia, Spain, 22–27 July 2018; pp. 7448–7451.
116. Kumpumäki, T.; Linna, P.; Lipping, T. Crop Lodging Analysis from Uas Orthophoto Mosaic, Sentinel-2
Image and Crop Yield Monitor Data. In Proceedings of the IGARSS 2018-2018 IEEE International Geoscience
and Remote Sensing Symposium, Valencia, Spain, 22–27 July 2018; pp. 7723–7726.
117. Falco, N.; Wainwright, H.; Ulrich, C.; Dafﬂon, B.; Hubbard, S.S.; Williamson, M.; Cothren, J.D.; Ham, R.G.;
McEntire, J.A.; McEntire, M. Remote Sensing to Uav-Based Digital Farmland. In Proceedings of the IGARSS
2018-2018 IEEE International Geoscience and Remote Sensing Symposium, Valencia, Spain, 22–27 July 2018;
pp. 5936–5939.
118. Albornoz, C.; Giraldo, L.F. Trajectory design for efﬁcient crop irrigation with a UAV. In Proceedings of the
2017 IEEE 3rd Colombian Conference on Automatic Control (CCAC), Cartagena, Colombia, 18–20 October
2017; pp. 1–6.
119. Chartzoulakis, K.; Bertaki, M.
Sustainable water management in agriculture under climate change.
Agric. Agric. Sci. Procedia 2015, 4, 88–98. [CrossRef]
120. Saccon, P. Water for agriculture, irrigation management. Appl. Soil Ecol. 2018, 123, 793–796. [CrossRef]
121. Gupta, S.G.; Ghonge, M.M.; Jawandhiya, P. Review of unmanned aircraft system (UAS). Int. J. Adv. Res.
Comput. Eng. Technol. (IJARCET) 2013, 2, 1646–1658. [CrossRef]
122. Cai, G.; Dias, J.; Seneviratne, L. A survey of small-scale unmanned aerial vehicles: Recent advances and
future development trends. Unmanned Syst. 2014, 2, 175–199. [CrossRef]
123. Palossi, D.; Gomez, A.; Draskovic, S.; Keller, K.; Benini, L.; Thiele, L. Self-sustainability in nano unmanned
aerial vehicles: A blimp case study. In Proceedings of the Computing Frontiers Conference, Siena, Italy,
15–17 May 2017; pp. 79–88.
124. Oettershagen, P.; Stastny, T.; Mantel, T.; Melzer, A.; Rudin, K.; Gohl, P.; Agamennoni, G.; Alexis, K.;
Siegwart, R. Long-endurance sensing and mapping using a hand-launchable solar-powered uav. In Field and
Service Robotics; Springer: Cham, Switzerland, 2016.
125. Maltamo, M.; Naesset, E.; Vauhkonen, J. Forestry applications of airborne laser scanning. Concepts Case Stud.
Manag. For. Ecosyst. 2014, 27, 460.
126. Tsouros, D.C.; Smyrlis, P.N.; Tsipouras, M.G.; Tsalikakis, D.G.; Giannakeas, N.; Tzallas, A.T.; Manousou, P.
Automated collagen proportional area extraction in liver biopsy images using a novel classiﬁcation via
clustering algorithm. In Proceedings of the 2017 IEEE 30th International Symposium on Computer-Based
Medical Systems (CBMS), Thessaloniki, Greece, 22–24 June 2017; pp. 30–34.
127. Bonotis, P.A.; Tsouros, D.C.; Smyrlis, P.N.; Tzallas, A.T.; Giannakeas, N.; Evripidis, G.; Tsipouras, M.G.
Automated Assesment of Pain Intensity based on EEG Signal Analysis. In Proceedings of the IEEE 19th
International Conference on BioInformatics and BioEngineering, Athens, Greece, 28–30 October 2019.
128. Cui, D.; Curry, D. Prediction in marketing using the support vector machine. Mark. Sci. 2005, 24, 595–615.
[CrossRef]
129. Tarca, A.L.; Carey, V.J.; Chen, X.W.; Romero, R.; Dr˘aghici, S. Machine learning and its applications to biology.
PLoS Comput. Biol. 2007, 3, e116. [CrossRef] [PubMed]
130. Leica Geosystems. ERDAS Imagine; Leica Geosystems: Atalanta, GA, USA, 2004.

## Page 26

Information 2019, 10, 349
26 of 26
131. Baatz, M.; Benz, U.; Dehghani, S.; Heynen, M.; Holtje, A.; Hofmann, P.; Lingenfelder, I.; Mimler, M.;
Sohlbach, M.; Weber, M. eCognition Professional User Guide 4; ADeﬁniens Imaging: Munich, Germany, 2004.
132. Tetracam, Inc. ADC Users Guide V2.3; Tetracam, Inc.: Chatsworth, CA, USA, 2011.
133. Westoby, M.J.; Brasington, J.; Glasser, N.F.; Hambrey, M.J.; Reynolds, J.
Structure-from-Motion
photogrammetry: A low-cost, effective tool for geoscience applications. Geomorphology 2012, 179, 300–314.
[CrossRef]
134. Liakos, K.; Busato, P.; Moshou, D.; Pearson, S.; Bochtis, D. Machine learning in agriculture: A review. Sensors
2018, 18, 2674. [CrossRef] [PubMed]
135. Hossain, M.D.; Chen, D. Segmentation for Object-Based Image Analysis (OBIA): A review of algorithms
and challenges from remote sensing perspective. ISPRS J. Photogramm. Remote Sens. 2019, 150, 115–134.
[CrossRef]
136. Wiegand, C.; Richardson, A.; Escobar, D.; Gerbermann, A.
Vegetation indices in crop assessments.
Remote Sens. Environ. 1991, 35, 105–119. [CrossRef]
137. Tanriverdi, C. A review of remote sensing and vegetation indices in precision farming. J. Sci. Eng. 2006,
9, 69–76.
138. Bannari, A.; Morin, D.; Bonn, F.; Huete, A. A review of vegetation indices. Remote Sens. Rev. 1995, 13, 95–120.
[CrossRef]
139. Xue, J.; Su, B. Signiﬁcant remote sensing vegetation indices: A review of developments and applications.
J. Sens. 2017, 2017, 1353691. [CrossRef]
140. Eurostat. Agriculture, Forestry and Fishery Statistics; Eurostat: Luxembourg, 2018.
141. European Commission. Commission Delegated Regulation (EU) 2019/945 of 12 March 2019 on unmanned
aircraft systems and on third-country operators of unmanned aircraft systems.
Off.
J. Eur.
Union
2019, L 152, 1–40.
142. European Commission. Commission Implementing Regulation (EU) 2019/947 of 24 May 2019 on the rules
and procedures for the operation of unmanned aircraft. Off. J. Eur. Union 2019, L 152, 45–70.
c⃝2019 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access
article distributed under the terms and conditions of the Creative Commons Attribution
(CC BY) license (http://creativecommons.org/licenses/by/4.0/).
