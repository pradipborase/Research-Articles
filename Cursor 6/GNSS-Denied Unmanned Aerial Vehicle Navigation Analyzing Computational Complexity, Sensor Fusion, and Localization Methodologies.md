# GNSS-Denied Unmanned Aerial Vehicle Navigation Analyzing Computational Complexity, Sensor Fusion, and Localization Methodologies.pdf

## Page 1

Jarraya et al. Satellite Navigation  (2025) 6:9 
https://doi.org/10.1186/s43020-025-00162-z
REVIEW
Open Access
© The Author(s) 2025. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which 
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory 
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this 
licence, visit http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.
Satellite Navigation
https://satellite-navigation.springeropen.com/
Gnss‑denied unmanned aerial vehicle 
navigation: analyzing computational 
complexity, sensor fusion, and localization 
methodologies
Imen Jarraya1*   , Abdulrahman Al‑Batati1   , Muhammad Bilal Kadri1   , Mohamed Abdelkader1   , 
Adel Ammar1   , Wadii Boulila1    and Anis Koubaa1   
Abstract 
Navigation without Global Navigation Satellite Systems (GNSS) poses a significant challenge in aerospace engineer‑
ing, particularly in the environments where satellite signals are obstructed or unavailable. This paper offers an in-
depth review of various methods, sensors, and algorithms for Unmanned Aerial Vehicle (UAV) localization in outdoor 
environments where GNSS signals are unavailable or denied. A key contribution of this study is the establishment 
of a critical classification system that divides GNSS-denied navigation techniques into two primary categories: abso‑
lute and relative localization. This classification enhances the understanding of the strengths and weaknesses of dif‑
ferent strategies in various operational contexts. Vision-based localization is identified as the most effective approach 
in GNSS-denied environments. Nonetheless, it’s clear that no single-sensor-based localization algorithm can fulfill all 
the needs of a comprehensive navigation system in outdoor environments. Therefore, it’s vital to implement a hybrid 
strategy that merges various algorithms and sensors for effective outcomes. This detailed analysis emphasizes 
the challenges and possible solutions for achieving reliable and effective outdoor UAV localization in environments 
where GNSS is unreliable or unavailable. This multi-faceted analysis, highlights the complexities and potential path‑
ways for achieving efficient and dependable outdoor UAV localization in GNSS-denied environments.
Keywords  UAV localization, GNSS-denied navigation, Absolute localization, Relative localization, Visual sensors, 
Non-visual sensors, Terrain aided algorithm, Digital map, Multi-modal sensor fusion framework, Multiple localization 
techniques, Computational complexity
Introduction
Global Navigation Satellite Systems (GNSS), such as 
Global Positioning System (GPS), Global’naya Navigat-
sionnaya Sputnikovaya Sistema (GLONASS), Galileo 
satellite navigation system (Galileo), BeiDou Navigation 
Satellite System (BDS), play a critical role in enhancing 
transportation efficiency and operations in various sec-
tors, especially Unmanned Aerial Vehicles (UAVs) (Li 
et al., 2020). While GNSS plays a key role in the providing 
precise location and navigation information for UAVs, it 
faces significant hurdles due to environmental and tech-
nical issues. These challenges underline the importance 
of developing advanced autonomous navigation solutions 
for UAVs to achieve effective self-localization (Materak, 
2023; Yan et al., 2023; Marut et al., 2023; She et al., 2020).
*Correspondence:
Imen Jarraya
imenjarraya85@gmail.com; ijarraya@psu.edu.sa
1 College of Computer and Information Sciences, Prince Sultan University, 
11586, Riyadh, Saudi Arabia

## Page 2

Page 2 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
Advancements in UAV navigation: a historical overview
UAV navigation evoluted from a simple Radio Detec-
tion and Ranging (RADAR) system and visual guidance 
in the 1940 s, to the current sophisticated technologies. 
The introduction of the H2S RADAR system in 1942 and 
the subsequent advancement of Doppler RADAR post-
World War II represented pivotal moments in UAV oper-
ations, significantly reducing manual control dependence 
and enhancing UAV autonomy (Khawaja et  al., 2024; 
Galati & Galati, 2016; Chandrasekar et al., 2023). In the 
1950 s, Terrain Referenced Navigation (TRN) became a 
key technology, improving UAV navigation by match-
ing measured terrain elevations with existing elevation 
maps. This period marked the transition from analog 
to digital systems. The introduction of Terrain Contour 
Matching (TERCOM) (Baker & Clem, 1977; Golden, 
1980) in the 1970  s represented a significant advance-
ment in navigation precision using Digital Elevation 
Maps (DEM). Innovations, including Sandia Inertial 
Terrain-Aided Navigation (SITAN) (Hollowell, 1990) and 
the Digital Scene Matching Area Correlator (DSMAC) 
(Carr & Sobek, 1980), emerged in later decades. These 
technologies improved accuracy through real-time 
adjustments and better alignment with terrain images, 
marking significant advancements in the development of 
TRN technology (Cottrill & Gu, 2024; Zhao et al., 2024; 
Gambrych et al., 2023). Despite significant progress, the 
full adoption of TRN and similar terrain-aided naviga-
tion techniques was limited by the challenges in sensor 
technology, data storage, signal processing, and comput-
ing power. Until the 1990 s, these challenges often made 
complete UAV navigation impractical, necessitating 
operators to rely on manual visual guidance (Wang et al., 
2024), (Forsyth, 2024). This issue prompted continuous 
efforts in research to overcome these barriers (Ding & 
Cheng, 2022).
The progress made in GNSS and advanced sensor 
technologies during the 1990s marked a significant leap 
forward in autonomous navigation capabilities. Flight 
Management Systems (FMS) (Liden, 1994) and Elec-
tronic Flight Instrument Systems (EFIS) (Ford C. Eng & 
MRAeS, 1985) expanded UAV navigational capabilities, 
enhancing operational efficiency and precision (Strauss 
& Scott, 2024). However, reliance on GNSS satellite net-
works exposes UAVs to risks from interferences such as 
atmospheric conditions, urban canyon effects, and secu-
rity threats like spoofing and jamming, compromising 
operational effectiveness (Pany et al., 2022). This under-
scores the need for robust navigation solutions to ensure 
efficient UAV navigation in complex environments, thus 
improving overall mission success.
Recent progress in UAV navigation is integrat-
ing advanced sensor technologies such as Light 
Detection and Ranging (LiDAR), cameras (Yin et  al., 
2023; Abdelkader et al., 2024, 2025) and Inertial Meas-
urement Units (IMUs), along with sophisticated Simul-
taneous Localization and Mapping (SLAM) algorithms 
(Gao et  al., 2024). These developments have notably 
enhanced the precision and autonomy of UAV flights 
indoors, aiming at dependable navigation without GNSS 
(El-Sheimy & Li, 2021; Guo et al., 2024; Liu et al., 2024). 
The objective is to achieve similar levels of accuracy in 
outdoor environments where GNSS availability is lim-
ited. The adaptation of indoor navigation technologies 
to outdoor applications faces challenges due to weather 
fluctuations and the varied terrains encountered in out-
door UAV navigation. Current research and development 
efforts are focused on improving approaches that ensure 
reliable and consistent UAV navigation in diverse envi-
ronments (Brommer et al., 2024; Cui et al., 2024).
Literature analysis & landscape
This survey comprehensively analysises the UAV localiza-
tion in GNSS-denied environments, covering advance-
ments and future directions. By analyzing 132 recent 
research papers, this work provides an overview of cur-
rent strategies, technologies, and trends. Significant con-
tributions from IEEE Xplore, ScienceDirect, MDPI, ACM 
Digital Library, and arXiv are highlighted, with journal 
articles representing 70% of the literature (Fig. 1.a). The 
remaining sources include conference proceedings (20%) 
and other publications (10%). The survey widely cov-
ers UAV localization studies, from theoretical work to 
practical experiments. Figure 1.b shows that 54.8% of the 
methodologies emphasize real-world experimentation, 
underlining the importance of empirical studies. Simula-
tions account for 42.2% of research, reflecting a balanced 
approach between practical and theoretical development 
in the field.
Contribution
Our comprehensive survey, based on a detailed review of 
research papers, offers a deep understanding of the cur-
rent state and future directions of outdoor UAV localiza-
tion in GNSS-denied environment. The key contributions 
of this review are highlighted below:
•	 We provide a new global categorization/architec-
ture all types of localization techniques. Specifically, 
we categorized localization techniques into Absolute 
Localization (AL), with respect to the global Earth 
coordinate frame, and Relative Localization (RL), 
with respect to a locally defined coordinate frame, as 
illustrated in Fig. 2. This structured approach facili-
tates the analysis of problems and solutions discussed

## Page 3

Page 3 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
in the research literature and ensures a holistic cover-
age of the domain.
•	 Emphasizing the significance of sensor fusion, specif-
ically multi-modal sensor fusion, which incorporates 
techniques like SLAM, Visual Odometry (VO), and 
Visual-Inertial Odometry (VIO) to enhance accuracy 
and reliability.
•	 Multiple Localization Techniques: Our survey 
explores UAV localization methods, including 
Inertial Navigation System (INS), vision, LiDAR, 
and terrain-aided navigation, highlighting TER-
COM, SITAN, and DSMAC navigation models, 
which utilize terrain and visual matching, along 
with algorithms such as the Kalman Filter (KF) and 
Artificial Intelligence (AI)-based approaches to 
enhance accuracy and robustness.
•	 Navigating Implementation Hurdles and Regula-
tory Requirements: We address the multifaceted 
challenges in deploying UAV localization solu-
tions, focusing on system complexity, energy man-
agement system, security, and compliance with 
regulatory standards.
Paper structure
This paper is organized into several sections for a thor-
ough exploration of UAV localization in GNSS-denied 
environments:
70%
20%
10%
a
b
Experiment
results
Simulation
results
54.8%
45.2%
Journal papers
Conference papers
Themes in books/theses/chapters 
Fig. 1  a: Percentage distribution of papers by type. b: Percentage distribution of papers by experiment or simulation methodologies
Outdoor GPS-denied
UAV Localization
Relative
Localization (RL)
Absolute
Localization (AL)
SatNav
Template
and Feature
Matching
Semantic
Mapping and
Recognition
Visual-Inertial
Odometry
(VIO)
Dead
Reackoning,
Filteration, &
Error
Optimization
SLAM, Visual
Odometry &
Optical Flow
Fig. 2  Classification of UAV localization methods

## Page 4

Page 4 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
•	 Sect. 2: Related surveys
•	 Sect.  3: Challenges in UAV localization in GNSS-
denied environments.
•	 Sect.  4: Comprehensive classification of UAVlo-
calization methods within GNSS-denied environ-
ments. The structure of this section is designed as 
follows:
–	 Sect. 4.1: Absolute Localization (AL)
* Sect.  4.1.1: Template and feature matching for 
UAV localization
 * Sect. 4.1.2: Semantic mapping and place recog-
nition
–	 Sect. 4.2: Relative Localization (RL)
 *Sect. 4.2.1: Dead reckoning, filtration, and error 
optimization
 *Sect. 4.2.2: Visual odometry and optical flow
 *Sect. 4.2.3: SLAM
•	 Sect. 5: Discussion and future directions
•	 Sect. 6: Conclusion
Related surveys
In this section, we provide a detailed analysis of 12 sur-
veys published between 2020 and 2024, focusing on 
UAV localization and navigation techniques in GNSS-
denied environments. The papers, outlined in Table  1 
and Table  2, examine key advancements in non-GNSS 
navigation techniques, the sensors utilized, and the chal-
lenges encountered in UAV localization.
Several papers provide comprehensive classifica-
tions of UAV localization methods in GNSS-denied 
environments, systematically organizing them accord-
ing to distinct technological approaches. For instance, 
Ali et  al. (2022) categorize UAV navigation into three 
primary vision-based techniques: correlation-extreme 
approaches, feature detection methods, and deep learn-
ing models. Likewise, Lu et al. (2022) divide vision-based 
localization into two categories: Relative Vision Locali-
zation (RVL) and Absolute Vision Localization (AVL), 
each focusing on different ways of leveraging visual data 
for UAV navigation. Raković et  al. (2021) take a more 
comprehensive approach, classifying UAV navigation 
methods into five categories: Satellite Navigation, INS, 
Terrestrial Navigation, Geomagnetic Navigation, and 
Vision Navigation Systems. Additionally, Couturier and 
Akhloufi (2021) further refine the classification of abso-
lute visual localization in GNSS-denied environments 
into three subcategories: template matching, feature 
points matching, and deep learning.
A key trend emerging from recent surveys is the pivotal 
role of multi-sensor fusion techniques in advancing UAV 
localization in GNSS-denied environments. Yin et  al. 
(2023), Tong et al. (2023) provide comprehensive reviews 
on SLAM systems and collaborative visual position-
ing, respectively, emphasizing the integration of sensors 
such as visual-inertial, LiDAR-inertial, and LiDAR-vis-
ual combinations. This multi-sensor fusion is critical 
for the robust and accurate UAV localization, particu-
larly in large-area group positioning. However, despite 
the potential of these approaches, significant challenges 
remain, including real-time processing, system reliability 
in dynamic environments, and hardware compatibility 
across diverse localization methods.
Vision-based techniques remain pivotal, as demon-
strated by studies such as Ali et al. (2022) and Lu et al. 
(2022). Their studies delve into techniques such as fea-
ture extraction, optical flow enhanced by deep learning, 
and Visual SLAM (VSLAM) for environmental map-
ping. While these methods, particularly those relying on 
algorithms like the Extended Kalman Filter (EKF), have 
shown promise in navigation prediction, their perfor-
mance is highly susceptible to environmental factors such 
as low visibility. This limitation underscores the need for 
the continued integration of AI and deep learning mod-
els, which can significantly enhance the adaptability and 
robustness of vision-based approaches. Furthermore, 
Dissanayaka et al. (2023) stress the importance of Visual 
LiDAR Odometry and Mapping (VLOAM) for improv-
ing navigation reliability, especially in scenarios where 
GNSS signals are degraded. Their research highlights 
that VLOAM ensures compliance with safety standards 
and increases operational robustness, as evidenced by 
numerical simulations.
AI-driven approaches are increasingly prominent in 
UAV navigation, as demonstrated by studies such as Gha-
semieh and Kashef (2024), which explore the applica-
tion of deep learning to VO for enhanced navigation and 
surveillance in GNSS-denied environments. A central 
focus of their work is the development of explainable AI 
models, addressing critical challenges such as the robust-
ness of optical flow and the need for improved process-
ing speeds. These models emphasize transparency and 
interpretability, ensuring their effective integration into 
UAV autonomy systems. Rezwan and Choi (2022) offer a 
comprehensive review of AI technologies in UAV naviga-
tion, categorizing them into mathematical, optimization 
and model-based learning approaches. Their research 
highlights the utility of algorithms such as Convolutional 
Neural Networks (CNNs) for image recognition, Recur-
rent Neural Networks (RNNs) for temporal data analysis,

## Page 5

Page 5 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
Table 1  Comparative analysis of previous UAV navigation survey papers (Part 1)
No. Paper Title, Authors, Year
Technologies
Sensors
Limitations
1
Towards explainable artificial intelligence 
in deep vision-based odometry, Alireza 
Ghasemieh et al., 2024 Ghasemieh and Kashef 
(2024)
Deep Learning, Visual Odometry
Cameras, IMU data, potentially includ‑
ing depth sensors
Based on visual odometry with AI, without men‑
tioning other techniques
2
An overview of simultaneous localization 
and mapping: towards multi-sensor fusion, 
Jun Yin et al., 2024 Yin et al. (2023)
Visual-inertial, LiDAR-inertial, LiDAR-visual, 
LiDAR-visual-inertial, and other multi-sensor 
fusion systems
Various heterogeneous sensors
Does not address alternative methods 
beyond SLAM for UAV localization, such 
as terrain-aided navigation.
3
Review of Navigation Methods for UAV-Based 
Parcel Delivery, Dissanayaka et al. (2023)
Satellite-based navigation, inertial navigation, 
vision-based navigation, and sensor fusion-
based navigation
Camera, Visual, LiDAR, IMU, Multi-sensor
Does not cover all UAV navigation scenarios, 
excludes detailed terrain-aided navigation 
algorithms.
4
Autonomous Underwater Vehicle Navigation: 
A Review, Zhang et al. (2023)
Dead Reckoning, Signal-Based Navigation, 
and Map-Matching Navigation
Sensors: Camera, Sonar, Inertial Sensors, Multi‑
beam Echosounder, Wide-swath bathymetry
Underwater focus, limiting applicability to aerial 
UAV navigation
5
Multi UAV Collaborative Absolute Vision Posi‑
tioning and Navigation: A Survey and Discus‑
sion, Tong et al. (2023)
Collaborative visual positioning, distributed 
collaborative measurement fusion
Visual sensors in UAV clusters
Does not encompass terrain UAV localization 
methods as TERCOM and DSMAC.
6
A Review of Navigation Algorithms 
for Unmanned Aerial Vehicles, Ali et al. (2022)
Outdoor vision-based UAV 
navigation:correlation-extreme approach, key 
point matching, and NN
Visual sensors
Focus on vision-based navigation, exclud‑
ing non-visual methods.
7
Vision-based localization methods under GPS-
denied conditions, Lu et al. (2022)
Relative Vision Localization (RVL), Absolute 
Vision Localization (AVL)
Visual sensors
Excludes non-visual terrain-relative navigation.

## Page 6

Page 6 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
Table 2  Comparative analysis of previous UAV navigation survey papers (Part 2)
No.
Paper Title, Authors, Year
Technologies
Sensors
Limitations
8
Artificial Intelligence Approaches for UAV 
Navigation: Recent Advances and Future Chal‑
lenges, Rezwan and Choi (2022)
Outdoor Navigation: Inertia-based, Signal-
based and Vision-based
Camera, gyroscopes, accelerometers, 
and altimeter
Focus on AI methods for UAV localization, 
excluding others.
9
A Survey on Radio Frequency based Precise 
Localisation Technology for UAV in GPS-denied 
Environment, Yang et al., 2021 Yang and Yang 
(2021)
RF based UAV Localisation Systems (Wi-Fi, 
Bluetooth, Zigbee, RFID, UWB), Classical 
Localisation Mechanisms (RSS, AOA, TOF/TOA, 
TDOA, Fingerprint)
Transmitters & Receivers
Focuses exclusively on RF-based localization 
techniques, overlooking non-RF sensor-based 
methods.
10
State of the Art in Vision-Based Localization 
Techniques for Autonomous Navigation 
Systems, Alkendi et al. (2021)
Odometry techniques: Single-based 
approaches, Hybrid approaches
visual sensors, RADAR odometry, laser-based 
odometry and IMUs
Focuses on VO, Visual-Inertial Odometry (VIO) 
methods; excludes other localization methods.
11
A review on absolute visual localization 
for UAV, Couturier et al., 2021 Couturier 
and Akhloufi (2021)
Absolute visual localization: template match‑
ing, feature points matching, deep learning, 
visual odometry
Cameras, potentially including specialized 
imaging hardware
The survey is dedicated to absolute visual locali‑
zation methods and does not  extensively cover 
other localization technologies.
12
UAV Positioning and Navigation-Review, Rako‑
vic et al., 2020 Raković et al. (2021)
Satellite, Geomagnetic, Inertial (Kalman Filter, 
Markov Model), Terrestrial, Vision Navigation 
Systems
GPS, GLONASS, GALILEO, INS, cameras & 
geomagnetic sensors
It lacks detailed exploration of Artificial Intel‑
ligence (AI) and ML technologies for enhanced 
UAV navigation accuracy and adaptability.
13
Our work: GNSS-Denied Unmanned Aerial 
Vehicle Navigation: Analyzing Compu-
tational Complexity, Sensor Fusion, and 
Localization Methodologies
Absolute localization and Relative localiza-
tion
Visual Sensors & Non-Visual Sensors
Focus on outdoor localization, overlook-
ing indoor environments and additional 
navigation layers such as path planning and 
obstacle avoidance

## Page 7

Page 7 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
Reinforcement Learning (RL) for adaptive decision-mak-
ing, and Genetic Algorithms (GAs) for optimizing route 
planning. Together, these AI-driven techniques are trans-
forming UAV autonomy by providing robust, adaptive 
solutions to complex navigation challenges.
Several surveys specifically address UAV localiza-
tion in GNSS-denied environments, emphasizing the 
importance of TRN methods. Raković et  al. (2021) 
comprehensively review positioning and navigation 
techniques, covering Satellite Navigation, INS, Terres-
trial Navigation, Geomagnetic Navigation, and Vision 
Navigation Systems, with a particular focus on TRN 
methods like TERCOM and DSMAC. These techniques 
have significant potential in improving localization 
accuracy in GNSS-denied outdoor settings. The suc-
cessful application of TRN methods in Autonomous 
Underwater Vehicles (AUVs) (Zhang et  al., 2023) also 
highlights their versatility and precision in environ-
ments where GNSS signals are unavailable. However, 
their widespread adoption in UAV systems is hindered 
by the need for highly detailed environmental maps and 
substantial computational resources. Further research 
is required to adapt and optimize these methods spe-
cifically for UAVs operating in GNSS-denied scenarios, 
addressing the challenges they present.
Non-visual localization methods have also gained 
prominence, Yang and Yang (2021) explored Radio Fre-
quency (RF)-based technologies for UAV localization 
in GNSS-denied environments. Unlike vision-based 
approaches, RF-based localization utilizes signals such 
as Wi-Fi, Bluetooth, Zigbee, RFID, and Ultra-Wide-
Band (UWB) to determine position. These signals are 
paired with classical localization mechanisms, including 
Received Signal Strength (RSS), Angle of Arrival (AOA), 
Time of Flight/Time of Arrival (TOF/TOA), Time Dif-
ference of Arrival (TDOA), and fingerprinting. UWB, 
in particular, has demonstrated high accuracy and low 
latency, making it effective in complex environments 
where visual data may be unreliable. However, chal-
lenges remain, such as the requirement for additional 
anchor nodes and the inherent variability in communi-
cation conditions, which can affect the reliability of RF-
based localization techniques. These surveys examine 
UAV localization strategies in GNSS-denied environ-
ments, focusing on evolving methodologies like vision-
based navigation, AI-driven techniques, and multi-sensor 
fusion. Table 3 highlights key algorithms. However, many 
surveys lack a holistic analysis covering the full range 
of technologies, such as TERCOM, DSMAC, and other 
advanced methods.
Our survey provides a comprehensive review on UAV 
localization in GNSS-deprived environments, that 
addresses the gaps identified in prior research. It intro-
duces absolute and relative localization as essential 
frameworks for understanding the various UAV position-
ing methods. In contrast to previous surveys, which offer 
limited insights into UAV localization without GNSS, 
ours provides an extensive outlook on TRN methods, 
including TERCOM, SITAN, and DSMAC, alongside AI 
and vision-based navigation applications. Moreover, our 
methodology integrates various multi-modal sensors and 
localization strategies, enriching the landscape of UAV 
navigation solutions.
Challenges in UAV localization in GNSS‑denied 
environments
A single GNSS unit is pivotal for UAV navigation, pro-
viding an accuracy of 5-10 ms, which is primarily used 
for mission planning and execution (Zhou et  al., 2024; 
Dang et al., 2023). Nonetheless, its shortcomings in terms 
of accuracy, reliability, availability, integrity, and safety 
underscore the need for alternative navigation strategies 
Table 3  Comparative overview of algorithms for UAV localization in GNSS-denied environments
Category
Algorithms/Methods
Explanation
Probabilistic Localization Algorithms (PLA)
Kalman Filter, Extended Kalman Filter, Particle 
Filter, Adaptive Kalman Filter, Fuzzy Logic Systems, 
Bayesian Estimators
The use of probability theory and optimization.
Feature-Based Localization Algorithms (FBLA)
TERCOM, DSMAC, SLAM, V-SLAM, ORB-SLAM
The use of matching features or landmarks 
in the environment.
Optical Localization Algorithms (OLA)
Optical Flow, VO, SfM, Stereo Vision
The use of visual data from cameras to determine 
how a robot moves relative to its environment.
Artificial Intelligence-Based Localization (AI)
Convolutional Neural Networks (CNNs), Recur‑
rent Neural Networks (RNNs), Long Short-Term 
Memory (LSTM), Multi-Layer Perceptrons (MLP)
The use of machine learning models for localiza‑
tion.
Dead Reckoning Localization (DRL)
Dead Reckoning, INS, Step Counting, Magnetom‑
eter-Based Dead Reckoning, Accelerometer-
Based Dead Reckoning, Gyroscope-Based Dead 
Reckoning
The use of algorithms that estimate position based 
on movement from a known point and assumed 
kinematics.

## Page 8

Page 8 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
in the situations where GNSS signals face compromise 
(Alpern, 2023; Rao et al., 2023). This section outlines five 
principal challenges faced in accurately localizing UAVs: 
signal issues, technical limitations and regulatory factors 
(Deraz et al., 2023; Gao et al., 2023).
Sensor signal issues
In GNSS-denied environments, UAVs depend on a 
variety of visual and non-visual sensor technologies, 
including RADAR, barometers, cameras, and LiDAR, 
to navigate and localize effectively (Zhang et  al., 2023; 
Boroujeni et al., 2024). Both visual and non-visual sen-
sors have distinct strengths and limitations, which can 
significantly impact their performance across varying 
environmental conditions.
•	 Cameras (Visual Odometry): VO systems, like those 
using the Intel RealSense D435 camera, estimate a 
UAV’s position by analyzing sequential images. Cam-
eras are cost-effective and provide high-resolution 
data, making them ideal for detailed mapping and 
navigation. However, their performance is signifi-
cantly impacted by lighting conditions and environ-
mental factors, such as low visibility during night-
time operations or in foggy environments (Tahir 
et al., 2024).
•	 Barometers: Barometers, like the Bosch BMP388, are 
utilized to determine altitude based on atmospheric 
pressure. However, these sensors require frequent 
recalibration due to environmental pressure changes, 
which can lead to inaccuracies. Moreover, dynamic 
weather conditions, such as rapid temperature fluc-
tuations, can cause glitches in barometric readings, 
affecting altitude measurements (Zibaei & Borth, 
2024; Ahmad & Akram, 2024).
•	 Radar altimeters: Radar altimeters, exemplified by 
the Honeywell KRA 405B, provide precise altitude 
measurements by analyzing RADAR signal reflec-
tions from the ground. Radar is particularly reli-
able in various weather conditions and can penetrate 
through obstacles like fog. However, RADAR altim-
eters can be susceptible to physical barriers, such 
as large objects obstructing the signal path, or elec-
tronic interference from other devices, which may 
degrade their accuracy (Gong et al., 2023b).
•	 Acoustic sensors (Sonar): Acoustic sensors, such as 
the Tritech Micron Sonar, are crucial in environ-
ments where visual or RADAR data might be unrelia-
ble, like underwater or densely vegetated areas. Sonar 
systems emit sound waves and analyze the returning 
echoes to determine distance and detect obstacles. 
These sensors are less affected by lighting conditions 
or atmospheric interferences, but they have limited 
range and suffer from signal scattering in complex 
environments (Nagla & Yadav, 2024).
•	 Inertial measurement units (IMUs): IMUs, such as 
the Bosch BMI160, are essential for real-time naviga-
tion by providing data on acceleration and rotational 
rates. They are highly robust and operate well in vari-
ous environmental conditions. However, IMUs suf-
fer from drift, which needs other sensors to correct 
these errors and maintain accurate navigation (Chen 
& Pan, 2024).
•	 Intermittent GNSS: Systems like the u-blox NEO-
M8N GPS module can be used to temporarily regain 
GPS signals in environments where GPS is intermit-
tently available. These systems are particularly useful 
for correcting drift in inertial navigation systems and 
improving overall localization accuracy during brief 
moments when the UAV can reconnect to GNSS 
(Moore et al., 2022).
•	 LiDAR: LiDAR systems, such as the Velodyne VLP-
16, are widely used for creating detailed 3D maps by 
emitting laser pulses and measuring their reflection 
times. While LiDAR is highly accurate in optimal 
conditions, its performance can degrade in adverse 
weather, such as fog or rain, where laser pulses may 
scatter, reducing the sensor’s effectiveness. Addition-
ally, high-power laser applications in LiDAR can suf-
fer from thermal distortions, impacting beam quality 
and overall mapping accuracy (Matyja et al., 2024).
Technical limitations
Navigating UAVs in GNSS-denied environments out-
doors introduces several technical challenges for autono-
mous operations:
•	 Dependency on terrain features: UAV localization 
in GNSS-denied environments often relies on TRN 
methods, such as TERCOM and SITAN. These sys-
tems depend heavily on distinct terrain features. 
However, in the areas with uniform or featureless 
landscapes, or where the terrain database is outdated, 
these methods struggle, limiting their utility in var-
ied or dynamic environments (Zhang et al., 2024; Ge 
et al., 2024; Gao et al., 2023a).
•	 Initial positioning accuracy:  Establishing a UAV’s ini-
tial position without GNSS is a significant challenge. 
TRN systems, including TERCOM and SITAN, 
require accurate initial positioning to effectively 
match the UAV’s observed terrain with pre-stored 
maps. Inaccuracies in this initial step can lead to 
compounded errors in subsequent navigation tasks 
(Wang et al., 2024).

## Page 9

Page 9 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
•	 Inertial measurement unit drift: IMUs provide iner-
tial data for navigation by estimating velocity, orien-
tation, and gravitational forces. Despite their utility, 
IMUs suffer from drift, where small errors accumu-
late over time, leading to increasing errors. This drift 
necessitates frequent calibrations, a task complicated 
without GPS or other external reference points (Elk-
holy et al., 2023; Sivamani & Gudipalli, 2024).
•	 Vision-based navigation system limitations: Vision-
based navigation, which uses cameras and computer 
vision algorithms to interpret environmental fea-
tures, faces challenges in adverse weather, low-light, 
or low-visibility conditions. These limitations can 
degrade the quality of visual data essential for navi-
gation, impacting the UAV’s ability to accurately per-
ceive and interact with its surroundings (Rani et al., 
2024).
•	 Computational and sensor limitations: Navigating 
UAVs in GNSS-denied environments demands sig-
nificant computational resources to analyze the data 
from IMUs, vision-based systems, LiDAR, RADAR 
altimeters, and to implement AI and TRN tech-
niques. The limited processing power and memory 
onboard UAVs pose challenges in utilizing advanced 
navigation strategies such as SLAM, sensor fusion, 
or AI for enhanced effectiveness (Wang et al., 2023; 
Peng et al., 2020).
•	 Malicious threats: Even in GNSS-denied environ-
ments, UAV navigation systems face vulnerabilities 
such as signal jamming (Almomani et al., 2022), elec-
tromagnetic interference, and spoofing of alternative 
navigation sensors (e.g., LiDAR or RF-based systems) 
(Zhang et  al., 2023; Alhafnawi et  al., 2023). These 
threats can significantly impair the performance of 
sensor-based localization systems, compromising 
UAV safety and security. To mitigate these risks, it is 
crucial to employ robust encryption, secure commu-
nication protocols, and advanced anomaly detection 
systems that can defend against sensor spoofing and 
signal interference (Allouch et  al., 2021; Gonzalez-
Jorge et  al., 2024; Eshmawi et  al., 2024; Fang et  al., 
2024; Hou et al., 2023).
Regulatory factors
Navigating regulatory landscapes for UAV localization 
in GNSS-denied areas requires adherence to guidelines 
from authorities like the Federal Aviation Administra-
tion (FAA) in the United States, European Aviation Safety 
Agency (EASA) in the European Union, and Civil Avia-
tion Authorities worldwide. Regulations prioritize relia-
bility, accuracy, integration, and availability of alternative 
navigation systems like LiDAR or RADAR for precise 
UAV localization on maps while addressing operational 
limits and risk mitigation without GNSS. Collaboration 
among developers, regulators, and stakeholders is crucial 
to update regulations in line with technological advance-
ments and operational needs (Gallo & Barrientos, 2022; 
Zenz, 2024).
Classification of UAV localization methods 
in GNSS‑denied environments
The section summarizes UAV localization techniques in 
non-GNSS outdoor environments, offering an overview 
that highlights the methods used for UAV localization in 
these challenging scenarios.
Absolute localization (AL)
Absolute Localization techniques play a vital role in 
determining a UAV’s specific location in relation to the 
global Earth coordinate system. While traditional satel-
lite navigation systems like GPS, GLONASS, or GALI-
LEO are widely utilized, they are beyond the scope of our 
current discussion. Instead, our focus shifts to alternative 
AL methods, with a particular emphasis on TRN, also 
known as TAN or Terrain-Based Navigation (TBN). TRN 
exploits the terrain profile directly below the aircraft 
based on sensor data and matches it with an onboard dig-
ital elevation model. AL methods also include Template 
and Feature Matching (TFM) and Semantic Mapping and 
Recognition (SMR), which rely on advanced sensors and 
technologies to achieve accurate geolocation, especially 
in environments where GNSS signals may be unreliable.
Template and feature matching for UAV localization
Template and Feature Matching methods are crucial for 
UAV localization in GNSS-denied environments, utiliz-
ing sensor data to match predefined templates or fea-
tures for precise navigation. Sophisticated systems like 
TERCOM, SITAN, and DSMAC enhance localization 
Barometer
(Baro)
Navigator
Position
Altitude
Measured
elevation
+ -
Correlation
algorithm
Position correction
Map-indicated
Elevation
Digital map
Radar
altimeter
Fig. 3  TERCOM algorithm integration for UAV localization 
in GNSS-denied environments

## Page 10

Page 10 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
by comparing real-time terrain or scene data with pre-
stored maps, such as DEM, ensuring reliable navigation 
in challenging conditions.
 TERCOM, SITAN and DSMAC The TERCOM sys-
tem is an application of TFM, comparing real-time 
RADAR altimetry data with pre-existing Digital Terrain 
Elevation Data (DTED) or DEM. As illustrated in Fig. 3, 
TERCOM integrates inputs from both RADAR and 
barometric altimeters, correlating the measured eleva-
tion data with digital maps to correct the UAV’s position 
(Raković et  al., 2021). This technique excels in regions 
with distinct terrain features, where the difference 
between the measured and map-indicated elevations 
allows for precise localization. However, TERCOM’s 
effectiveness decreases in flatter regions lacking signifi-
cant terrain contours. To overcome this limitation, the 
SITAN system, an evolved version of TERCOM, intro-
duces real-time updates to terrain data, allowing UAVs 
to dynamically adjust to environmental changes dur-
ing flight. This adaptability makes SITAN highly reli-
able in more complex and variable terrains. In addition, 
SITAN integrates advanced filtering techniques, such as 
the Kalman Filter (KF) and its variants, further enhanc-
ing its precision and robustness in both structured and 
unpredictable environments. Conversely, the DSMAC 
system depicted in Figure 4 improves localization accu-
racy by matching observed terrain with stored visual 
images. This approach offers a distinct advantage in areas 
with minimal topographic variation, as it relies on visual 
terrain characteristics rather than elevation data. While 
TERCOM and SITAN are most effective in regions with 
significant terrain variations, DSMAC excels in environ-
ments where visual cues are more reliable (AbdulMajuid 
et al., 2021; Gupta et al., 2022; Jurevičius et al., 2019).
Recent advances in template and feature matching 
Recent advancements in TFM techniques for UAV locali-
zation have increasingly focused on integrating advanced 
imaging technologies, neural network algorithms, and 
sensor fusion methods, particularly in GPS-denied 
environments. A key trend is the growing use of sensor 
fusion to enhance both the robustness and precision of 
TFM systems. For example, He et al. (2020) introduced 
a hybrid approach combining GNSS and LiDAR-SLAM, 
using GNSS for broad-area coverage and LiDAR-SLAM 
for precise pose estimation, which is especially beneficial 
in GNSS-denied environments. There are also substan-
tial advancements in vision-based systems, particularly 
for large-scale mapping. Mughal et al. (2021) developed 
a system that relies on pre-stored orthomosaic maps 
for UAV localization, while Hosseini et  al. (2020) pro-
posed an automatic localization system that combines 
high-resolution images with elevation models, greatly 
improving real-time localization accuracy in GPS-denied 
environments.
Another important advancement is using deep learn-
ing techniques to enhance feature extraction and match-
ing processes. Kinnari et al. (2023) introduced the LSVL 
method, which integrates high-resolution UAV imagery 
with satellite data to ensure reliable localization, even 
across diverse terrains and under challenging seasonal 
variations. Likewise, Cao et al. (2023) combined template 
matching and CNNs, achieving greater accuracy in GPS-
independent UAV localization. These methods exemplify 
how deep learning is improving the precision and adapt-
ability of UAV navigation in complex environments.
Recent advancements have increasingly focused on 
improving real-time processing capabilities in UAV local-
ization systems. For example, Lee et al. (2020) introduced 
the Advanced Precision Terrain-Aided Navigation (AP-
TAN) system, which integrates INS, GNSS, and TRN 
technologies, along with an interferometric RADAR 
altimeter and LiDAR, to enable reliable real-time naviga-
tion without GPS. This highlights the growing emphasis 
on real-time functionality in TFM systems. Nevertheless, 
challenges in scalability and generalization remain. While 
many TFM methods work well in controlled settings, 
they can struggle in unfamiliar or highly variable environ-
ments. To address this, Lindstrom et al. (2022) utilized 
Synthetic Aperture Radar (SAR) images processed with 
the Range-Doppler Algorithm, enhancing the robustness 
of UAV localization under challenging conditions. Addi-
tionally, Wang and Somani (2020) introduced a triplet-
ranking Siamese deep CNN model for matching aerial 
images with pre-stored DEMs, achieving high accuracy 
in diverse operational scenarios.
Hybrid approaches are also being explored, like dead 
reckoning with terrain image processing to improve 
TERCOM
DSMAC
Fig. 4  TERCOM vs DSMAC

## Page 11

Page 11 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
localization accuracy in new environments. Van  Kirk 
et al. (2022) combined traditional image processing tech-
niques such as Scale-Invariant Feature Transform (SIFT) 
with dead reckoning. Similarly, Kinnari et  al. (2022) 
developed a season-invariant visual localization system 
using Monte-Carlo localization and CNNs to maintain 
the performance of the system in different seasons.
In summary, significant advancements in Template 
and Feature Matching for UAV localization have been 
achieved, with notable progress in areas such as sensor 
fusion, deep learning, and real-time processing. How-
ever, overcoming the challenges of scalability and gener-
alization remains essential for ensuring these systems can 
reliably function in diverse environments and operational 
scenarios. Table 5 provides an overview on the current 
state of the art in this critical area.
Semantic mapping and place recognition
Semantic Mapping and Place Recognition (PR) are 
much interconnected and enhancing global localization 
capabilities in autonomous systems. Semantic Mapping 
focuses on creating a detailed and structured represen-
tation of the environment by processing the data from 
sensors such as cameras and LiDARs. With advanced 
algorithms, particularly those rooted in artificial intel-
ligence, this data is transformed into meaningful labels 
(e.g., “tree,” “building,” “road”) and organized spatially to 
capture the relationships between elements. The primary 
goal of Semantic Mapping is to provide a contextual 
framework that enables systems to interpret their sur-
roundings at a higher level. In contrast, PR is the over-
arching framework that identifies and correlates places 
based on sensory data. PR operationalizes the struc-
tured data provided by Semantic Mapping to recognize 
and localize specific locations. While Semantic Map-
ping builds detailed environmental models, PR applies 
this enriched information to solve practical localization 
challenges. PR methodologies are divided into distinct 
branches: appearance-based PR relying on visual fea-
tures; geometric-based PR using spatial relationships; 
semantic-based PR leveraging semantic labels and spa-
tial relationships; and semantic-structural PR, a hybrid 
approach combining semantic and geometric data. These 
methodologies benefit from the structured and context-
rich data generated through Semantic Mapping.
The significant contributions of various studies in this 
field are comprehensively outlined in Table 6, showcasing 
the advancements in methodologies, applications, and 
innovations within Semantic Mapping and PR.
•	 Bui et al. (2023) introduce an appearance-based PR 
approach for UAV localization, utilizing cross-view 
image comparison where UAV-captured ground 
photos are matched with satellite imagery. This 
method employs a Transformer-based architecture, 
specifically a Vision Transformer, to match ground-
level UAV photos with satellite imagery. It enhances 
the image tokens to significantly improve localization 
accuracy. The use of Recall@1, a metric evaluating 
the system’s ability to identify the correct item as the 
top result, underscores the method’s precision. By 
adopting sophisticated deep learning strategies, the 
approach underscores the potential of visual data for 
precise geo-localization, shifting from conventional 
sensors and reliance on GPS.
•	 Ouyang et  al. (2023) presents a novel semantic-
based PR approach for aircraft positioning in 
GNSS/GPS-denied environments, harnessing a 
semantic vector map-based framework. It utilizes a 
downward-facing monocular camera, an altimeter, 
and a compass in conjunction with open-source 
Vector Maps (VMAPs). The core of the method-
ology involves a coarse-to-fine building vector 
matching technique combined with an improved 
particle filter algorithm, aiming to minimize locali-
zation errors. This approach underscores the signif-
icance of semantic targets in improving localization 
precision. Nevertheless, challenges persist in the 
regions lacking clear semantic features, particularly 
at lower altitudes.
•	 Wang et  al. (2023) proposed a semantic-based PR 
approach through the Weight-Adaptive Multi-Fea-
ture Fusion Network (WAMF-FPI) for UAV image 
localization. This method employs a fusion network 
integrating multiple features to enhance localiza-
tion accuracy, particularly to improve spatial and 
scale information handling. It introduces a unique 
Hanning loss to prioritize central area accuracy. By 
restoring feature maps to the original satellite image 
resolution and employing a novel weighting mecha-
nism, they significantly improved localization accu-
racy. The model demonstrates the improved perfor-
mance on the UL14 dataset, showcasing its potential 
for precise navigation in challenging environments. 
This work harnesses deep learning strategies, offering 
an innovative solution for UAV localization without 
traditional satellite navigation systems. This under-
scores the critical need to address spatial and multi-
scale challenges in UAV localization.
•	 Wang et  al. (2022) propose a geometric-based PR 
approach that integrates geomagnetic data with INS 
to achieve accurate aircraft positioning in GNSS-
denied environments. This method utilizes geomag-
netic field information, aligning it with an a priori 
geomagnetic reference map and applying an INS to 
correct errors over long distances. The system lever-

## Page 12

Page 12 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
ages a geomagnetic triangle matching algorithm inte-
grated with SLAM techniques to enhance localiza-
tion accuracy. This approach addresses the challenges 
in geomagnetic navigation by improving adaptability 
and accuracy in complex magnetic environments.
•	 Allik et  al. (2022) contributed an appearance-based 
PR approach using machine learning with a twin net-
work architecture for scene recognition from NADIR 
imagers. This method demonstrates effectiveness in 
sparse terrains, where traditional localization tech-
niques may struggle due to limited features. By lev-
eraging machine learning for high-altitude systems, 
their approach highlights the potential of visual-
based recognition in GNSS-denied conditions, show-
casing its adaptability and precision in challenging 
environments..
•	 The paper (Liu et al., 2024) introduces the Semantic-
aware Graph Convolutional Network (SeGCN) as 
a Semantic-Structural PR approach for UAV geo-
localization, particularly in GNSS-denied environ-
ments. It addresses the challenge of cross-view geo-
localization by utilizing both semantic information 
(e.g., object categories) and structural relationships 
(e.g., spatial geometry) of objects from UAV and sat-
ellite images. SeGCN uses a graph convolutional net-
work that infers potential semantic features through 
cross-attention of image contexts and explores the 
structural information of objects. This approach has 
demonstrated superior accuracy in localization and 
navigation tasks over traditional methods, confirmed 
by experiments on University-1652 and SUES-200 
benchmarks and real UAV datasets. SeGCN repre-
sents a significant advancement in UAV navigation 
and localization under GNSS-denied conditions by 
effectively matching UAV-captured images to maps 
using semantic and structural insights.
Relative localization (RL)
RL is designed to ascertain a UAV’s location using a 
local coordinate frame, making it highly effective in the 
environments lacking GPS, such as indoor and outdoor 
spaces. RL employs diverse strategies, including Dead 
Reckoning, Filtration & Error Optimization; SLAM; 
Visual Odometry & Optical Flow; and Visual-Inertial 
Odometry, to offer adaptable and precise localization 
solutions where absolute localization is not available.
Dead reckoning, filtration, and error optimization
This strategy calculates the UAV’s current position 
based on previous positions and movements, adjust-
ing for errors and uncertainties with filtering or/and 
optimization techniques. This subsection highlights key 
advancements and collaborative efforts that have signifi-
cantly enhanced the accuracy of UAV navigation in GPS-
denied scenarios (Gallo & Barrientos, 2022; Ye et  al., 
2023; Zheng et al., 2023; Ouyang et al., 2020; AbdulMa-
juid et  al., 2021; El  Sabbagh et  al., 2023; Taghizadeh & 
Safabakhsh, 2023). Some recent works are presented in 
Table 4.
Recent advancements in this field have shown a signifi-
cant progress in minimizing errors and enhancing long-
term positioning accuracy. Gallo and Barrientos (2022) 
developed the algorithms aiming at reducing attitude 
error and position drift in low SWaP UAVs, highlight-
ing how computationally efficient methods can address 
the limitations of lightweight platforms. Similarly, Ye 
et  al. (Xiaoyu et  al., 2024) combined Error State Right-
Invariant Extended Kalman Filtering (ES-RIEKF) with 
LSTM networks, achieving drift-free state estimation in 
fixed-wing UAVs by integrating traditional filtering with 
machine learning for error correction over time.
Multi-UAV collaborations have also contributed to 
advancements in relative localization. Zheng et al. (2023) 
integrated multi-UAV ranging with IMU data to improve 
localization accuracy during low-altitude flights. Their 
method demonstrated that the collaborative data sharing 
between multiple UAVs can effectively reduce localiza-
tion errors. Ouyang et  al. (2020) employed cooperative 
navigation using RSSI measurements and Kalman filters, 
enhancing accuracy in RSS-based localization through 
shared data between UAVs.
Neural network-based approaches have also emerged 
as effective tools for GPS-denied navigation. AbdulMa-
juid et  al. (2021) employed RNNs to estimate position 
and velocity reliably, while El Sabbagh et al. (2023) uti-
lized cascaded neural networks to predict velocity and 
position errors during GPS signal loss. These neural 
models enable learning and adapting over time, providing 
robust navigation solutions in environments where tra-
ditional methods might struggle. Also, Taghizadeh and 
Safabakhsh (2023) introduced an integrated INS/GNSS 
system that incorporates an attention-based hierarchi-
cal LSTM model. Their approach achieved exceptional 
long-term accuracy in position and velocity predictions, 
demonstrating the potential of advanced machine learn-
ing models to address complex navigation challenges in 
the environments with extended GNSS outages.
Visual odometry and optical flow
VO and Optical Flow are essential for UAV localization 
in GNSS-denied environments by estimating displace-
ment and orientation using sequential image data. VO 
focuses on pose estimation without mapping, offer-
ing a lightweight solution for real-time motion track-
ing, while SLAM integrates localization with mapping

## Page 13

Page 13 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
Table 4  Literature summary of dead reckoning, filtration, & error optimization
Authors
Sensors
Algorithms
Implementation
Description of results
IMU RADAR LiDAR Camera Barometer
Magnetometer DRL PLA FBLA OLA AI
Simulation Experiment
Ye et al. Xiaoyu et al. (2024)
✓
✓
✓
✓
✓
✓
✓
✓
- Using the ES-RIEKF and the ES-EKF, 
along with integrating an LSTM 
prediction network into the state 
estimation system, the approach 
enhances accuracy during peri‑
ods when GNSS is unavailable. 
Results demonstrate that ES-RIEKF 
outperforms ES-EKF with faster con‑
vergence, a maximum positioning 
error of 30 meters over a 130-sec‑
ond GNSS denial period, and mini‑
mal three-axis position distur‑
bances.
Zheng et al. (2023)
✓
✓
✓
✓
- Developed a fusion localiza‑
tion method based on multi-UAV 
collaboration and IMU for GNSS-
denied scenarios. This method 
includes UAV coordinate correction, 
pre-processing of ranging data, 
and unscented Kalman filter (UKF) 
application. The method reduced 
positioning error by 21.4% com‑
pared to EKF and performed better 
at low altitudes.
El Sabbagh et al. (2023)
✓
✓
✓
✓
✓
- Cascaded neural networks 
is proposed to estimate velocity 
and position errors during GPS 
signal blockage to handle the time 
dependency and non-linearity 
modeling for different GPS out‑
age periods. Using the proposed 
CNFNN during GPS outages 
enhances the position estimation 
accuracy by 30%, 44%, and 80% 
for 10, 25, and 50 s GPS outages. 
On the other hand, the estimated 
position accuracy of MEMS IMU 
is enhanced by 94%, 98%, and 99%

## Page 14

Page 14 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
Table 4  (continued)
Authors
Sensors
Algorithms
Implementation
Description of results
IMU RADAR LiDAR Camera Barometer
Magnetometer DRL PLA FBLA OLA AI
Simulation Experiment
Taghizadeh and Safabakhsh 
(2023)
✓
✓
✓
✓
✓
- Examined Attention-based Hier‑
archical Long Short-Term Memory 
(AHLSTM) model improvement 
on INS/GNSS integrated navigation 
systems during GNSS outages. The 
results indicate a remarkable 70% 
improvement in long-term position 
and velocity prediction compared 
to similar methods.
Gallo and Barrientos (2022)
✓
✓
✓
✓
✓
✓
- Inertial navigation algorithm 
for GNSS-Denied conditions, evalu‑
ated with Monte Carlo simulations. 
The vertical position estimation 
error is independent of the qual‑
ity of all sensors and depends 
exclusively on ionospheric effects, 
and the pressure offset change 
since the time the GNSS signals 
are lost.
AbdulMajuid et al. (2021)
✓
✓
✓
✓
✓
✓
- RNN used for GPS-denied naviga‑
tion with median MPE of 35m 
in validation, as low as 2.7m 
in some cases. The MPE in 90% 
of the validation flights is bounded 
below 166 meters.
Ouyang et al. (2020)
✓
✓
✓
✓
- Localizing 20 UAVs in a GNSS-
denied environment using a hybrid 
centralized-distributed scheme 
and a multi-sensor fusion algorithm 
(AV-ECKF) that relies on RF relative-
ranging measurements and other 
sensors. AV-ECKF is more accurate 
and stable than EKF, with 85% 
confidence in achieving a 5-meter 
estimation error.

## Page 15

Page 15 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
for simultaneous navigation and map construction. 
To enhance accuracy, Visual-Inertial Odometry (VIO) 
combines camera data with inertial sensors like accel-
erometers and gyroscopes, improving performance in 
GPS-limited settings (Li et  al., 2021; Xu et  al., 2023). 
These techniques collectively enable UAVs to navigate in 
challenging environments effectively. Table  7 highlights 
key developments in VIO and Optical Flow, emphasizing 
their roles in enhancing localization accuracy.
Wang et  al. (2023) developed a stereo visual-inertial 
method for UAV navigation in complex bridge envi-
ronments, significantly improving navigation accuracy 
in diverse conditions. Addressing similar challenges, 
Luo et  al. (2023) introduced a monocular VIO system 
enhanced with point-line fusion and backend adap-
tive optimization, resulting in a 33.8% improvement in 
positioning accuracy. This advancement underscores 
the importance of advanced optimization techniques in 
enhancing navigation reliability in GNSS-denied environ-
ments. Similarly, Gallo and Barrientos (2023) proposed a 
semi-direct visual navigation method that integrates INS 
outputs with visual estimations, effectively mitigating the 
position drift during GNSS outages and improving locali-
zation stability.
Further advancing UAV localization capabilities, Elling-
son et al. (2020) explored the navigation for fixed-wing 
UAS in GPS-denied settings using monocular cameras 
and IMUs. Their system achieved less than 2.5% accumu-
lated error over the distance traveled, emphasizing the 
effectiveness of monocular camera systems in delivering 
accurate pose estimation. Complementing these efforts, 
Lu et  al. (2022) introduced a hybrid mapping strategy 
for micro-aerial vehicles, merging 3D motion plan-
ning with robust localization techniques. This approach 
proved highly effective in dynamic and GPS-denied sce-
narios, highlighting the critical role of hybrid strategies 
in real-time UAV operations. In this context, Allak et al. 
(2020) tested VIO algorithms in Mars-like environments, 
achieving an RMSE of 1.52 ms over a 113-meter trajec-
tory. This demonstrates the adaptability and resilience 
of VIO techniques in environments with minimal navi-
gational cues. Additionally, Kim et al. (2022) developed 
an optical sensor fusion method that combines a Feature 
Point Threshold Filter (FPTF) algorithm with INS data, 
demonstrating superior performance in low-altitude 
UAV navigation. While Benjumea et al. (2021) achieved 
sub-10 cm localization accuracy for high-precision infra-
structure inspection by merging stereo camera data with 
a robotic total station.
Incorporating 
advanced 
machine 
learning 
tech-
niques, Deraz et  al. (2023) integrated optical flow with 
a deep learning-based LSTM model, significantly reduc-
ing velocity errors during GNSS signal loss. This work 
demonstrates the transformative potential of AI in 
enhancing UAV navigation systems, particularly in chal-
lenging scenarios with signal disruptions.
SLAM
Simultaneous Localization and Mapping is essential for 
relative localization in UAVs, enabling them to create 
real-time maps of unknown environments while simul-
taneously determining their position within those maps 
(Zhang et  al., 2022). This dual capability is especially 
critical in regions where reliable maps are unavailable, 
significantly boosting UAV navigation and autonomy in 
GNSS-denied or map-scarce environments.
A key component of SLAM is VO, which estimates 
displacement and orientation by analyzing sequential 
image data, providing the motion estimates necessary 
for SLAM to generate globally consistent trajectories 
and detailed environmental maps. Building on this 
foundation, VIO enhances accuracy and robustness 
by integrating visual data with inertial measurements 
from accelerometers and gyroscopes. This fusion not 
only compensates for motion blur but also improves 
performance in dynamic and GNSS-limited environ-
ments, making it indispensable for UAV operations in 
complex scenarios. Recent advancements in SLAM, 
VO, and VIO have further refined their efficiency and 
adaptability, incorporating innovations such as multi-
sensor fusion, event-based cameras, and deep learning, 
which collectively address the challenges of localiza-
tion and mapping in unstructured and dynamic envi-
ronments. These developments continue to empower 
UAVs to navigate and operate autonomously in diverse 
and demanding settings. Recent advancements in UAV 
SLAM have introduced noteworthy innovations, con-
tributing to the enhanced performance of UAVs in 
various challenging settings, as some recent works are 
presented in Table 8.
Wan et  al. (2022) introduced a terrain-aided SLAM 
algorithm for planetary UAV localization. By integrating 
VO in frame-to-frame motion estimation and geo-refer-
encing UAV images using DEMs, their approach signifi-
cantly reduces localization errors in featureless planetary 
landscapes. The method achieves robust and accurate 
localization with Local Bundle Adjustment (LBA), which 
fuses the relative pose estimates from VO with absolute 
geo-referencing results. This combined approach out-
performs traditional SLAM methods like ORB-SLAM2 
and ORB-SLAM3, highlighting the adaptability of SLAM 
technology for planetary exploration. Such advancements 
demonstrate the potential of extending UAV capabilities 
beyond Earth, making SLAM a critical tool in environ-
ments where the conventional navigation methods are 
ineffective.

## Page 16

Page 16 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
Additionally, LiDAR-based SLAM solutions have also 
gained attention, particularly for their ability to perform 
in low-visibility conditions. Ho et al. (2021) addressed the 
limitations of visual odometry by utilizing 2D LiDAR-
based SLAM for UAV navigation in GPS-denied envi-
ronments. Their study demonstrates how optimizing key 
parameters, such as loop closure thresholds and search 
radii, can significantly enhance SLAM performance. 
With MATLAB simulations, Ho et  al. achieved a 45% 
increase in processing speed, underscoring the potential 
for LiDAR-based systems to provide accurate trajectory 
mapping even in environments where visual cues are 
insufficient.
These advancements highlight SLAM’s pivotal role in 
enhancing UAV autonomy and navigation in GPS-denied 
environments. The integration of advanced sensors like 
LiDAR and AI algorithms (Al-lQubaydhi et  al., 2024) 
enhances SLAM’s effectiveness, driving more precise 
and adaptable processes. For example, Jensen and Budge 
(2023) developed an innovative localization system for 
small UAVs operating in GPS-denied environments. By 
combining camera and LiDAR sensors with Error-State 
Extended Kalman Filtering (ESEKF) and camera-to-
LiDAR sensor fusion, their system achieved an average 
localization error of 3.2 ms, demonstrating the effective-
ness of sensor fusion. These innovations in sensor tech-
nologies and algorithmic optimizations position SLAM 
as a cornerstone for reliable UAV operations, particularly 
in the most challenging settings (Chiang et al., 2023).
A major development is the integration of SLAM with 
computer vision algorithms, as demonstrated by Ngo 
et al. (2022), who developed a UAV platform for autono-
mous search and rescue missions. Their approach effec-
tively merges real-time localization with environmental 
mapping, showcasing the practical application of SLAM 
in complex and dynamic settings. This integration not 
only proves the feasibility of SLAM in high-stakes opera-
tions but also emphasizes its growing importance in ena-
bling UAVs to operate without reliance on GNSS.
Discussion and future direction
Discussion
Analysing 132 research papers, we explored the integra-
tion of diverse sensors and algorithms to improve UAV 
localization in GPS-denied environments. These efforts 
focus on terrain or map feature extraction, advanced 
scene recognition techniques, multi-sensor fusion, and 
implementing sophisticated localization methods.
Absolute localization methods, such as TERCOM, 
SITAN, and DSMAC, rely on pre-mapped terrain data 
like DEMs and external sensors, including RADAR, 
LiDAR, and barometers. These systems use this data to 
accurately match the UAV’s position with distinct terrain 
features, ensuring precise navigation even in GPS-denied 
environments. For instance, TERCOM matches baro-
metric and RADAR readings to terrain profiles but may 
lack the precision needed for more advanced tasks. To 
overcome these limitations, SITAN was developed, inte-
grating advanced filtering techniques such as the EKF 
and UKF to enhance accuracy. Additionally, an enhanced 
DSMAC takes precision by leveraging high-resolution 
satellite imagery and detailed terrain maps to match 
specific ground features more effectively. Despite their 
strengths, AL methods struggle in environments with 
sparse or uniform features (e.g., deserts or open water), 
where few distinctive features are available to match pre-
mapped data (see Sect. 4.1). In contrast, RL methods rely 
on real-time data from onboard sensors, such as cameras 
for visual odometry or LiDAR for SLAM, excelling at 
lower altitudes where they can capture detailed environ-
mental features. Techniques like SLAM, which integrate 
visual-inertial odometry and optical flow, enable the 
UAV to map unfamiliar environments in real-time while 
simultaneously determining its position. RL methods are 
highly adaptable, performing effectively in dynamic envi-
ronments where pre-mapped data may be unavailable or 
outdated (see Sect. 4.2).
A key factor in the performance of AL and RL tech-
niques lies in the types of features each method utilizes. 
AL methods predominantly rely on elevation-based fea-
tures, detected by sensors such as RADAR, barometers, 
or LiDAR, which are particularly effective for captur-
ing large-scale terrain changes. In contrast, RL meth-
ods focus on visual features, captured cameras or other 
imaging sensors, to detect finer and localized details in 
the UAV’s immediate surroundings. For instance, in fea-
ture-sparse environments at low altitudes, AL methods 
can improve localization accuracy by increasing altitude 
to detect more prominent terrain features. Conversely, 
in urban settings with high visual complexity, RL meth-
ods prove more effective by utilizing detailed visual cues 
such as building edges, textures, and obstacles for precise 
navigation.
The performance of both AL and RL methods is highly 
dependent on environmental conditions and the avail-
ability of sensor data. A hybrid approach that combines 
both AL and RL can offer a more reliable and robust 
localization solution, allowing UAVs to adapt to diverse 
environmental challenges and ensuring consistent per-
formance in various conditions. This hybrid model 
ensures that UAVs can capitalize on both terrain-based 
and real-time data-driven localization techniques, which 
enhances overall navigation accuracy, particularly in 
GPS-denied environments. Integrating AL and RL tech-
niques in a sensor fusion framework is an advanced

## Page 17

Page 17 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
solution to UAV navigation challenges in GPS-denied 
environments (see Table 9).
For both absolute and relative navigation, the key chal-
lenges in real-time processing lie in optimizing algo-
rithmic efficiency and harnessing high-performance 
computational resources to ensure reliable operation. 
This includes effective sensor integration, low-latency 
processing, and maintaining robust performance in 
dynamic environments. The main implementation obsta-
cles are summarized below:
•	 Computational complexity Integrating multiple sen-
sors such as LiDAR, RADAR, cameras, and IMUs 
presents computational challenges due to the need to 
process large volumes of heterogeneous data in real-
time. The sensor type directly influences the process-
ing load; for instance, Visual SLAM systems, which 
use camera data, can operate at high frequencies (e.g., 
250  Hz) when leveraging GPU-enabled hardware. 
Meanwhile, LiDAR typically produces larger raw data 
streams due to denser point clouds. However, mod-
ern LiDAR-based odometry and SLAM solutions 
(e.g. LIO-SAM Shan et al. (2020), Fast-LIO2 Xu et al. 
(2021)) efficiently use geometric feature extraction, 
sub-sampling, or scan matching to run in real-time-
often avoiding the need for computationally heavy 
Bundle Adjustment. Consequently, although LiDAR 
data volume can be high, well-optimized pipelines 
can achieve performance on par with, or even sur-
pass, purely visual methods. Managing these diverse 
data streams efficiently (whether visual or LiDAR) 
requires advanced algorithms-such as deep learning 
models, Kalman filters, or other recursive methods-
to achieve reliable multi-modal sensor fusion in real-
time applications. Commonly used in research, algo-
rithms such as the EKF, UKF, and RLS offer varying 
trade-offs between accuracy and computational com-
plexity:
–	 Extended kalman filter offers a balance between 
accuracy and computational efficiency, making it a 
widely-used choice for many real-time applications. 
However, the EKF can introduce errors in highly 
non-linear environments, as highlighted in stud-
ies such as Refs. Ye et al. (2023) and Ouyang et al. 
(2020). This limitation often results in divergence 
in system state estimation, especially when initial 
conditions are poorly defined or system dynamics 
exhibit significant non-linearity.
–	 Unscented kalman filter improves accuracy by 
avoiding the need for linearization, unlike the EKF. 
For example, a study by Zheng et al. (2023) dem-
onstrated that in a multi-UAV collaboration using 
fusion localization in partial GNSS-denied sce-
narios, the UKF significantly outperformed the 
EKF. This approach utilized sensors like IMUs and 
distance measurement modules, including time-
of-flight (TOF) and received signal strength indi-
cator (RSSI), for UAV localization. The simulation 
results showed a 21.4% reduction in positioning 
error, demonstrating clear improvements in both 
accuracy and robustness. However, the UKF typi-
cally increases computational complexity due to the 
generation of sigma points required for non-linear 
transformations.
–	 Recursive least squares (RLS) is highly effective in 
environments with dynamically changing param-
eters due to its ability to continuously update its 
estimates. This adaptability makes it particularly 
valuable for real-time applications, though it 
comes with higher computational demands. For 
example, in the study by Benjumea et al. (2021), 
RLS was used for UAV sensor fusion, significantly 
improving real-time adaptability and reducing 
sensitivity to sensor noise. In GPS-denied envi-
ronments, the integration of RLS enabled the 
UAV to maintain a positional error of less than 
2  ms over 100  s of GPS signal loss, achieving a 
15-20% improvement in localization accuracy 
compared to standard Kalman Filters by better 
adapting to rapidly changing flight dynamics.
•	 Real-time processing capabilities Real-time process-
ing is critical for UAV operations in environments 
where GPS is unavailable. It ensures the timely and 
accurate handling of sensor data, requiring the inte-
gration of optimized algorithms with high-perfor-
mance hardware. The following factors are essential 
for achieving real-time performance:
–	 Hardware acceleration Utilizing specialized hard-
ware, such as Graphics Processing Units (GPUs) 
and Field Programmable Gate Arrays (FPGAs), 
can significantly reduce processing latency. GPUs 
excel at parallel processing tasks, making them 
ideal for managing the large datasets produced 
by sensors like LiDAR and cameras. For instance, 
the VINS-MONO (visual inertial SLAM using 
monocular camera ad an IMU) algorithm has a 
GPU accelerated version (pjrambo, 2025) that can 
run on NVIDIA Jetosn edge devices to achieve a 
real-time performance. Another stere-based visual 
inertial SLAM is the Isaac ROS Visual SLAM soft-
ware package developed by NVIDIA (Corporation, 
2025), which is GPU-accelerated and can provide 
pose estimation at frequency up to 250 Hz.

## Page 18

Page 18 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
–	 Algorithm optimization Customizing sensor fusion 
algorithms for specific hardware architectures can 
significantly boost processing speed. Techniques 
such as down sampling sensor data, using approxi-
mation methods, and optimizing matrix opera-
tions are essential for maintaining real-time perfor-
mance. For example, the ES-RIEKF framework (Ye 
et  al., 2023) achieves attitude convergence in less 
than 25  s during flight, outperforming traditional 
EKF by reducing oscillations. Similarly, integrat-
ing enhanced visual odometry with LSTM-based 
drift correction (Deraz et al., 2023) reduces forward 
velocity error by 63.01% after 30 s and 54.33% after 
113 s of GNSS signal loss, demonstrating the direct 
impact of algorithm optimization on UAV localiza-
tion in GPS-denied scenarios
–	 Latency management Ensuring low-latency com-
munication between sensors and processing units 
is crucial for real-time operations. High-bandwidth 
communication protocols and the strategic place-
ment of processing units to minimize data trans-
mission distances are essential. For example, in the 
study (Deraz et al., 2023), a micro-FMCW RADAR 
attached to a 3DR Solo quadcopter achieves real-
time RADAR target detection in just 1.3 ms, allow-
ing near-instantaneous sensor feedback. Low 
latency is especially vital for maintaining precise 
localization and rapid response to dynamic con-
ditions, which is crucial for successful missions in 
GPS-denied environments and other challenging 
scenarios.
Experimental methods
Simulation and quasi-experimental strategies for UAV 
localization in GPS-denied environments are well-docu-
mented, as highlighted in previous sections and particu-
larly in Tables 5 to 8. However, despite the existence of 
diverse approaches, practical implementations remain 
limited, and their real-world applications and effective-
ness are still underexplored, particularly concerning 
execution time, computational delays, and other specific 
details. Herein, we present relevant experimental imple-
mentations for UAV localization in environments lacking 
GPS support. 
1.	 Experiment at Hong Kong University of Science and 
Technology (HKUST) using VINS-Mono (Qin et  al., 
2018):
•	Description: The experiment conducted at the 
HKUST utilized the VINS-Mono, a Visual-Iner-
tial Navigation System combining monocular 
camera input with inertial measurement data. 
VINS-Mono, and its successor VINS-Fusion, are 
typically suited for indoor environments, where 
they excel in scenarios with rich visual features 
and controlled conditions. However, this experi-
ment aimed to assess the system’s performance 
in a large-scale outdoor environment. Data col-
lection for this outdoor test conducted at a rate 
of 20 Hz for visual data and 200 Hz for IMU 
measurements, covering a path length of 2.5 km 
under normal walking conditions. In another 
larger-scale test, data was collected at a rate of 
25 Hz for visual data and 200 Hz for IMU meas-
urements, covering a path length of 5.62 km over 
1 h and 34 min. The results were notable, show-
ing nearly zero drift in the entire path, with the 
estimated trajectory closely aligning with Google 
Maps. This suggests that VINS-Mono can main-
tain accurate localization over extended peri-
ods and distances, even in challenging outdoor 
scenarios, despite not being primarily designed 
for them. Notably, VINS-Mono has been suc-
ceeded by VINS-Fusion, a more flexible system 
that builds on its predecessor’s capabilities for 
enhanced applicability across various environ-
ments.
•	Strengths: VINS-Mono is highly effective in envi-
ronments with rich visual features, providing 
accurate pose estimation with minimal drift over 
extended distances. It excels in urban or well-lit 
environments where visual data is reliable.
•	Limitations: The reliance on visual data makes 
VINS-Mono less effective in environments with 
poor lighting, low visibility, or sparse visual fea-
tures, such as forests, deserts, or during night 
operations. It may also struggle in dynamic light-
ing conditions.
2.	 Development and testing of the PO-MSCKF algorithm 
(Xueyu et al., 2024):
•	Description: Xueyu et  al. introduced and rigor-
ously tested the Pose-Only Multi State Con-
strained Kalman Filter (PO-MSCKF) algorithm, 
which enhances traditional VIO systems. The key 
innovation of PO-MSCKF is its focus on elimi-
nating the need for 3D feature reconstruction by 
using the Pose-Only (PO) theory. This approach 
simplifies the algorithm, reducing computational 
costs while maintaining model consistency. Com-
prehensive experiments were conducted in vari-
ous environments, including indoor, outdoor, and

## Page 19

Page 19 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
Table 5  Literature summary of absolute localization - template and feature matching
Authors
Sensors
Algorithms
Implementation
Description of results
IMU Radar LiDAR Camera Barometer Magnetometer DRL PLA FBLA OLA AI
Simulation Experiment
He et al. (2020)
✓
✓
✓
✓
✓
✓
Experimental results demonstrate high accu‑
racy, with average position errors around 0.03 
meters and rotational errors of 0.0120 rad 
for yaw and 0.0445 rad for pitch, indicating 
effective drift error correction and reliable 
pose estimation without high-cost inertial 
devices.
Kinnari et al. (2023)
✓
✓
✓
✓
✓
✓
✓
Large-scale map matching method together 
with a point mass filter, achieving 12.6-18.7 m 
error with a map size of 100 km2 in real-time 
operation.
Cao et al. (2023)
✓
✓
✓
✓
✓
Template matching with CNN for UAV visual 
localization, shows enhanced feature extrac‑
tion and accuracy.
Zhang et al. (2022)
✓
✓
✓
✓
✓
✓
 DNN to extract scene features for position 
matching and optical flow estimation. This 
method can correct the position drift of IMU
Van Kirk et al. (2022)
✓
✓
✓
✓
✓
✓
 Proposed a system combining dead reckon‑
ing and terrain imaging for UAV naviga‑
tion in GPS-denied environments. Utilizes 
image processing for location estimation 
and ground speed calculation. Validated 
through both simulations and physical tests.
Lindstrom et al. (2022)
✓
✓
✓
✓
✓
 SAR-image-based method for matching; 
errors estimated within 3 meters of truth 
in both simulated and real data.
Kinnari et al. (2022)
✓
✓
✓
✓
✓
✓
✓
 Season-invariant visual localization in GNSS-
denied environments. Achieved mean 
localization errors of 26.5m, 29.1m, and 30.6m 
in real UAV data after approximately 2 km 
of travel.
White et al. (2021)
✓
✓
✓
✓
✓
 Utilized SAR images and CNNs for GPS-denied 
navigation. Tested on both simulated and real 
data, showing effective navigational error 
estimation in UAVs.
Mughal et al. (2021)
✓
✓
✓
✓
✓
 Developed a deep learning-based image 
matching system for UAV localization. 
Achieved matching accuracy of 91.04% 
and GPS localization error with an average 
of 3.708 m2 and a maximum of 33.164 m2.

## Page 20

Page 20 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
Table 5  (continued)
Authors
Sensors
Algorithms
Implementation
Description of results
IMU Radar LiDAR Camera Barometer Magnetometer DRL PLA FBLA OLA AI
Simulation Experiment
Hosseini et al. (2020)
✓
✓
✓
✓
- Based on GIS data, elevation models, 
and georeferenced images for UAV localiza‑
tion, the accuracy within a 5 m horizontal 
difference using aerial and satellite reference 
data.
Lee et al. (2020)
✓
✓
✓
✓
✓
✓
✓
✓
✓
 The AP-TAN method attained a navigation 
accuracy of around 3.1 m CEP at 1.5 km alti‑
tude and 5.9 m CEP at 5.1 km altitude.
Wang and Somani (2020)
✓
✓
✓
✓
 High accuracy in Aerial-DEM matching using 
a triplet-ranking Siamese deep CNN model 
for real-time UAS navigation in GPS-denied 
environments. Aerial-DEM matching accuracy 
as high as 0.96078m.

## Page 21

Page 21 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
Table 6  Literature summary of absolute localization - semantic mapping and recognition
Authors
Sensors
Algorithms
Implementation
Description of results
IMU Radar LiDAR Camera Barometer Magnetometer DRL PLA FBLA OLA AI
Simulation Experiment
Bui et al. (2023)
✓
✓
✓
✓
✓
For UAV to Satellite, it reached an 87.33% Recall@1 
and 89.28% Average Precision, while Satellite 
to UAV tasks saw 90.16% Recall@1 and 86.93% AP. 
The large-scale Vision Transformer (ViT-L) version 
of the model achieved the highest accuracy, 
with an 88.18% Recall@1 and 89.99% AP. Moreover, 
the model’s inference time, when using a smaller 
ViT (ViT-S) backbone, was only 0.89 times that of 
a comparative ResNet-50-based model, showcas‑
ing both efficiency and performance.
Ouyang et al. (2023)
✓
✓
✓
✓
The Semantic Vector Map excels in aircraft geolo‑
cation, maintaining sub-10m error in an 11,025 
km2 map. However, it struggles without semantic 
targets in large areas or at low altitudes, causing 
localization challenges.
Wang et al. (2023)
✓
✓
✓
✓
✓
Combining object tracking and semantic segmen‑
tation for UAV image localization on satellite maps, 
employing the WAMF-FPI for UAV localization. 
Results in remarkable accuracy at 3m, 5m, and 10m 
scales (12.50%, 26.99%, and 52.63%, respectively). 
However, data coverage limits persist, making it 
challenging to achieve the required real-world 
accuracy.
Wang et al. (2022)
✓
✓
✓
✓
✓
Developed a geomagnetic/INS integrated naviga‑
tion method. Effectively corrected the output errors 
of the INS and guided navigation accurately.
Allik et al. (2022)
✓
✓
✓
✓
Machine learning approach with a twin net‑
work architecture to enable scene recognition 
from a NADIR imager, showing effectiveness 
in simulations for high-flying systems over sparse 
terrain.
Liu et al. (2024)
✓
✓
✓
✓
✓
For the SeGCN approach on the University-1652 
dataset, the results demonstrated a Recall@1 (R@1) 
of 89.18% and an Average Precision (AP) of 90.89% 
for the Drone→Satellite task. For the Satellite→
Drone task, the results showed an R@1 of 94.29% 
and an AP of 89.65%. These outcomes illustrate 
SeGCN’s effectiveness, showcasing its superior per‑
formance over state-of-the-art methods in cross-
view geo-localization tasks.

## Page 22

Page 22 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
Table 7  Summarizing literature on RL: visual-inertial odometry & optical flow
Authors
Sensors
Algorithms
Implementation
Description of results
IMU RADAR LiDAR Camera Barometer Magnetometer DRL PLA FBLA OLA AI
Simulation Experiment
Wang et al. (2023)
✓
✓
✓
✓
✓
✓
✓
Developed a stereo visual-inertial method 
(FMC-SVIL) with RMSEs of 0.416m (sunny) 
and 0.340m (cloudy), utilizing AprilTag 
detection and pose graph optimization 
for precise UAV navigation.
Luo et al. (2023)
✓
✓
✓
✓
✓
✓
✓
Proposed using VINS-MONO, leading 
to a 32.3% improvement on the EuRoc 
dataset over PL-VINS, and in challenging 
real-world scenarios with variable illumina‑
tion, weak texture, and complex environ‑
ments, achieving a 33.8% enhancement.
Gallo and Barrientos (2023) ✓
✓
✓
✓
✓
✓
A Semi-Direct Visual Odometry (SVO)-
based Inertially Assisted Visual Navigation 
System (IA-VNS). Results for Scenario 1: 
mean (max) 0.521 (1.321) degrees, std 
0.151 degrees.
Lu et al. (2022)
✓
✓
✓
✓
✓
✓
✓
✓
Hybrid mapping strategy that integrates 
a matching algorithm with 3D motion 
planning. The final drift is around 13% 
of the total traveled distance.
Allak et al. (2020)
✓
✓
✓
✓
✓
✓
✓
✓
Conducting AVI-NAV experiment 
for UAV navigation in Mars-like environ‑
ments. Achieves robust pose estimation 
with an RMSE of 1.52 m on a 113 m trajec‑
tory using vision-based techniques.
Ellingson et al. (2020)
✓
✓
✓
✓
✓
✓
✓
Monocular camera and IMU-based 
odometry-like estimator for fixed-wing UAS 
navigation in GPS-denied environments. 
Total accumulated error is demonstrated 
as less than 1% of the distance traveled. 
After initialization errors were removed, 
the filter was accurate, ultimately accu‑
mulating an error of approximately 2.5% 
of the distance traveled.
Deraz et al. (2023)
✓
✓
✓
✓
✓
✓
✓
✓
Forward velocity of the vehicle is calcu‑
lated using both RADAR height esti‑
mate and enhanced visual odometry. 
VO is implemented using optical flow 
and deep learning-based techniques. can 
improve the average forward and lateral 
velocities errors for the flight to 63.01% 
in 30sec, 62.26% in 60 sec, 58.76% in 90 sec 
and 54.33% in 113 sec during the GNSS 
signal outage.

## Page 23

Page 23 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
Table 7  (continued)
Authors
Sensors
Algorithms
Implementation
Description of results
IMU RADAR LiDAR Camera Barometer Magnetometer DRL PLA FBLA OLA AI
Simulation Experiment
Kim et al. (2022)
✓
✓
✓
✓
✓
✓
Modified FPTF algorithm for enhanced 
optical-flow-based UAV navigation. Fuses 
data from INS and optical flow sensor. 
Evaluated through Gazebo simulations 
and experimental flight tests in varying 
flight conditions.
Benjumea et al. (2021)
✓
✓
✓
✓
✓
Employed EKF and Extended Recursive 
Least Squares (ERLS) for UAV positional 
accuracy. ERLS aligned 3D camera data 
with a global reference from a robotic 
total station, and EKF integrated this data 
for precise UAV state estimation, achieving 
an error below 10 cm against total station 
measurements.

## Page 24

Page 24 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
Table 8  Literature summary of relative visual localization - SLAM
Authors
Sensors
Algorithms
Implementation
Description of results
IMU RADAR LiDAR Camera Barometer Magnetometer DRL PLA FBLA OLA AI
Simulation Experiment
Wan et al. (2022)
✓
✓
✓
✓
✓
✓
- Proposed a terrain-aided SLAM algorithm for plan‑
etary UAV navigation in GPS-denied environments. 
Achieved an average localization error of 0.45 m 
in simulations over a 33.8 km flight, outperforming 
ORB-SLAM2 and ORB-SLAM3. Processing speed of 12 
Hz ensures real-time performance.
 Ngo et al. (2022) ✓
✓
✓
✓
✓
✓
- Development of UAVs for autonomous search 
and rescue in GPS-denied environments. Utilized 
SLAM for mapping and computer vision for victim 
detection. Demonstrated in simulations and flight 
tests.
Ho et al. (2021)
✓
✓
✓
✓
- Utilized LiDAR-based SLAM for 2-D UAV navigation 
in GPS-denied environment. Achieved up to 45% 
increase in processing speed and accurate trajectory 
mapping in MATLAB simulation.

## Page 25

Page 25 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
large-depth scenarios, using multiple datasets 
such as EuRoc, Kitti, and NUDT.
–	 EuRoc datasets (Burri et al., 2016): These data-
sets are commonly used in the research com-
munity for testing visual-inertial odometry algo-
rithms. The EuRoc datasets were collected using 
a micro-aerial vehicle (MAV) and include 20 Hz 
stereo images, 200 Hz IMU data, and ground 
truth data.
–	 Kitti datasets (Rosten et  al., 2010): The Kitti 
datasets were collected using a land vehicle 
equipped with sensors, including cameras and 
IMUs. The datasets include 10 Hz images, 200 
Hz IMU data, and ground truth, making them 
suitable for testing algorithms in urban and 
highway environments.
–	 NUDT datasets: The NUDT datasets consist 
of sequences from both UAV and land vehicle 
experiments. The UAV data were collected at 
an altitude of about 180  ms, covering a dis-
tance of 2.8 km, while the land vehicle data 
covered a distance of 4.5 km. These datasets 
provide challenging sequences for visual-iner-
tial odometry testing, especially in large-depth 
environments.
	
 The results of the PO-MSCKF algorithm dem-
onstrated exceptional performance in various 
challenging scenarios. In the EuRoc dataset, 
particularly in the difficult MH05 sequence of 
the Machine Hall environment, PO-MSCKF 
achieved an RMSE of 0.28  ms, highlighting 
its robustness in complex indoor settings. In 
the Kitti datasets, which consist of urban and 
highway environments with varying depths, 
the 
algorithm 
consistently 
outperformed 
other state-of-the-art methods, achieving 
RMSE values ranging from 9.17 ms in Kitti08 
to 14.01 ms in Kitti10. The algorithm’s robust-
ness was further validated in the NUDT data-
set, which included experiments in large-depth 
environments. Here, PO-MSCKF achieved an 
RMSE of 10.69 ms in the land vehicle experi-
ment and 25.47  ms in the UAV experiment, 
proving its ability to maintain high accuracy 
even in conditions where traditional methods 
struggled, particularly in altitude estimation.
•	Strengths: PO-MSCKF is particularly effec-
tive in environments with varied depth, such as 
those found in the Kitti datasets. The algorithm 
addresses some of the common limitations of 
standard VIO systems by avoiding the need for 
3D feature reconstruction, thus improving accu-
racy in pose estimation and enhancing computa-
tional efficiency.
Table 9  Pros and cons of localization techniques
Localization type
Technique
Pros
Cons
AL
Template and feature matching
Achieves high precision in environ‑
ments with distinct terrains, utilizing 
detailed feature comparison.
Loses effectiveness in uniform landscapes 
with a lack of distinct features.
Semantic mapping and recognition
Offers in-depth insights 
into the environment, utilizing 
semantic information to enhance 
accuracy and awareness.
Demands extensive computational resources, 
posing challenges for real-time application.
RL
Dead reckoning, filtration, & error 
optimization
Provides reliable continuous track‑
ing crucial for GPS-independent 
navigation through IMU data inte‑
gration and error correction.
Tends to accumulate errors over time, requiring 
periodic recalibration or adjustments.
SLAM
Enables mapping and localization 
in unknown environments, offering 
a comprehensive solution for explo‑
ration in GNSS-denied areas.
Requires sophisticated algorithms and extensive 
computational resources, making implementa‑
tion challenging on constrained UAVs.
Visual odometry & optical flow
Performs effectively in dynamic 
environments by providing accu‑
rate motion estimation through vis‑
ual data analysis.
Suffers from degraded performance under poor 
lighting, rapid movements, or in featureless 
environments.
Visual-inertial odometry
Enhances robustness of localization 
by combining visual data with iner‑
tial measurements, improving 
accuracy and stability.
Necessitates complex integration and precise 
calibration, presenting significant technical 
challenges.

## Page 26

Page 26 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
•	Limitations: While PO-MSCKF excels in struc-
tured environments, it may face challenges in 
unstructured or visually featureless environ-
ments. Additionally, the algorithm might strug-
gle in dynamic or rapidly changing environ-
ments, where the traditional limitations of VIO 
systems could still persist.
3.	 Steerable-laser terrain-referenced navigation system 
(Carroll & Canciani, 2021):
•	Description: The study by Carroll & Canciani 
(2021) investigated a steerable-laser TRN system 
designed specifically for GPS-denied environ-
ments. Mounted on an aircraft, the system utilized 
a steerable laser altimeter capable of measuring 
terrain profiles at various slant angles, represent-
ing a significant advancement over traditional 
nadir-only systems, which capture data directly 
beneath the aircraft in a vertical orientation. The 
experiment was conducted under two distinct 
flight scenarios: a flat terrain profile over Califor-
nia and a mountainous terrain profile. The steer-
able-laser TRN system demonstrated substantial 
improvements in navigation accuracy, particularly 
in complex terrains. In flat terrain, optimal laser 
steering led to a remarkable reduction in RMSE 
values, decreasing from 29.1 ms (East) and 30.7 ms 
(North) to 10.8 ms (East) and 7.9 ms (North). In 
mountainous terrain, the enhancements were 
more significant, with RMSE values reduced to 
1.2  ms (East) and 1.0  ms (North). These results 
indicate that the system can enhance navigation 
accuracy by up to 20 times compared to tradi-
tional nadir-only systems.
•	Strengths: The system is particularly effective in 
complex terrains, such as mountainous regions, 
where traditional TRN systems might struggle. 
By optimizing the laser steering, the system sig-
nificantly enhances navigation accuracy, reducing 
RMSE values dramatically in such environments. 
Moreover, the steerable-laser TRN system does 
not depend on external signals, making it highly 
reliable in GPS-denied or contested environments. 
The ability to adjust the laser’s angle to target 
specific terrain features optimizes the amount of 
navigational information collected, significantly 
improving overall system performance.
•	Limitations: While the system’s performance in 
complex terrains is impressive, its complexity and 
potential cost may limit its application to smaller 
UAVs or budget-conscious projects. Additionally, 
the requirement for specialized hardware and pre-
cise calibration can increase operational overhead. 
Furthermore, the system’s reliance on laser tech-
nology may pose challenges in adverse weather 
conditions, such as fog or heavy rain, where laser 
measurements could be disrupted. This limita-
tion might necessitate the use of complementary 
sensors or techniques to ensure reliable operation 
under all conditions.
4.	 Novel positioning method for UAVs in GNSS-denied 
environments (Cui et al., 2024):
•	Description: Cui et al. proposed a novel position-
ing method for UAVs in GNSS-denied environ-
ments using a Mechanical Antenna (MA). The 
system comprises a rotating permanent magnet-
based MA installed on the UAV, which generates a 
Low-Frequency (LF) magnetic signal. This signal is 
received by a 3D magnetic field sensor at a ground 
base station. The positioning algorithm employed 
is based on Particle Swarm Optimization (PSO), 
which calculates the UAV’s position relative to the 
base station. The LF bands offer high propagation 
stability and strong anti-interference capabilities, 
making this method particularly effective in chal-
lenging environments such as dense forests or 
underground areas. Experimental results showed 
that the system achieved a mean positioning error 
of 0.43 ms within a range of 549 ms. The experi-
ments also demonstrated that the system main-
tained a stable signal propagation and was resilient 
to environmental interferences, making it a robust 
alternative for accurate UAV positioning in sce-
narios where GNSS signals are unreliable or una-
vailable.
•	Strengths: This method is highly effective in envi-
ronments where traditional GNSS signals are 
unreliable, such as dense forests or underground 
areas. The LF magnetic signal generated by the 
MA ensures stable and interference-resistant 
communication. The PSO algorithm enhances 
the system’s accuracy and efficiency in position 
calculation, making it suitable for a wide range of 
industrial applications. The system’s positioning 
accuracy of 0.43 ms is a significant achievement, 
highlighting its potential for precise navigation in 
GNSS-denied environments.
•	Limitations: The reliance on ground-based infra-
structure, such as the 3D magnetic field sensor 
and base station, limits the system’s flexibility and 
scalability for large-scale or remote operations. 
The system also requires precise calibration and 
maintenance of the ground station to ensure accu-

## Page 27

Page 27 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
racy. Additionally, the effective range of 549  ms 
may not be sufficient for all applications, particu-
larly those requiring long-range positioning.
5.	 Long-range GPS-denied aerial navigation with LiDAR 
localization (Hemann et al., 2016):
•	Description: Hemann et  al. presented a method 
for long-range GPS-denied aerial navigation using 
LiDAR localization, validated on two helicopter 
flights covering distances of 196 km and 218 km. 
The system achieved a final position error of 
27.2 ms, representing 0.012% of the total distance 
traveled, demonstrating a significant improvement 
in drift-free navigation over long distances. The 
method integrates LiDAR measurements with an 
error-state KF, which uses intermittent global cor-
rections to maintain an accurate state estimate. 
The LiDAR system provided 42,000 measurements 
per second, and the method was tested using 10 m 
resolution DEMs from the U.S. Geological Sur-
vey’s (USGS). The system exhibited robustness in 
challenging environments, such as dense vegeta-
tion or low terrain variability, demonstrating the 
feasibility of long-distance GPS-denied navigation 
using advanced sensor fusion techniques.
•	Strengths: The LiDAR-based system is highly effec-
tive for long-range navigation, offering minimal 
drift over extended distances. It performs well in 
different environments, including those with lim-
ited visual features, and is less affected by lighting 
conditions. The system’s ability to maintain a small 
position error (within 27.2 ms over 218 km) dem-
onstrates its robustness in challenging conditions.
•	Limitations: The system’s reliance on accurate 
and up-to-date DEMs can limit its effectiveness 
in rapidly changing environments. While LiDAR 
systems are more expensive and required higher 
computational resources-potentially restricting 
their use in smaller UAVs or cost-sensitive appli-
cations-we acknowledge that recent developments 
(e.g., Livox Mid 360, Unitree L1, Intel Realsense 
L515) offer more compact, lightweight, and 
energy-efficient LiDAR sensors with lower price. 
Nevertheless, challenges remain, especially when 
operating in featureless or uniformly flat terrains 
(e.g., flying over water or regions with minimal 
height variation), where both LiDAR and DEM-
based matching can struggle to maintain accuracy 
due to the lack of distinct features. As such, addi-
tional sensing modalities (e.g. RGB/thermal cam-
eras) or complementary algorithms may still be 
necessary to ensure robust performance in these 
environments.
The experimental results reveal multiple strategies for 
UAV localization in GPS-denied environments, with 
different systems excelling in specific conditions. Some 
systems perform best in structured and visually rich 
settings, while others are more effective in complex ter-
rains where traditional methods fall short. It is noted that 
achieving centimeter-level accuracy is typically feasible 
only in optimal, feature-rich settings. However, outdoor 
environments often introduce additional challenges that 
can impact performance.
Implications for different UAV types and altitudes
One important practical consideration in selecting a non-
GNSS navigation strategy is the type of UAV platform 
and its typical flight altitude.
Fixed-wing UAVs often fly at higher altitudes and 
maintain faster and more stable flight profiles. As a 
result, techniques leveraging coarse or large-scale terrain 
matching-such as TERCOM and DSMAC-can be more 
suitable for these platforms. Their reliance on broader 
and consistent terrain features aligns well with the alti-
tude ranges and speed envelopes that many fixed-wing 
aircraft maintain. On the other hand, rotorcrafts (e.g., 
quadcopters), which typically operate at lower altitudes 
and hover or fly slowly, benefit more from SLAM-based 
methods or visual odometry. These techniques rely on 
local and detailed features in the immediate environ-
ment, which rotorcraft can capture effectively due to 
their proximity to the ground and slower, more agile 
flight dynamics.
Consequently, the operational envelope (e.g., flight alti-
tude, speed) and vehicle type (fixed-wing vs. rotorcraft) 
become important design considerations when deciding 
on sensor payload and navigation algorithms. Fixed-wing 
UAVs may allocate more onboard resources for terrain-
based correlation (using DEMs, RADAR altimetry, etc.), 
while rotorcraft often favor real-time vision or LiDAR-
based SLAM pipelines.
Going forward, system designers should continue to 
tailor navigation algorithms to the primary use cases of 
each UAV platform, ensuring that processing power, sen-
sor selection, and algorithmic complexity match the flight 
regimes. Balancing these trade-offs can optimize perfor-
mance and reliability in diverse GNSS-denied conditions.
Future directions
The advancement of autonomous localization tech-
nologies, encompassing both absolute and relative 
localization, is crucial for the future of UAV operations, 
particularly in GNSS-denied environments. As these

## Page 28

Page 28 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
technologies evolve, several key areas offer substantial 
opportunities for innovation, enhancing UAV capabilities 
in challenging conditions:
•	 Advanced multi-modal sensor fusion: Integrating data 
from various sensors into a unified framework is cru-
cial to overcoming individual sensor limitations. By 
synthesizing information from sources such as cam-
eras, LiDAR, RADAR, and IMUs, UAVs can achieve 
a comprehensive understanding of their environ-
ment, significantly improving navigation accuracy in 
GPS-denied scenarios.
•	 Deep learning and AI integration: The integration 
of deep learning and AI for advanced data analy-
sis and predictive modeling is poised to transform 
UAV localization. These technologies empower 
UAVs to navigate autonomously through complex 
environments with higher precision by continually 
learning from and adapting to their surroundings. 
Future research will likely center on developing 
more advanced AI models capable of addressing 
the variability and unpredictability inherent in real-
world scenarios, ultimately improving the accuracy, 
reliability, and efficiency of UAV localization sys-
tems in GPS-denied environments.
•	 Enhancing real-time processing capabilities: Real-
time processing is crucial for UAVs, especially in 
GPS-denied environments where timely decision-
making based on sensor data is essential for safe 
navigation. To optimize performance, UAVs should 
leverage advanced computing platforms to reduce 
processing latency and fine-tune sensor fusion 
algorithms for specific hardware architectures 
using techniques such as data downsampling and 
optimized matrix operations. Additionally, main-
taining low-latency communication between sen-
sors and processing units through high-bandwidth 
protocols and strategic positioning is vital to mini-
mize data transmission delays.
•	 Addressing implementation barriers: Implement-
ing multi-modal sensor fusion frameworks in UAVs 
presents several practical challenges essential for 
reliable operation. Achieving the full potential of 
UAV localization in GPS-denied environments 
necessitates ongoing advancements focused on:
–	 Sensor calibration: Future efforts must ensure 
accurate calibration, as it is crucial for reliable 
data fusion. Calibration errors can lead to signifi-
cant inaccuracies in UAV positioning and orien-
tation, particularly in GPS-denied environments 
where alternative navigational aids are unavail-
able.
–	 Data synchronization: Efforts must focus on 
improving synchronization mechanisms, as sensors 
often operate at different sampling rates and expe-
rience varying latencies. Advanced time-stamping 
and interpolation techniques will be critical to 
aligning data streams effectively.
–	 Environmental adaptation: Sensor systems must 
be developed to adapt to environmental factors 
like fog or low light. Future solutions should enable 
adaptive weighting of sensor inputs based on their 
reliability under specific conditions to maintain 
consistent performance.
–	 Software integration: Further work is required to 
develop middleware that efficiently manages data 
flow between sensors, fusion algorithms, and UAV 
control systems, ensuring seamless software inte-
gration.
–	 Power efficiency: Efforts should focus on energy-
efficient algorithms and hardware to manage the 
increased power demands from sensor fusion, 
which is particularly critical for battery-powered 
UAVs.
–	 Scalability: Future sensor fusion frameworks should 
be designed to integrate additional sensors and 
adapt to various UAV platforms without requiring 
significant reconfiguration, ensuring scalability.
Conclusion
This paper presents a comprehensive review of key devel-
opments in UAV navigation, with a particular focus on 
operations in environments where GNSS is unavailable. 
Our analysis highlights key innovations in sensor tech-
nologies, including IMUs, barometers, and the strategic 
fusion of cameras, RADAR, and LiDAR. These advance-
ments have collectively reduced the dependency on 
GNSS, allowing UAVs to operate more effectively in chal-
lenging environments. A key component of these innova-
tions is the integration of VIO and SLAM, both essential 
for improving UAV localization accuracy. VIO combines 
visual data with inertial measurements, allowing for pre-
cise navigation even when GNSS signals are unreliable. 
Meanwhile, SLAM enhances this capability by simulta-
neously mapping unknown environments and tracking 
the UAV’s position, enabling seamless interaction with 
dynamic surroundings.
Furthermore, our survey emphasized the transforma-
tive potential of AI-driven Semantic Mapping and Recog-
nition technologies, which enable UAVs to autonomously 
recognize and categorize environmental features, sig-
nificantly improving decision-making and operational 
efficiency. These improvements become even more 
impactful when integrated with absolute methods such

## Page 29

Page 29 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
as terrain-aided navigation techniques like TERCOM and 
DSMAC, offering a powerful synergy. AI improves the 
UAV’s ability to interpret complex terrains, while terrain-
based techniques ensure precise positioning, providing 
reliable path finding even in the most challenging condi-
tions without GNSS signals. By combining AI’s real-time 
scene analysis with terrain elevation data, these methods 
enhance the robustness of UAV navigation in GNSS-
denied environments.
In conclusion, this survey provides a comprehensive 
overview of the current advancements in UAV navigation 
in GNSS-denied environments, highlighting both sig-
nificant achievements and areas ripe for further research. 
The collaborative efforts of the international research 
community are crucial in overcoming the challenges 
of GNSS-independent navigation, ultimately aiming to 
equip UAVs for safe and efficient operation in diverse 
environments. As the field continues to evolve, the inte-
gration of cutting-edge sensors, advanced algorithms, 
and innovative localization techniques will be instrumen-
tal in shaping the future of autonomous UAV navigation, 
making airspace more navigable and accessible than ever 
before.
Acknowledgements
The authors express their gratitude for the support provided by Prince Sultan 
University (PSU) in Saudi Arabia.
Author contributions
Conceptualization, I.J, M.A. and A.K.; Writing—Original Draft Preparation, I.J, 
A.S.A.-B., M.B.K., M.A., and A.A.; Writing—Review & Editing, A.S.A.-B., M.B.K., M.A., 
M.A., A.A., and W.B.; Supervision, M.B.K. and A.K.; project administration, All 
authors have read and agreed to the published version of the manuscript.
Funding
The research was funded by PSDSARC seed project number (PSDSARC Project 
ID: PID-000085_01_02), and the APC was funded by PSU.
Availability of data and materials
There are no data or materials available.
Declarations
Competing interests
The authors declare no Conflict of interest.
Received: 29 April 2024   Revised: 22 January 2025   Accepted: 24 January 
2025
References
Ahmad, M. W., & Akram, M. U. (2024). Uav sensor failures dataset: Biomisa 
arducopter sensory critique (basic). Data in Brief, 52, 110069. https://​doi.​
org/​10.​1016/j.​dib.​2024.​110069
Abdelkader, M., Al-Batati, A.S., Jarraya, I., & Koubaa, A. (2024). D2dtracker: A 
framework for enabling real-time trajectory prediction for agile drone-
to-drone tracking via adaptive model selection. In: 2024 2nd Interna‑
tional Conference on Unmanned Vehicle Systems-Oman (UVS), pp. 1–7. 
https://​doi.​org/​10.​1109/​UVS59​522.​2024.​98711​23 . IEEE
Almomani, I., Ahmed, M., Kosmanos, D., Alkhayer, A., & Maglaras, L. (2022). An 
efficient localization and avoidance method of jammers in vehicular ad 
hoc networks. IEEE Access, 10, 131640–131655. https://​doi.​org/​10.​1109/​
ACCESS.​2022.​32296​23
Allak, E., Brommer, C., Dallenbach, D., & Weiss, S. (2020). Amadee-18: Vision-
based unmanned aerial vehicle navigation for analog mars mission 
(avi-nav). Astrobiology, 20(11), 1321–1337. https://​doi.​org/​10.​1089/​ast.​
2019.​2036
Allouch, A., Cheikhrouhou, O., Koubâa, A., Toumi, K., Khalgui, M., & Nguyen 
Gia, T. (2021). Utm-chain: Blockchain-based secure unmanned traffic 
management for internet of drones. Sensors, 21(9), 3049.
Abdelkader, M., Gabr, K., Jarraya, I., AlMusalami, A., & Koubaa, A. (2025). 
Smart-track: A novel kalman filter-guided sensor fusion for robust uav 
object tracking in dynamic environments. IEEE Sensors Journal, 25(2), 
3086–3097. https://​doi.​org/​10.​1109/​JSEN.​2024.​35059​39
Al-lQubaydhi, N., Alenezi, A., Alanazi, T., Senyor, A., Alanezi, N., Alotaibi, B., 
Alotaibi, M., Razaque, A., & Hariri, S. (2024). Deep learning for unmanned 
aerial vehicles detection: A review. Computer Science Review, 51, 100614. 
https://​doi.​org/​10.​1016/j.​cosrev.​2023.​100614
Alpern, S. (2023). The faulty satnav (gps) problem: Search for home in networks 
with unreliable directions. Theoretical Computer Science, 975, 114109. 
https://​doi.​org/​10.​1016/j.​tcs.​2023.​114109
AbdulMajuid, A., Mohamady, O., Draz, M., & El-bayoumi, G. (2021). Gps-denied 
navigation using low-cost inertial sensors and recurrent neural net‑
works. arXiv preprint arXiv:​2109.​04861, https://​doi.​org/​10.​48550/​arXiv.​
2109.​04861
Allik, B.L., Schomer, N., & Miller, C. (2022). Localization for aerial systems in gps 
denied environments using recognition. In: AIAA SCITECH 2022 Forum, 
doi 10.2514/6.2022-2212
Alhafnawi, M., Salameh, H. B., Masadeh, A., Al-Obiedollah, H., Ayyash, M., 
El-Khazali, R., & Elgala, H. (2023). A survey of indoor and outdoor uav-
based target tracking systems: Current status, challenges, technologies, 
and future directions. IEEE Access. https://​doi.​org/​10.​1109/​ACCESS.​2023.​
32990​57
Ali, B., Sadekov, R. N., & Tsodokova, V. V. (2022). A review of navigation algo‑
rithms for unmanned aerial vehicles based on computer vision systems. 
Gyroscopy and Navigation, 13(4), 241–252. https://​doi.​org/​10.​1134/​
S2075​10872​20400​22
Alkendi, Y., Seneviratne, L., & Zweiri, Y. (2021). State of the art in vision-based 
localization techniques for autonomous navigation systems. IEEE Access, 
9, 76847–76874. https://​doi.​org/​10.​1109/​ACCESS.​2021.​30827​78
Benjumea, D., Alcántara, A., Ramos, A., Torres-Gonzalez, A., Sánchez-Cuevas, P., 
Capitan, J., Heredia, G., & Ollero, A. (2021). Localization system for light‑
weight unmanned aerial vehicles in inspection tasks. Sensors, 21(17), 
5937. https://​doi.​org/​10.​3390/​s2117​5937
Baker, W., & Clem, R. (1977). Terrain contour matching [tercom] primer. 
Technical ReportASP-TR-77-61. AeronauticalSystems Division, Wright-
Patterson AFB
Brommer, C., Fornasier, A., Scheiber, M., et al. (2024). The insane dataset: Large 
number of sensors for challenging uav flights in mars analog, outdoor, 
and out-/indoor transition scenarios. The International Journal of Robot-
ics Research, 43(8), 1083–1113. https://​doi.​org/​10.​1177/​02783​64924​
12272​45
Bui, D. V., Kubo, M., & Sato, H. (2023). Cross-view geo-localization for autono‑
mous uav using locally-aware transformer-based network. IEEE Access. 
https://​doi.​org/​10.​1109/​ACCESS.​2023.​32982​92
Burri, M., Nikolic, J., Gohl, P., Schneider, T., Rehder, J., Omari, S., Achtelik, M. W., & 
Siegwart, R. (2016). The euroc micro aerial vehicle datasets. The Interna-
tional Journal of Robotics Research, 35(10), 1157–1163. https://​doi.​org/​
10.​1177/​02783​64915​620033
Boroujeni, S.P.H., Razi, A., Khoshdel, S., Afghah, F., Coen, J.L., ONeill, L., Fule, P.Z., 
Watts, A., Kokolakis, N.-M.T., & Vamvoudakis, K.G. (2024). A comprehen‑
sive survey of research towards ai-enabled unmanned aerial systems in 
pre-, active-, and post-wildfire management. https://​doi.​org/​10.​48550/​
arXiv.​2401.​02456, arXiv preprint arXiv:​2401.​02456
Couturier, A., & Akhloufi, M. A. (2021). A review on absolute visual localization 
for uav. Robotics and Autonomous Systems, 135, 103666. https://​doi.​org/​
10.​1016/j.​robot.​2020.​103666
Chandrasekar, V., Beauchamp, R. M., & Bechini, R. (2023). Introduction to dual 
polarization weather radar: Fundamentals, applications, and networks. . 
https://​doi.​org/​10.​1017/​97811​08772​266

## Page 30

Page 30 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
Carroll, J. D., & Canciani, A. J. (2021). Terrain-referenced navigation using 
a steerable-laser measurement sensor. Navigation, 68(1), 115–134. 
https://​doi.​org/​10.​1002/​navi.​406
Chiang, K., Chiu, Y., Srinara, S., & Tsai, M. (2023). Performance of lidar-slam-based 
pnt with initial poses based on ndt scan matching algorithm. Satellite 
Navigation, 4(1), 3. https://​doi.​org/​10.​1186/​s43020-​022-​00092-0
Cottrill, H. S., & Gu, Y. (2024). Enhanced 3d localization on venus: A map match‑
ing and particle filtering approach. In: AIAA SCITECH 2024 Forum. https://​
doi.​org/​10.​2514/6.​2024-​2270
Corporation, N. (2025). Isaac ROS Visual SLAM Documentation. https://​nvidia-​
isaac-​ros.​github.​io/​repos​itori​es_​and_​packa​ges/​isaac_​ros_​visual_​slam/​
index.​html. Accessed: 2025-01-06
Chen, C., & Pan, X. (2024). Deep learning for inertial positioning: A survey. IEEE 
Transactions on Intelligent Transportation Systems. https://​doi.​org/​10.​
1109/​TITS.​2024.​33811​61
Cao, Y., Ren, K., & Chen, Q. (2023). Template matching based on convolution 
neural network for uav visual localization. Optik, 283, 170920. https://​
doi.​org/​10.​1016/j.​ijleo.​2023.​170920
Carr, J. R., & Sobek, J. S. (1980). Digital scene matching area correlator (dsmac). 
In Image Processing For Missile Guidance, 238, 36–41. https://​doi.​org/​10.​
1117/​12.​959130
Cui, Y., Wang, C., Hu, Q., Xu, B., Song, X., Yuan, Z., & Zhu, Y. (2024). A novel 
positioning method for uav in gnss-denied environments based on 
mechanical antenna. IEEE Transactions on Industrial Electronics. https://​
doi.​org/​10.​1109/​TIE.​2023.​33478​59
Deraz, A. A., Badawy, O., Elhosseini, M. A., Mostafa, M., Ali, H. A., & El-Desouky, 
A. I. (2023). Deep learning based on lstm model for enhanced visual 
odometry navigation system. Ain Shams Engineering Journal, 14(8), 
102050. https://​doi.​org/​10.​1016/j.​asej.​2023.​102050
Ding, P., & Cheng, X. (2022). A new contour-based combined matching 
algorithm for underwater terrain-aided strapdown inertial navigation 
system. Measurement, 202, 111870. https://​doi.​org/​10.​1016/j.​measu​
rement.​2022.​111870
Dang, Y., Karakoc, A., Norshahida, S., & Jäntti, R. (2023). 3d radio map-based gps 
spoofing detection and mitigation for cellular-connected uavs. IEEE 
Transactions on Machine Learning in Communications and Networking. 
https://​doi.​org/​10.​1109/​TMLCN.​2023.​33056​18
Dissanayaka, D., Wanasinghe, T. R., De Silva, O., Jayasiri, A., & Mann, G. K. (2023). 
Review of navigation methods for uav-based parcel delivery. IEEE 
Transactions on Automation Science and Engineering. https://​doi.​org/​10.​
1109/​TASE.​2023.​33214​93
Ellingson, G., Brink, K., & McLain, T. (2020). Relative navigation of fixed-wing 
aircraft in gps-denied environments. NAVIGATION: Journal of the Institute 
of Navigation, 67(2), 255–273. https://​doi.​org/​10.​1002/​navi.​364
Elkholy, M., Elsheikh, M., & El-Sheimy, N. (2023). Radar/INS integration and map 
matching for land vehicle navigation in urban environments. Sensors, 
23(11), 5119. https://​doi.​org/​10.​3390/​s2311​5119
El-Sheimy, N., & Li, Y. (2021). Indoor navigation: State of the art and 
future trends. Satellite Navigation, 2(1), 7. https://​doi.​org/​10.​1186/​
s43020-​021-​00041-3
El Sabbagh, M. S., Maher, A., Abozied, M. A., & Kamel, A. M. (2023). Promoting 
navigation system efficiency during gps outage via cascaded neural 
networks: A novel ai based approach. Mechatronics, 94, 103026. https://​
doi.​org/​10.​1016/j.​mecha​troni​cs.​2023.​103026
Eshmawi, A. A., Umer, M., Ashraf, I., & Park, Y. (2024). Enhanced machine learn‑
ing ensemble approach for securing small unmanned aerial vehicles 
from gps spoofing attacks. IEEE Access, 12, 27344–27355. https://​doi.​
org/​10.​1109/​ACCESS.​2024.​33597​00
Ford C. Eng, T. (1985). MRAeS: Flight instrumentation. Aircraft Engineering and 
Aerospace Technology, 57(4), 2–23. https://​doi.​org/​10.​1108/​eb036​092
Fang, Z., Han, B., & Schotten, H.D. (2024). 3D cooperative localization in uav 
systems: Crlb analysis and security solutions. arXiv preprint arXiv:​2402.​
09810, https://​doi.​org/​10.​48550/​arXiv.​2402.​09810
Forsyth, R. (2024). Me 163 Vs Allied Heavy Bombers: Northern Europe 1944–45 
Duel (1st ed.). Oxford: Osprey Publishing. https://​doi.​org/​10.​5040/​97814​
72861​863
Gallo, E., & Barrientos, A. (2022). Reduction of gnss-denied inertial navigation 
errors for fixed wing autonomous unmanned air vehicles. Aerospace 
Science and Technology, 120, 107237. https://​doi.​org/​10.​1016/j.​ast.​2021.​
107237
Gallo, E., & Barrientos, A. (2023). Gnss-denied semi-direct visual navigation for 
autonomous uavs aided by pi-inspired inertial priors. Aerospace, 10(3), 
220. https://​doi.​org/​10.​3390/​aeros​pace1​00302​20
Ge, J., Cheng, J., & Qi, B. (2024). A non-rigid terrain transformation particle filter 
suitable for terrain-aided navigation without sound velocity profile. 
Ocean Engineering, 294, 116858. https://​doi.​org/​10.​1016/j.​ocean​eng.​
2023.​116858
Guo, H., Chen, X., Yu, M., Uradziński, M., & Cheng, L. (2024). The usefulness of 
sensor fusion for unmanned aerial vehicle indoor positioning. Interna-
tional Journal of Intelligent Unmanned Systems, 12(1), 1–18. https://​doi.​
org/​10.​1108/​IJIUS-​01-​2023-​0006
Galati, G., & Galati, G. (2016). The radar flies: Birth and development of 
airborne and of anti-submarine warfare systems. 100 Years of 
Radar, Springer International Publishing, Cham, pp 147–190, doi 
10.1007/978-3-319-00584-3_6
Gambrych, J., Gromek, D., Abratkiewicz, K., Wielgo, M., Gromek, A., & 
Samczyński, P. (2023). Sar and orthophoto image registration with 
simultaneous sar-based altitude measurement for airborne navigation 
systems. IEEE Transactions on Geoscience and Remote Sensing, 61, 1–14. 
https://​doi.​org/​10.​1109/​TGRS.​2023.​33270​90
Gonzalez-Jorge, H., Aldao, E., Fontenla-Carrera, G., Veiga-López, F., Balvís, E., & 
Ríos-Otero, E. (2024). Counter drone technology: A review. https://​doi.​org/​
10.​20944/​prepr​ints2​02402.​0551.​v1
Ghasemieh, A., & Kashef, R. (2024). Towards explainable artificial intelligence in 
deep vision-based odometry. Computers and Electrical Engineering, 115, 
109127. https://​doi.​org/​10.​1016/j.​compe​leceng.​2024.​109127
Gupta, D., Khanna, A., Bhattacharyya, S., Hassanien, A.E., Anand, S., & Jaiswal, 
A. (2022). International Conference on Innovative Computing and Com‑
munications: Proceedings of ICICC 2022, Volume 1 vol. 473. Springer, 
Singapore. https://​doi.​org/​10.​1007/​978-​981-​19-​2821-5
Golden, J. P. (1980). Terrain contour matching (tercom): a cruise missile guid‑
ance aid. Image Processing for Missile Guidance, 238, 10–18. https://​doi.​
org/​10.​1117/​12.​959127
Gao, J., Sha, J., Wang, Y., Wang, X., & Tan, C. (2024). A fast and stable gnss-
lidar-inertial state estimator from coarse to fine by iterated error-state 
kalman filter. Robotics and Autonomous Systems, 175, 104675. https://​
doi.​org/​10.​1016/j.​robot.​2024.​104675
Gao, C., Wang, X., Wang, R., Zhao, Z., Zhai, Y., Chen, X., & Chen, B. M. (2023). A 
uav-based explore-then-exploit system for autonomous indoor facility 
inspection and scene reconstruction. Automation in Construction, 148, 
104753. https://​doi.​org/​10.​1016/j.​autcon.​2023.​104753
Gao, H., Yu, Y., Huang, X., Song, L., Li, L., Li, L., & Zhang, L. (2023). Enhancing the 
localization accuracy of uav images under gnss denial conditions. Sen-
sors, 23(24), 9751. https://​doi.​org/​10.​3390/​s2324​9751
Gong, J., Yan, J., Hu, H., Kong, D., & Li, D. (2023). Improved radar detection 
of small drones using doppler signal-to-clutter ratio (dscr) detector. 
Drones, 7(5), 316. https://​doi.​org/​10.​3390/​drone​s7050​31
Hosseini, K., Ebadi, H., & Farnood Ahmadi, F. (2020). Determining the location 
of uavs automatically using aerial or remotely sensed high-resolution 
images for intelligent navigation of uavs at the time of disconnection 
with gps. Journal of the Indian Society of Remote Sensing, 48, 1675–1689. 
https://​doi.​org/​10.​1007/​s12524-​020-​01197-2
Hollowell, J. (1990). Heli/sitan: A terrain referenced navigation algorithm for 
helicopters. Technical report, Sandia National Lab.(SNL-NM), Albuquer‑
que, NM (United States). https://​doi.​org/​10.​1109/​PLANS.​1990.​66236
Ho, J., Phang, S., & Mun, H. (2021). 2-d uav navigation solution with lidar sensor 
under gps-denied environment. In: Journal of Physics: Conference 
Series, vol. 2120, p. 012026. https://​doi.​org/​10.​1088/​1742-​6596/​2120/1/​
012026 . IOP Publishing
Hemann, G., Singh, S., & Kaess, M. (2016). Long-range gps-denied aerial inertial 
navigation with lidar localization. In: 2016 IEEE/RSJ International Confer‑
ence on Intelligent Robots and Systems (IROS), pp. 1659–1666. https://​
doi.​org/​10.​1109/​IROS.​2016.​77592​67 . IEEE
He, G., Yuan, X., Zhuang, Y., & Hu, H. (2020). An integrated gnss/lidar-slam pose 
estimation framework for large-scale map building in partially gnss-
denied environments. IEEE Transactions on Instrumentation and Measure-
ment, 70, 1–9. https://​doi.​org/​10.​1109/​TIM.​2020.​30244​05
Hou, L., Zhang, S., Wang, C., Li, X., Chen, S., Zhu, L., & Zhu, Y. (2023). Jamming 
recognition of carrier-free uwb cognitive radar based on manet. IEEE 
Transactions on Instrumentation and Measurement. https://​doi.​org/​10.​
1109/​TIM.​2023.​32987​62

## Page 31

Page 31 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
	
Jensen, N. I., & Budge, S. E. (2023). Gps-denied navigation using location 
estimation and texel image correction. Autonomous Systems: Sensors, 
Processing and Security for Ground, Air, Sea, and Space Vehicles and Infra-
structure, 12540, 168–176. https://​doi.​org/​10.​1117/​12.​26641​19
Jurevičius, R., Marcinkevičius, V., & Šeibokas, J. (2019). Robust gnss-denied 
localization for uav using particle filter and visual odometry. Machine 
Vision and Applications, 30, 1181–1190. https://​doi.​org/​10.​1007/​
s00138-​019-​01046-4
Khawaja, W., Ezuma, M., Semkin, V., Erden, F., Ozdemir, O., & Guvenc, I. (2024). A 
survey on detection, classification, and tracking of aerial threats using 
radar and communications systems. arXiv preprint arXiv:​2402.​05909, 
https://​doi.​org/​10.​48550/​arXiv.​2402.​05909
Kim, T., Kim, D., Kim, S., Kim, Y., & Han, S. (2022). Improved optical sensor fusion 
in UAV navigation using feature point threshold filter. International 
Journal of Aeronautical and Space Sciences, 23(1), 1–12. https://​doi.​org/​
10.​1007/​s42405-​021-​00423-6
Kinnari, J., Renzulli, R., Verdoja, F., & Kyrki, V. (2023). Lsvl: Large-scale season-
invariant visual localization for uavs. Robotics and Autonomous Systems, 
168, 104497. https://​doi.​org/​10.​1016/j.​robot.​2023.​104497
Kinnari, J., Verdoja, F., & Kyrki, V. (2022). Season-invariant gnss-denied visual 
localization for UAVs. IEEE Robotics and Automation Letters, 7(4), 
10232–10239. https://​doi.​org/​10.​1109/​LRA.​2022.​31878​45
Lindstrom, C., Christensen, R., Gunther, J., & Jenkins, S. (2022). Gps-denied 
navigation aided by synthetic aperture radar using the range-doppler 
algorithm. NAVIGATION: Journal of the Institute of Navigation, 69(3), 533. 
https://​doi.​org/​10.​33012/​navi.​533
Liden, S. (1994). The evolution of flight management systems. In: AIAA/IEEE 
Digital Avionics Systems Conference. 13th DASC, pp. 157–169. https://​
doi.​org/​10.​1109/​DASC.​1994.​369487 . IEEE
Lu, Z., Liu, F., & Lin, X. (2022). Vision-based localization methods under GPS-
denied conditions. https://​doi.​org/​10.​48550/​arXiv.​2211.​11988
Luo, H., Li, G., Zou, D., Li, K., Li, X., & Yang, Z. (2023). UAV navigation with 
monocular visual inertial odometry under GNSS-denied environment. 
IEEE Transactions on Geoscience and Remote Sensing. https://​doi.​org/​10.​
1109/​TGRS.​2023.​33235​19
Lee, J., Sung, C.-K., Oh, J., Han, K., Lee, S., & Yu, M.-J. (2020). A pragmatic 
approach to the design of advanced precision terrain-aided navigation 
for uavs and its verification. Remote Sensing, 12(9), 1396. https://​doi.​org/​
10.​3390/​rs120​91396
Lu, H., Shen, H., Tian, B., Zhang, X., Yang, Z., & Zong, Q. (2022). Flight in gps-
denied environment: Autonomous navigation system for micro-aerial 
vehicle. Aerospace Science and Technology, 124, 107521. https://​doi.​org/​
10.​1016/j.​ast.​2022.​107521
Li, X., Wang, X., Liao, J., Li, X., Li, S., & Lyu, H. (2021). Semi-tightly coupled 
integration of multi-gnss ppp and s-vins for precise positioning in gnss-
challenged environments. Satellite Navigation, 2, 1–14. https://​doi.​org/​
10.​1186/​s43020-​020-​00033-9
Liu, X., Wang, Z., Wu, Y., & Miao, Q. (2024). Segcn: A semantic-aware graph 
convolutional network for uav geo-localization. IEEE Journal of Selected 
Topics in Applied Earth Observations and Remote Sensing. https://​doi.​org/​
10.​1109/​JSTARS.​2024.​33706​12
Liu, Y., Wang, S., Xie, Y., Xiong, T., & Wu, M. (2024). A review of sensing technolo‑
gies for indoor autonomous mobile robots. Sensors, 34(4), 1222. https://​
doi.​org/​10.​3390/​s2404​1222
Li, R., Zheng, S., Wang, E., Chen, J., Feng, S., Wang, D., & Dai, L. (2020). Advances 
in beidou navigation satellite system (bds) and satellite navigation 
augmentation technologies. Satellite Navigation, 1, 1–23. https://​doi.​
org/​10.​1186/​s43020-​020-​00010-2
Materak, W. (2023). The evolution of air threats in future conflicts. Safety & 
Defense, 9(1), 24–30. https://​doi.​org/​10.​37105/​sd.​196
Mughal, M. H., Khokhar, M. J., & Shahzad, M. (2021). Assisting uav localization 
via deep contextual image matching. IEEE Journal of Selected Topics in 
Applied Earth Observations and Remote Sensing, 14, 2445–2457. https://​
doi.​org/​10.​1109/​JSTARS.​2021.​30620​28
Matyja, T., Stanik, Z., & Kubik, A. (2024). Automatic correction of baro‑
metric altimeters using additional air temperature and humidity 
measurements. GPS Solutions, 28(1), 40. https://​doi.​org/​10.​1007/​
s10291-​023-​01582-7
Moore, A., Schubert, M., Rymer, N. H., Villalobos, D., Glover, J. S., Ozturk, D., & 
Dill, E. T. (2022). Volume raycasting of GNSS signals through ground 
structure lidar for UAV navigational guidance and safety estimation. In 
AIAA Scitech 2022 Forum. https://​doi.​org/​10.​2514/6.​2022-​2218
Marut, A., Wojciechowski, P., Wojtowicz, K., & Falkowski, K. (2023). Visual-based 
landing system of a multirotor uav in gnss denied environment. In: 
2023 IEEE 10th International Workshop on Metrology for AeroSpace 
(MetroAeroSpace), pp. 308–313. https://​doi.​org/​10.​1109/​Metro​AeroS​
pace5​7412.​2023.​10190​013 . IEEE
Ngo, E., Ramirez, J., Medina-Soto, M., Dirksen, S., Victoriano, E.D., & Bhandari, 
S. (2022). Uav platforms for autonomous navigation in gps-denied 
environments for search and rescue missions. In: 2022 International 
Conference on Unmanned Aircraft Systems (ICUAS), pp. 1481–1488. 
https://​doi.​org/​10.​1109/​ICUAS​54217.​2022.​98361​81 . IEEE
Nagla, K., & Yadav, S. (2024). Sonar sensor advancements. In: Handbook of 
Vibroacoustics Noise and Harshness. Singapore: Springer. https://​doi.​org/​
10.​1007/​978-​981-​99-​4638-9_​46-1
Ouyang, C., Hu, S., Long, F., Shi, S., Yu, Z., Zhao, K., You, Z., Pi, J., & Xing, B. (2023). 
A semantic vector map-based approach for aircraft positioning in gnss/
gps denied large-scale environment. Defence Technology, 33, 209–221. 
https://​doi.​org/​10.​1016/j.​dt.​2023.​06.​002
Ouyang, X., Zeng, F., Lv, D., Dong, T., & Wang, H. (2020). Cooperative naviga‑
tion of UAVs in GNSS-denied area with colored rssi measurements. IEEE 
Sensors Journal, 21(2), 2194–2210. https://​doi.​org/​10.​1109/​JSEN.​2020.​
30253​99
Pany, T., Akos, D., Arribas, J., Bhuiyan, M. Z. H., Closas, P., Dovis, F., Fernandez-
Hernandez, I., Fernández-Prades, C., Gunawardena, S., Humphreys, T., 
et al. (2022). Gnss software defined radio History current developments 
and standardization efforts. In 35th International Technical Meeting of the 
Satellite Division of the Institute of Navigation ION GNSS., 5, 3148–3177. 
https://​doi.​org/​10.​33012/​2022.​18434
pjrambo. (2025). VINS-Fusion with GPU Acceleration. https://​github.​com/​pjram​
bo/​VINS-​Fusion-​gpu. Accessed: 2025-01-06
Peng, J., Zhang, P., Zheng, L., & Tan, J. (2020). UAV positioning based on multi-
sensor fusion. IEEE Access, 8, 34455–34467. https://​doi.​org/​10.​1109/​
ACCESS.​2020.​29742​85
Qin, T., Li, P., & Shen, S. (2018). Vins-mono: A robust and versatile monocu‑
lar visual-inertial state estimator. IEEE transactions on robotics, 34(4), 
1004–1020. https://​doi.​org/​10.​1109/​TRO.​2018.​28537​29
Rani, A. R., Anusha, Y., Cherishama, S., & Laxmi, S. V. (2024). Traffic sign detec‑
tion and recognition using deep learning-based approach with haze 
removal for autonomous vehicle navigation. e-Prime–Advances in 
Electrical Engineering, Electronics and Energy, 7, 100442. https://​doi.​org/​
10.​1016/j.​prime.​2024.​100442
Rezwan, S., & Choi, W. (2022). Artificial intelligence approaches for uav naviga‑
tion: Recent advances and future challenges. IEEE Access, 10, 26320–
26339. https://​doi.​org/​10.​1109/​ACCESS.​2022.​31576​26
Rosten, E., Porter, R., & Drummond, T. (2010). Faster and better: A machine 
learning approach to corner detection. IEEE Transactions on Pattern 
Analysis and Machine Intelligence, 32(1), 105–119. https://​doi.​org/​10.​
1109/​TPAMI.​2008.​275
Raković, D.M., Simonović, A., & Grbović, A.M. (2021). Uav positioning and 
navigation-review. In: Experimental and Computational Investiga‑
tions in Engineering: Proceedings of the International Conference of 
Experimental and Numerical Investigations and New Technologies, 
CNNTech 2020, pp. 220–256. https://​doi.​org/​10.​1007/​978-3-​030-​58362-
0_​14 . Springer
Rao, N., Sundaram, S., & Raghavendra, V. (2023). Computationally light 
spectrally normalized memory neuron network based estimator for 
gps-denied operation of micro-uav. In: 2023 9th International Confer‑
ence on Control, Decision and Information Technologies (CoDIT), pp. 
1894–1899.https://​doi.​org/​10.​1109/​CoDIT​56608.​2023.​10123​015 . IEEE
Shan, T., Englot, B., Meyers, D., Wang, W., Ratti, C., & Daniela, R. (2020). Lio-sam: 
Tightly-coupled lidar inertial odometry via smoothing and mapping. In: 
IEEE/RSJ International Conference on Intelligent Robots and Systems 
(IROS), pp. 5135–5142. https://​doi.​org/​10.​1109/​IROS4​5743.​2020.​93411​76 
. IEEE
Sivamani, G. K. S., & Gudipalli, A. (2024). Design and implementation of data 
logging and stabilization system for a uav. Heliyon. https://​doi.​org/​10.​
1016/j.​heliy​on.​2024.​e15042
Strauss, M.P., & Scott, M.W. (2024). 50 years of progress in rotorcraft design: A 
retrospective from the vertical flight society’s aircraft design technical 
committee, https://​doi.​org/​10.​13140/​RG.2.​2.​19219.​25124

## Page 32

Page 32 of 32
Jarraya et al. Satellite Navigation  (2025) 6:9
She, F., Zhang, Y., Shi, D., Zhou, H., Ren, X., & Xu, T. (2020). Enhanced relative 
localization based on persistent excitation for multi-UAVs in GPS-denied 
environments. IEEE Access, 8, 148136–148148. https://​doi.​org/​10.​1109/​
ACCESS.​2020.​30155​93
Taghizadeh, S., & Safabakhsh, R. (2023). An integrated INS/GNSS system with 
an attention-based hierarchical lstm during GNSS outage. GPS Solutions, 
27(2), 71. https://​doi.​org/​10.​1007/​s10291-​023-​01374-6
Tong, P., Yang, X., Yang, Y., Liu, W., & Wu, P. (2023). Multi-UAV collaborative abso‑
lute vision positioning and navigation: A survey and discussion. Drones, 
7(4), 261. https://​doi.​org/​10.​3390/​drone​s7040​261
Tahir, N. U. A., Zhang, Z., Asim, M., Chen, J., & ELAffendi, M. (2024). Object 
detection in autonomous vehicles under adverse weather: a review 
of traditional and deep learning approaches. Algorithms, 17(3), 103. 
https://​doi.​org/​10.​3390/​a1703​0103
Van Kirk, C., Chen, A., Biaz, S., & Chapman, R. (2022). Dead reckoning and terrain 
image processing as basis for UAV home-oriented navigation under 
foreign GPS-denied environments. Journal of Computing Sciences in 
Colleges, 38(2), 74–89.
Wang, G., Chen, J., Dai, M., & Zheng, E. (2023). Wamf-FPI: A weight-adaptive 
multi-feature fusion network for UAV localization. Remote Sensing, 15(4), 
910. https://​doi.​org/​10.​3390/​rs150​40910
Wang, D., Liu, L., Ben, Y., Dai, P., & Wang, J. (2023). Seabed terrain-aided naviga‑
tion algorithm based on combining artificial bee colony and particle 
swarm optimization. Applied Sciences, 13(2), 1166. https://​doi.​org/​10.​
3390/​app13​021166
Wang, D., Liu, L., Ben, Y., Dai, P., & Wang, J. (2024). Underwater terrain-matching 
algorithm based on improved iterative closest contour point algorithm. 
Measurement and Control, 57(7), 00202940231224569. https://​doi.​org/​
10.​1177/​00202​94023​12245​69
Wang, T., & Somani, A. K. (2020). Aerial-dem geolocalization for GPS-denied 
UAS navigation. Machine Vision and Applications, 31(1–2), 3. https://​doi.​
org/​10.​1007/​s00138-​019-​01069-w
Wan, X., Shao, Y., Zhang, S., & Li, S. (2022). Terrain aided planetary UAV localiza‑
tion based on geo-referencing. IEEE Transactions on Geoscience and 
Remote Sensing, 60, 1–18. https://​doi.​org/​10.​1109/​TGRS.​2022.​31987​45
White, T., Wheeler, J., Lindstrom, C., Christensen, R., & Moon, K.R. (2021). Gps-
denied navigation using sar images and neural networks. In: ICASSP 
2021-2021 IEEE International Conference on Acoustics, Speech and 
Signal Processing (ICASSP), pp. 2395–2399. https://​doi.​org/​10.​1109/​
ICASS​P39728.​2021.​94138​23 . IEEE
Wang, Y., Yan, C., Liang, C., Liu, Y., Li, H., Zhang, C., Duan, X., & Pan, Y. (2024). 
Polymers used in saw gas sensors for detecting sulfur-containing com‑
pounds, https://​doi.​org/​10.​20944/​prepr​ints2​02401.​1044.​v1
Wang, Q., Zheng, C., Wu, P., & Wang, X. (2022). Geomagnetic/inertial navigation 
integrated matching navigation method. Heliyon, 8(11), e11249. https://​
doi.​org/​10.​1016/j.​heliy​on.​2022.​e11249
Wang, F., Zou, Y., Zhang, C., Buzzatto, J., Liarokapis, M., Rey Castillo, E., & Lim, J. 
B. (2023). UAV navigation in large-scale GPS-denied bridge environ‑
ments using fiducial marker-corrected stereo visual-inertial localisation. 
Automation in Construction, 156, 105139. https://​doi.​org/​10.​1016/j.​
autcon.​2023.​105139
Xu, W., Cai, Y., He, D., Lin, J., & Zhang, F. (2021). FAST-LIO2: Fast Direct LiDAR-
inertial Odometry. IEEE Transactions on Robotics, 38(4), 2053–2073.
Xiaoyu, Y., Fujun, S., Rui, Z., & Qinghua, Z. (2024). Semi-aerodynamic model 
aided invariant kalman filtering for uav full-state estimation. IEEE Sensors 
Journal. https://​doi.​org/​10.​1109/​JSEN.​2024.​34149​95
Xueyu, D., Lilian, Z., Ruochen, L., Maosong, W., Wenqi, W., & Jun, M. (2024). Po-
msckf: An efficient visual-inertial odometry by reconstructing the multi-
state constrained kalman filter with the pose-only theory. arXiv preprint 
arXiv:​2407.​01888, https://​doi.​org/​10.​48550/​ARXIV.​2407.​01888
Xu, Y., Wan, D., Bi, S., Guo, H., & Zhuang, Y. (2023). A fir filter assisted with 
the predictive model and elm integrated for uwb-based quadrotor 
aircraft localization. Satellite Navigation, 4(1), 2. https://​doi.​org/​10.​1186/​
s43020-​022-​00091-1
Yin, P., Cisneros, I., Zhao, S., Zhang, J., Choset, H., & Scherer, S. (2023). isimloc: 
Visual global localization for previously unseen environments with 
simulated images. IEEE Transactions on Robotics, 39(3), 1893–1909. 
https://​doi.​org/​10.​1109/​TRO.​2023.​32382​01
Yan, X., Fu, T., Lin, H., Xuan, F., Huang, Y., Cao, Y., Hu, H., & Liu, P. (2023). Uav 
detection and tracking in urban environments using passive sensors: A 
survey. Applied Sciences, 13(20), 11320. https://​doi.​org/​10.​3390/​app13​
20113​20
Ye, X., Song, F., Zhang, Z., Zhang, R., & Zeng, Q. (2023). Semi-aerodynamic 
model aided invariant kalman filtering for uav full-state estimation. 
arXiv preprint arXiv:​2310.​01844, https://​doi.​org/​10.​48550/​arXiv.​2310.​
01844
Yang, B., & Yang, E. (2021). A survey on radio frequency based precise 
localisation technology for UAV in GPS-denied environment. Journal 
of Intelligent & Robotic Systems, 103, 1–30. https://​doi.​org/​10.​1007/​
s10846-​021-​01500-4
Yin, J., Yan, F., Liu, Y., He, G., & Zhuang, Y. (2023). An overview of simultaneous 
localisation and mapping: towards multi-sensor fusion. International 
Journal of Systems Science, 55(3), 550–568. https://​doi.​org/​10.​1080/​
00207​721.​2023.​22824​09
Zibaei, E., & Borth, R. (2024). Building causal models for finding actual causes 
of unmanned aerial vehicle failures. Frontiers in Robotics and AI, 11, 
1123762. https://​doi.​org/​10.​3389/​frobt.​2024.​11237​62
Zhang, Y., Carballo, A., Yang, H., & Takeda, K. (2023). Perception and sensing 
for autonomous vehicles under adverse weather conditions: A survey. 
ISPRS Journal of Photogrammetry and Remote Sensing, 196, 146–177. 
https://​doi.​org/​10.​1016/j.​isprs​jprs.​2022.​12.​012
Zenz, A. (2024). Safety first: Analysing the problematisation of drones. Griffith 
Law Review, 32(3), 310–334. https://​doi.​org/​10.​1080/​10383​441.​2024.​
23039​37
Zhang, R., Hao, G., Zhang, K., & Li, Z. (2023). Unmanned aerial vehicle naviga‑
tion in underground structure inspection: A review. Geological Journal. 
https://​doi.​org/​10.​1002/​gj.​4763
Zhang, B., Ji, D., Liu, S., Zhu, X., & Xu, W. (2023). Autonomous underwater 
vehicle navigation: a review. Ocean Engineering, 273, 113861. https://​
doi.​org/​10.​1016/j.​ocean​eng.​2023.​113861
Zheng, Y., Xie, Y., & Li, J. (2023). Multi-UAV collaboration and imu fusion localiza‑
tion method in partial gnss-denied scenarios. IEEE Access. https://​doi.​
org/​10.​1109/​ACCESS.​2023.​32990​23
Zhao, S., Xiao, X., Pang, X., Wang, Y., & Deng, Z. (2024). Gravity matching 
algorithm based on backtracking for small range adaptation area. IEEE 
Transactions on Instrumentation and Measurement. https://​doi.​org/​10.​
1109/​TIM.​2024.​33501​39
Zhou, X., Yang, Q., Liu, Q., Liang, W., Wang, K., Liu, Z., Ma, J., & Jin, Q. (2024). 
Spatial-temporal federated transfer learning with multi-sensor data 
fusion for cooperative positioning. Information Fusion, 105, 102182. 
https://​doi.​org/​10.​1016/j.​inffus.​2023.​102182
Zhang, S., Zhao, S., An, D., Liu, J., Wang, H., Feng, Y., Li, D., & Zhao, R. (2022). 
Visual slam for underwater vehicles: A survey. Computer Science Review, 
46, 100510. https://​doi.​org/​10.​1016/j.​cosrev.​2022.​100510
Zhang, Q., Zhang, H., Lan, Z., Chen, W., & Zhang, Z. (2022). A dnn-based opti‑
cal aided autonomous navigation system for uav under gnss-denied 
environment. In: International Conference on Autonomous Unmanned 
Systems, pp. 3536–3547. https://​doi.​org/​10.​1007/​978-3-​031-​15753-3_​
283 . Springer
Zhang, J., Zhang, T., Liu, S., & Xia, M. (2024). A robust particle filter for ambigu‑
ous updates of underwater terrain-aided navigation. Mechatronics, 98, 
103133. https://​doi.​org/​10.​1016/j.​mecha​troni​cs.​2023.​103133
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub‑
lished maps and institutional affiliations.
