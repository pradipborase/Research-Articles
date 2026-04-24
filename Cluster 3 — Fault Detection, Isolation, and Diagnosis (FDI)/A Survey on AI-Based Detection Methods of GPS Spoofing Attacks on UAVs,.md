# A Survey on AI-Based Detection Methods of GPS Spoofing Attacks on UAVs,.pdf

## Page 1

Proceedings of 2024 IEEE 12th International Conference on Intelligent Systems (IS) 
1 
 
A Survey on AI-Based Detection Methods of GPS 
Spoofing Attacks on UAVs 
 
Abdallah AlAbidy*, Amr Zaben*, Osama M.F. Abu-Sharkh†, Haitham Ameen Noman† 
Department of Computer Engineering, King Abdullah II School of Engineering 
Princess Sumaya University for Technology 
Amman, Jordan 
abd20190520@std.psut.edu.jo, amr20190064@std.psut.edu.jo, osama@psut.edu.jo, h.ani@psut.edu.jo 
 
 
Abstract— Global Positioning System (GPS) spoofing attacks on 
unmanned aerial vehicles (UAVs) can cause severe consequences, 
including abnormal behavior, privacy breaches, safety hazards, 
financial losses, and national security risks. Hence, detecting and 
preventing GPS spoofing attacks on UAVs is paramount to 
ensure their safety and security. This survey paper explores the 
cutting-edge techniques based on artificial intelligence (AI) 
proposed in the literature for detecting GPS spoofing attacks on 
UAVs. We present an overview of the UAV navigation system 
and then delve into the concept of GPS spoofing, encompassing 
its various forms, such as soft and hard spoofing. Furthermore, 
we discuss the advantages of utilizing AI in developing detection 
methods compared to traditional approaches. Subsequently, we 
analyze the detection methods based on deep learning (DL) and 
machine learning (ML) proposed in the literature, evaluating 
their strengths and weaknesses whenever feasible. Our survey 
provides valuable insights for researchers and practitioners 
working in the fields of AI and UAV security with the target of 
developing more advanced and effective AI-based methods for 
GPS spoofing detection on UAVs. 
Keywords- drone; deep learning; machine learning; detection; 
GPS spoofing; unmanned aerial vehicle; UAV 
NOMENCLATURE 
AI 
 
Artificial Intelligence 
ANN 
         
Artificial Neural Network 
BiLSTM 
Bidirectional Long Short-Term Memory 
BOX-MLP 
BOX Multi-Layer Perceptron 
CART  
Classification and Regression Trees 
CBA 
 
CNN-BiLSTM-Attention 
CNN 
              Convolutional Neural Network 
DL 
 
Deep Learning 
DNN 
 
Deep Neural Network 
DoS 
 
Denial of Service 
GAN 
 
Generative Adversarial Network 
GNSS  
Global Navigation Satellite System 
GPS 
 
Global Positioning System 
GRU-RNN   Gated Recurrent Unit Recurrent Neural Network 
IDS 
Intrusion Detection System 
IF 
Isolation Forest 
IMU 
Inertial Measurement Unit 
INS 
Inertial Navigation System 
KNN 
K-Nearest Neighbor 
LIDAR Light Detection and Ranging 
LOF 
Local Outlier Factor 
I. 
 INTRODUCTION  
 Unmanned Aerial Vehicles (UAVs), often called drones, 
are aircraft that operate without a human pilot on board. A 
human operator can control those vehicles remotely or navigate 
independently based on predetermined flight paths. UAVs 
come in various sizes, ranging from small handheld models to 
large-scale aircraft. They are employed for various applications 
and can be equipped with different sensors and imaging 
devices to collect aerial data and capture photographs. 
Additionally, certain UAVs are specifically designed to 
transport specific payloads, such as weapons, supplies, or other 
types of equipment. 
In recent years, the use of UAVs has experienced 
significant growth, and they are gaining popularity across 
various industries. They can be used in a wide range of 
applications: Aerial photography and videography. UAVs 
equipped with high-quality cameras capture aerial images and 
videos for various purposes, such as cinematography, real 
estate, construction, surveying, and agriculture. Also, UAVs 
equipped with multispectral and hyperspectral sensors monitor 
crops and soil health, enabling farmers to make more informed 
decisions about their fields. In the same context, search and 
rescue UAVs equipped with thermal imaging and other sensors 
are used to locate missing persons and identify hazards in 
disaster zones, providing valuable information to rescue teams. 
Similarly, delivery services UAVs are being developed and 
tested for package delivery, especially in hard-to-reach areas, 
inspection, and maintenance. In this area, UAVs are used to 
inspect infrastructure such as power lines, bridges, and 
pipelines for damage and maintenance, reducing the need for 
human inspectors to work at heights or in dangerous 
environments.  
979-8-3503-5098-2/24/$31.00 ©2024 IEEE
2024 IEEE 12th International Conference on Intelligent Systems (IS) | 979-8-3503-5098-2/24/$31.00 ©2024 IEEE | DOI: 10.1109/IS61756.2024.10705273
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

2 
 
Nowadays, for security and surveillance, UAVs are used by 
law enforcement and military organizations for surveillance 
and monitoring of significant events, crowd control, and border 
surveillance; environmental monitoring, UAVs are used for 
environmental monitoring and conservation efforts, such as 
tracking wildlife populations and monitoring deforestation; 
mapping and surveying, UAVs equipped with Light Detection 
and Ranging (LIDAR) and photogrammetry sensors are used 
for mapping and surveying land areas for various purposes, 
such as urban planning and construction [1]. The above 
examples represent only a glimpse of what UAVs could 
accomplish. With ongoing technological advancements, it is 
expected that novel uses will emerge. Nonetheless, before 
UAVs can be broadly implemented, several hurdles exist, 
including ethical, privacy, and safety concerns. UAVs are also 
vulnerable to many cybersecurity attacks [2].  
Like all network-connected devices, UAVs are susceptible 
to cybersecurity attacks that compromise their safety and 
functionality. Here are some of the most common cybersecurity 
issues in UAVs: data security: UAVs may gather large 
amounts of data, which can be sensitive or confidential; 
malware and viruses, UAVs can be infected with malware or 
viruses, which can cause the UAV to malfunction or perform 
unintended actions; denial of service (DoS) attacks, attackers 
can overload UAV communication channels with data, causing 
the UAV to crash or lose connection with its operator; rogue 
UAVs, attackers can use UAVs as weapons or as 
reconnaissance tools to gather intelligence on targets; GPS 
spoofing, GPS is a critical component of UAV navigation, and 
attackers can manipulate the GPS signal to misdirect or even 
hijack the UAV and potentially cause harm. The latter attack is 
the primary concern of this paper. Most of the applications, as 
mentioned earlier, lie on the location of the UAV to provide the 
intended service. Therefore, it is of high importance to detect 
and mitigate such attacks. GPS spoofing attacks have been 
addressed intensively, in general, in autonomous vehicles and 
other applications. Some recent studies can be found in [3] – 
[4]. 
In this paper, we review and discuss some of the state-of-
the-art works in the literature that introduced methods to detect 
GPS spoofing attacks, specifically on UAVs. We explain the 
UAV navigation system and the types of GPS spoofing attacks 
that may occur on such systems. We also describe the 
differences between the AI-based and traditional-based 
detection approaches. In this paper, we mainly concentrate on 
the works that proposed AI-based methods since they use 
intelligent techniques to learn complex patterns in data and 
consequently may enhance the accuracy of GPS spoofing 
attack detection in complex scenarios. We aim to be both 
comprehensive and inclusive in this survey. We provide a 
comparative analysis to highlight the pros and cons of each 
proposed method in the literature. It is worth mentioning that 
we assume proper knowledge of the reader of ML and DL as 
we do not explain the algorithms or neural networks 
themselves in this paper but concentrate on their use in 
detecting spoofing attacks on UAVs. We aim from this work to 
provide valuable insights for researchers and practitioners 
working in the fields of AI and UAV security with the target of 
developing more advanced and effective AI-based methods for 
GPS spoofing detection on UAVs due to its widespread in 
many essential and critical applications as have been described 
before.  
The rest of the paper is organized as follows. The UAV 
cybersecurity threat model is discussed in Section II. The 
functionality of the UAV navigation system and the GPS 
spoofing attacks on UAVs are discussed in Section III.  The 
advantages of adopting AI algorithms in developing methods to 
detect GPS spoofing attacks on UAVs over the rest are 
discussed in Section IV.  State-of-the-art ML-based and DL-
based detection methods proposed in the literature are 
addressed in Sections V and VI, respectively. The findings are 
discussed in Section VII, and the paper is concluded in Section 
VIII. 
II. 
UAV CYBERSECURITY THREAT MODELS 
It is imperative to briefly discuss the general cybersecurity 
threat model applicable to UAVs and identify potential 
vulnerabilities. More elaborations on cybersecurity threat 
models can be found in many works in the literature, such as 
[5] – [8].  
Cybersecurity threat models for UAVs often categorize 
risks based on the layers of UAV architecture, communication, 
control systems, and payload systems. Each of these layers 
presents distinct vulnerabilities that can be exploited by 
adversaries. For instance, communication links between 
UAVs and ground control stations are particularly vulnerable 
to eavesdropping, signal spoofing, and jamming attacks. 
Researchers emphasize that intercepting or disrupting 
communication can lead to loss of operational control or 
misdirection of the UAV. The control systems of UAVs, 
including flight and mission control algorithms, are 
susceptible to attacks aimed at the software level. These 
systems rely heavily on the integrity of the data they receive, 
which could result in incorrect commands and potentially 
catastrophic outcomes if corrupted through malware or other 
forms of cyber attacks. Additionally, the payload systems, 
which may include cameras, sensors, or other data-collecting 
devices, can be compromised. This could lead to espionage, 
data theft, or manipulation of data, which is a significant threat 
in military and surveillance applications. Another potential 
vulnerability arises from the physical interfaces and 
maintenance ports on UAVs. Unauthorized access to these can 
allow attackers to bypass network security measures and 
directly manipulate UAV hardware and software.  
To effectively address and reduce the cybersecurity risks 
associated with UAVs, it is crucial to implement a multi-
layered security approach as advised by current threat models. 
This comprehensive strategy involves the deployment of 
robust, end-to-end encryption for all communication channels. 
Encryption serves as the first line of defense for protecting the 
integrity and confidentiality of data transmitted between 
UAVs and ground control stations. Implementing robust 
encryption protocols such as AES-256 shields UAV 
communications from eavesdropping and spoofing attacks. 
Additionally, conducting continuous and rigorous software 
testing is crucial to address vulnerabilities within UAV control 
systems. This includes regular updates and patches to fix any 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

3 
 
identified security gaps. Moreover, UAV software should 
undergo extensive testing phases, including penetration testing 
and vulnerability assessments, before deployment. These tests 
help to simulate potential attacks and identify weak points 
within the system’s software architecture. Moreover, physical 
security measures are as crucial as cyber defenses in 
protecting UAV systems. Secure access controls for physical 
interfaces prevent unauthorized access to UAV hardware. This 
involves the use of tamper-proof hardware modules, where 
critical components are sealed and shielded against physical 
tampering. Additionally, using biometric data, such as 
fingerprint recognition or retina scans, ensures that only 
authorized personnel have access to UAV maintenance ports 
and internal systems. Furthermore, the integration of advanced 
anomaly detection systems is essential; these systems monitor 
operations to detect any irregular activities that could indicate 
a security breach, providing the opportunity for quick 
defensive actions to mitigate potential threats. By monitoring 
network traffic and system behavior, these systems can detect 
deviations from normal operations, which may signify an 
ongoing attack or system compromise. AI algorithms enhance 
the sensitivity and accuracy of anomaly detection, enabling 
these systems to adapt and respond to new and sophisticated 
threats dynamically. Early detection through these systems 
allows for rapid response strategies, minimizing potential 
damage and reinforcing the UAV’s resilience against attacks. 
This multi-faceted approach is designed to enhance UAV 
operations' overall security and resilience. By integrating these 
security measures, UAV operators and manufacturers can 
fortify their systems against various cyber threats. 
In this paper, we emphasize one category of attacks, which 
are the GPS spoofing attacks on UAVs and their AI-based 
detection methods. We describe such attacks in the following 
section. 
III. 
GPS SPOOFING ATTACK ON UAVS 
Navigation systems on UAVs are critical for ensuring that 
the UAVs can fly safely and accurately. UAVs rely on either 
one of the following devices or a combination of them: GPS 
receivers, onboard motion sensors, and vision sensors to 
navigate through the airspace and reach their intended 
destinations. GPS positioning in the states is based on signals 
with codes sent by 24 satellites, which are located 20,192 km 
above the Earth and collected by GPS receivers. The orbital 
range of these 24 satellites around the Earth ensures that a 
GPS receiver is visible from at least four satellites anytime 
and anywhere [9]. A  GPS  receiver processes the codes 
received, from the satellites, which provide information about 
the time when the signal was transmitted and the location of 
the satellites. A mathematical method called trilateration is 
used to obtain the location of the receiver related to the 
intersection of three spherical surfaces, which represents the 
distances between a GPS receiver and three of the 24 satellites 
mentioned earlier. One of the most critical factors for the 
accuracy of GPS is the synchronization between the clock in 
the GPS receiver and the highly accurate atomic clocks in the 
GPS satellites. The signals that satellites send include the 
precise time at which the signal was transmitted. The receiver 
determines its distance from each satellite by calculating the  
 
Figure 1. GPS trilateration method to locate objects.  The different Rs (R1, 
R2, and R3) represent the radiuses of the coverage without time error 
corrections, while the Rs-ΔRs (R1-ΔR1, R2-ΔR2, R3-ΔR3) represent the 
radiuses of the coverage with time error corrections.   
time delay of the incoming signal. However, GPS receivers 
typically do not have atomic clocks due to their size and cost. 
This leads to errors in distance measurements due to slight 
inaccuracies in the receiver's clock. By using signals from at 
least four satellites, the GPS receiver can solve for its spatial 
coordinates in addition to the time error in its clock. 
Correcting this time error significantly improves the accuracy 
of the position calculation. This is illustrated in Fig. 1. 
Satellite-based GPS navigation may provide reasonably stable 
accuracy if enough GPS signals are tracked over the whole 
UAV mission. One drawback of using GPS alone in UAVs is 
its inability to provide accurate altitude measurements, which 
is essential for UAVs [10]. Hence, GPS functionality is 
enhanced through the integration with an Inertial Navigation 
System (INS). Basically, the system works by fusing sensory 
information taken from inertial sensors such as accelerometers 
and rotational sensors such as gyroscopes to continuously 
estimate the position and orientation of the UAV in real-time 
using computer algorithms. An INS needs to work on a 
significant growth in systematic errors when used alone due to 
the integration of different sources of sensor errors over time 
[11]. Utilizing an INS accompanied by a GPS receiver, the 
system provides position, velocity, and altitude navigation 
parameters with high data rates and good accuracy. Although 
the use of a GPS/INS solves the previously mentioned 
problems of using a GPS receiver or an INS separately, the 
integrated system fails to provide crucial information about the 
vertical distance and movement of a UAV relative to the 
ground, as stated in [10]. The use of a vision-based navigation 
system, which relies on vision sensors such as cameras, hyper-
spectral sensors, laser scanners, etc., integrated with the 
GPS/INS system could encounter the problem mentioned 
earlier. Vision-based navigation is mainly used to process a 
sequence of stereo imagery to determine the platform 
trajectory, which, therefore, solves the issue of the poorly 
determined platform trajectory by the GPS/INS system [10].  
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

4 
 
The primary component of the integrated navigation system 
responsible for directing UAVs in their intended direction is 
the GPS. However, GPS spoofing attacks, which generate 
counterfeit GPS signals, can manipulate the UAV's navigation 
system and consequently cause abnormalities in the UAV 
missions and behavior. The possible spoofing attack to 
mislead the GPS receiver is elucidated in the following. 
GPS spoofing attacks can be classified into two types, 
namely, soft and hard GPS spoofing, as discussed in [12]. Soft 
GPS spoofing involves transmitting a counterfeit signal at the 
same frequencies as the satellites involved in the positioning 
of the UAV. With some degree of synchronization and a 
transmitted power slightly higher than the power of the 
authentic GPS signal to match the authentic signal's power 
level, the GPS receiver is spoofed. In other words, for a soft 
GPS spoofing to be successful, the counterfeit signal must 
meet the following requirements: having the same power level 
as the authentic signal, transmitted at a distance within the 
antenna coverage of the threatened GPS receiver, and the 
delay time is analogous to the ones of the authentic signal. A 
hard GPS spoofing attack occurs when one or more of the 
requirements for soft GPS spoofing are not met. In this case, a 
jamming signal is created and transmitted at high power to 
disrupt the authentic signal. The jamming signal is transmitted 
at the same frequency as the authentic signal, causing the GPS 
receiver to lose the authentic signal and lock onto the jamming 
signal. 
The authors of [13] identify two types of GPS attacks with 
different levels of sophistication. Unauthenticated and 
authenticated GPS attacks. The former is typically carried out 
on civilians. Such attacks use unauthenticated signals, and 
hence, the attacker can create spoofing signals, change the 
content of the authentic GPS signals, and/or delay signals or 
send them ahead of time. On the other hand, authenticated 
GPS attacks target military UAVs that require sophisticated 
and expensive equipment to perform the attack. Attackers 
cannot 
produce 
military 
GPS 
signals, 
as 
they 
are 
authenticated, but can catch and relay signals, which may 
delay but not send signals ahead of time. According to the 
categories mentioned in [12], the authors of [14] considered 
the unauthenticated GPS attack as soft and the authenticated 
GPS attack as hard. 
GPS spoofing attacks on UAVs can manifest in a 
multitude of ways, each with its unique repercussions 
depending on the context.  Key impacts include unpredictable 
UAV behavior, invasion of privacy, compromised data 
integrity, safety concerns, critical mission disruption, financial 
implications, and national security threats. The extent of the 
impact of GPS spoofing attacks varies based on factors such 
as the UAV's type, its application, and the attack's context. 
While a minor deviation might be inconsequential in some 
missions, it can lead to critical outcomes in others, like 
military operations. Therefore, recognizing and mitigating 
such attacks is imperative for the operational integrity and 
security of UAVs and their applications. An illustration of a 
GPS spoofing attack is shown in Fig. 2.  
 
Figure 2. GPS spoofing attack illustration. 
 
The extent of the impact of GPS spoofing attacks varies 
based on factors such as the UAV's type, its application, and 
the attack's context. While a minor deviation might be 
inconsequential in some missions, it can lead to critical 
outcomes in others, like military operations. Therefore, 
recognizing and mitigating such attacks is imperative for the 
operational integrity and security of UAVs and their 
applications. 
An illustration of a GPS spoofing attack is shown in Fig. 2. 
The path AXB is the original predetermined trajectory or the 
desired trajectory, which is determined in real-time using a 
remote controller; on the other hand, the path AXC is the 
spoofed trajectory. At point X, the attacker performed a 
successful spoofing attack, where the UAV changed its 
direction toward the undesired destination. 
IV. 
AI-BASED VS. TRADITIONAL-BASED DETECTION 
APPROACHES 
Recently, many techniques have been adopted to detect 
anomaly behaviors of UAVs, in general, using intrusion 
detection systems (IDS). Some of them are traditional-based 
approaches, such as the works in [15] – [17], while others are 
AI-based approaches, such as the works in [18] – [46]. An IDS 
using AI can be called a learning-based approach and does not 
require the theoretical creation of an accurate formal system; 
this works by studying historical data to understand the 
system's behavior. Attacks on UAVs are random and 
unexpected; this makes the learning-based approach a fast, 
timely, and robust detection method. Moreover, when an 
attack happens, the outcome will significantly differ from the 
actual standard data. In that case, the AI IDS will allow the 
avoidance of attacks by promptly transmitting decision 
information to the UAV microprocessor. Nevertheless, IDS 
trained through AI can detect defects at the hardware level and 
software levels. The AI-based approaches can be categorized 
into ML and DL. ML is a broad domain that encompasses 
various algorithms and techniques  for  enabling  computers  
to  learn  from  and  make predictions or decisions based on 
data. These methods include, but are not limited to, logistic 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

5 
 
regression, decision trees, support vector machines, random 
forests, etc. ML detection methods rely on extracting 
handcrafted features from data, which are then used to train a 
model capable of making predictions. Deep learning, on the 
other hand, refers specifically to a class of machine learning 
that involves neural networks with many layers. DL 
techniques automate the feature extraction process, allowing 
these models to learn high-level abstractions in data directly 
from raw input. Therefore, while categorizing AI-based 
detection methods into ML and DL categories is technically 
accurate, it is essential to communicate that DL is a 
specialized, more advanced branch of ML. This distinction 
highlights the evolution from algorithms that require manual 
feature selection to more sophisticated models that learn to 
identify relevant features autonomously. The use of DL-based 
IDSs generally outperforms ML-based IDSs since the former 
uses intelligent techniques with feature extraction processes to 
learn complex patterns in data. Consequently, it may enhance 
the accuracy of GPS spoofing attack detection. However, 
untrained enough IDS can lead to higher percentages of 
missed detections or false positives, which can be avoided by 
proper training on large datasets. Also, a high computational 
load is placed on the UAV, which is not actually a drawback 
nowadays with the rapid advancements of powerful 
microcontrollers.  
Traditional approaches have been used to detect anomaly 
behaviors in UAVs, including GPS spoofing attacks, but they 
have been inefficient and require regular updating processes. 
The traditional-based approaches can be categorized into two 
types, namely, redundancy-based approaches and behavioral-
based approaches, as mentioned in [18]. The following 
discusses their limitations in the use of GPS spoofing attacks 
and, hence, the superiority of the AI-based approaches. 
Redundancy-based approaches [15], [16] often use extra 
hardware components to perform cross-checks and cross-
correlation of their status during runtime. For example, a dual 
receiver can be used in some cases to enable cross-correlation 
between the signals in the receivers, which also requires an 
additional communication link between the receivers. The 
redundancy-based approaches invariably add to the cost and 
complexity of an IDS. On the other hand, behavioral-based 
approaches [17] require a description of how a normal UAV 
operates implemented at the program level. If the UAV 
behaves differently, then an attack may occur without 
detection. A precise description of the UAV behavior is hard 
to predict as its behavior is generally stochastic and depends 
on the surrounding environment, so false positive detection is 
possible with high rates. 
V. 
ML-BASED DETECTION METHODS 
In this section, we discuss the various ML-based detection 
methods of GPS spoofing attacks introduced in the literature, 
specifically for UAVs. We discuss each of them in the 
following. We also summarize their findings in Table I. 
Jasim et al. proposed in [20] an ML-based system for 
UAVs that harnessed ML techniques to detect jamming and 
spoofing attacks. They utilized a UAV Attack Dataset [19], 
comprising various features including timestamp, valid, 
timestamp sample, thrust, hover_thrust_var, accel_innov, 
accel_innov_var, 
accel_innov_test_ratio, 
accel_noise_var 
(inputs of classification phase), and label (output of 
classification phase). These features were utilized to train and 
test their system. However, they conducted training and 
testing using an 80% and 20% split, respectively, which 
showed that it was the most effective approach compared to 
other splits. The authors proposed several classifiers, including 
K-Nearest Neighbor (KNN), Gradient Boosting, and Decision 
Tree, and evaluated their performance using different metrics. 
Among these classifiers, the Decision Tree model achieved 
outstanding results. The proposed Decision Tree exhibited an 
accuracy rate of 99.86% while achieving high recall, F1-score, 
and precision values of 99.93%, 99.92%, and 99.93%, 
respectively. With a low error rate of 0.14%, the Decision 
Tree model effectively detected spoofing attacks. Furthermore, 
the proposed Decision Tree showed efficient execution with a 
duration of 0.66 seconds. Future work may consider the 
utilization of alternative classifiers, such as random forest 
(RF) or support vector machine (SVM), to enhance system 
performance further.  
Manesh et al. focused in [21] on detecting GPS spoofing 
signals in UAVs using a supervised ML approach based on an 
artificial neural network (ANN). The authors presented their 
created dataset and investigated the effectiveness of different 
features, including pseudo-range, Doppler shift, and signal-to-
noise ratio (SNR), in accurately classifying GPS signals. They 
extensively analyzed five selected features: satellite number, 
carrier phase, pseudo-range, Doppler shift, and SNR. When 
comparing the efficiency of different features for detecting 
GPS spoofing signals, the authors employed a neural network 
architecture consisting of one input layer, one hidden layer 
with ten hidden nodes, and one output layer. Notably, when 
combining the features of the pseudo-range, Doppler shift, and 
SNR with other features, an accuracy of at least 98% is 
achieved. The work also examined the impact of the number 
of hidden neurons in one-hidden-layer and two-hidden-layer 
neural networks on the detection performance. Increasing the 
number of hidden neurons from 2 to 10 in the one-hidden-
layer network improves accuracy by 9.2%. However, after 
approximately 14 hidden neurons, the accuracy plateaus as the 
network becomes saturated. In contrast, the two-hidden-layer 
network achieved comparable accuracy with only six neurons 
(3 neurons in each hidden layer). The authors suggested future 
research directions, including exploring improved ML 
techniques, incorporating online learning in neural networks, 
and investigating unsupervised ML algorithms for classifying 
unlabeled data and clustering unknown received messages. 
Avgin et al. used in [22] the UAV attack dataset [19] to 
compare different classifiers, including Decision Tree, 
multilayer perceptron classifier (MLPC), KNN, and C-Support 
Vector. The authors employed RF as a feature extraction 
method. The primary objective of this research is to identify 
the ML algorithm that achieved the highest F-1 scores. The 
results revealed that the decision tree classifier exhibited the 
best performance with an accuracy of 88.16%, recall of 
99.05%, F-1 score of 78.56%, and precision of 79.44%. The 
authors emphasized the importance of increasing the F-1 score 
as a critical evaluation metric for detecting UAV attacks. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

6 
 
TABLE I. SUMMARY OF RESULTS FOR ML-BASED DETECTION METHODS OF GPS SPOOFING ATTACKS ON UAVS 
Ref. 
AI Method 
Additional 
Info. 
Dataset 
Evaluation Metrics 
 
 
AUC  
(%) 
 
 
Accuracy 
(%) 
 
 
Recall 
(%) 
 
 
F1- 
Score 
(%) 
 
 
Precision 
(%) 
 
MSE 
 
Detection 
Time 
 
 
Detection 
Rate (%) 
 
[20] 
KNN 
80% training 
20% testing 
UAV 
Attack 
Dataset 
- 
97.16 
97 
97.33 
97 
 
- 
- 
70% training 
30% testing 
- 
97.1 
- 
- 
- 
- 
- 
- 
60% training 
40% training 
- 
96.71 
- 
- 
- 
- 
- 
- 
Gradient 
Boosting 
80% training 
20% testing 
1.13 
98.87 
99 
99.66 
99 
 
- 
- 
70% training 
30% testing 
- 
98.12 
- 
- 
- 
- 
- 
- 
60% training 
40% training 
- 
98.49 
- 
- 
- 
- 
- 
- 
Decision Tree 
80% training 
20% testing 
0.14 
99.86 
99.93 
99.92 
99.93 
 
- 
- 
70% training 
30% testing 
- 
99.86 
- 
- 
- 
- 
- 
- 
60% training 
40% training 
- 
99.74 
- 
- 
- 
- 
- 
- 
[21] 
ANN 
- 
Developed 
- 
98.30 
- 
- 
- 
- 
- 
99.2 
[22] 
Decision Tree 
- 
UAV 
Attack 
Dataset 
- 
88.17 
99.05 
78.56 
79.44 
- 
- 
- 
MLPC 
- 
67.93 
98.72 
37.32 
51.78 
- 
- 
- 
KNN 
- 
94.83 
99.71 
70.40 
90.40 
- 
- 
- 
C-SVM 
- 
94.73 
99.73 
67.38 
90.21 
- 
- 
- 
[23] 
Linear 
Regression 
The following 
results are the 
average of 
K=5, 10, 15, 
and 20 (when 
K-folds are 
applied) 
 
Developed 
- 
51.5 
100 
49 
33 
- 
- 
- 
SVM 
Polynomial 
- 
94.5 
92 
95.50 
99 
- 
- 
- 
SVM Linear 
- 
52.5 
100 
49 
33 
- 
- 
- 
SVM rbf 
- 
92.5 
88 
95 
99 
- 
- 
- 
SVM Sigmoid 
- 
15.5 
19 
22.5 
32 
- 
- 
- 
Naïve Bayes 
- 
88.5 
74 
85 
99 
- 
- 
- 
Decision Tree 
- 
92.5 
89 
89.75 
91 
- 
- 
- 
RF 
- 
93.5 
89 
89.75 
95 
- 
- 
- 
[24] 
MOD 
- 
Developed 
- 
99.8 
- 
- 
- 
- 
- 
99.9 
WMOD 
- 
99.8 
- 
- 
- 
- 
- 
99.9 
Bagging 
- 
99.6 
- 
- 
- 
- 
- 
99.6 
Boosting 
- 
99.56 
- 
- 
- 
- 
- 
99.35 
Stacking 
- 
99.7 
- 
- 
- 
- 
- 
99.8 
[25] 
Gaussian Naïve 
Bayes 
- 
Developed 
- 
≈91 
- 
- 
- 
- 
- 
≈86 
CART 
- 
≈99.8 
- 
- 
- 
- 
- 
≈99.9 
LR 
- 
≈91 
- 
- 
- 
- 
- 
≈86 
RF 
- 
≈99.8 
- 
- 
- 
- 
- 
≈99.9 
LSVM  
- 
≈95 
- 
- 
- 
- 
- 
≈92 
ANN 
- 
≈95.9 
- 
- 
- 
- 
- 
≈96.1 
PCA 
- 
96.34 
- 
- 
- 
- 
- 
98.85 
K-means 
clustering 
- 
86.23 
- 
- 
- 
- 
- 
88.1 
Autoencoder 
- 
99.53 
- 
- 
- 
- 
- 
99.73 
[26] 
KNN 
- 
Developed 
- 
79.08 
- 
- 
- 
- 
- 
70.75 
Radius 
Neighbor 
- 
73.81 
- 
- 
- 
- 
- 
71.97 
Linear SVM 
- 
64.56 
- 
- 
- 
- 
- 
62.08 
C-SVM 
- 
91.85 
- 
- 
- 
- 
- 
88.86 
Nu-SVM 
- 
92.78 
- 
- 
- 
- 
- 
91.26 
[27] 
PCA+OCC 
- 
Developed 
- 
- 
- 
90.57 
- 
- 
- 
- 
 
 
 
 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

7 
 
Shafique et al. proposed in [23] a methodology that 
involves deploying  multiple ML  algorithms, including  
Decision  Tree, SVM with different kernels, Logistic 
Regression (LR), RF, and Naïve Bayes, for the proposed 
model. GPS signal characteristics, including jitter, jitter 
(absolute), jitter (local), jitter (RAP), jitter (ppq5), shimmer, 
shimmer (local), shimmer (dB), shimmer (apq3), shimmer 
(apq5), and frequency modulation, are used as features in the 
model to detect whether an attacker or a legitimate entity 
sends a signal. The authors collected their dataset specifically 
for this study. Following the analysis, SVM with the 
polynomial kernel was selected as the most suitable ML 
algorithm for the proposed work, providing better results than 
the other ML algorithms. Once the suitable ML algorithm was 
chosen, four different models (K-learning models) were 
developed using the K-fold validation method to enhance the 
model's performance and robustness. Soft and hard voting 
techniques were employed to assign class labels to unseen or 
test 
data. 
The 
extensive 
experiments 
and 
analyses 
demonstrated the proposed model's effectiveness, with 99% 
accuracy, 98% precision, 99% recall, and 98% F1-score. 
Furthermore, the paper suggests potential enhancements by 
incorporating DL algorithms or a combination of ML and DL 
algorithms, emphasizing integrating DL strategies with a 
CNN. 
The authors Khoei et al. proposed in [24] two innovative, 
dynamic 
selection 
strategies, 
dubbed 
metric-optimized 
dynamic (MOD) and weighted-metric-optimized dynamic 
(WMOD).  Typically, their methodology incorporated a 
unique one-stage ensemble feature selection approach that 
eliminates redundant or insignificant features, streamlining the 
detection process. The study conducted a comprehensive 
comparison of ten machine learning models, assessing their 
performance based on various metrics like accuracy, detection 
probability, false alarm probability, misdetection probability, 
and processing time. These dynamic techniques proved to 
surpass the traditional ensemble models, achieving remarkable 
outcomes. They achieved 99.6% accuracy, a 98.9% detection 
probability, a low false alarm rate of 1.56%, a misdetection 
rate of only 1.09%, and a swift processing time of merely 1.24 
seconds. The study's significance lies in its innovative feature 
selection approach, dynamic selection methods, and thorough 
comparative analysis. The work utilized a meticulously 
balanced dataset of real and spoofed GPS signals, which 
underwent extensive preprocessing, including null value and 
noise 
management, 
encoding, 
normalization, 
and 
hyperparameter tuning using Bayesian optimization. This 
rigorous approach ensures the reliability and robustness of the 
detection methods. In other work, Khoei et al. presented in 
[25] a performance analysis of supervised and unsupervised 
ML models for detecting GPS spoofing attacks. The optimal 
simulation environment was set for each model, which then 
concluded that the highest achiever out of the supervised and 
unsupervised models was classification and regression trees 
(CART); it had the highest accuracy and probability of 
detection out of all the models with almost 100%, as well as 
the best performance evaluation with the lowest processing 
time of 1.25s, training time of 1.14s, prediction time of 0.11s, 
and the smallest memory size of 142.6MiB.  
Aissou et al. proposed in [26] a detection method using 
instance-based learning models. Five models were evaluated, 
namely KNN, Radius Neighbor, Linear SVM, C-SVM, and 
Nu-SVM. Satellite signals were collected, and features were 
extracted using software-defined radio units. Simulations were 
performed on three types of GPS spoofing attacks (simplistic, 
intermediate, and sophisticated), and the performance of the 
models was compared. The results show that Nu-SVM 
outperforms the other models with 92.78% accuracy, 91.26% 
probability of detection, 6.02% probability of false alarm, and 
8.73% 
probability 
of 
misdetection. 
The 
model 
also 
demonstrated strong computational efficiency regarding 
memory usage and processing time. The authors discussed the 
limitations of existing techniques and highlighted the 
contributions of their work, including real-time feature 
extraction, 
attack 
simulation, 
feature 
selection, 
and 
performance investigation of the models. 
Whelan et al. proposed in [27] an approach that utilizes 
PCA and OCCs, allowing the use of flight logs for training 
data. The IDS, called MAVIDS, operates onboard the UAV 
within a resource-constrained agent device, enabling detection 
and potential mitigation even when communication to the 
ground control station is lost due to jamming. The authors 
discussed results focusing on GPS spoofing and jamming 
attacks using the F1-score as the primary metric, scoring 
90.57% against GPS spoofing attacks. 
Semanjski et al. proposed in [28] a method that utilizes 
cross-correlation monitoring and SVM classification. The data 
used for training and validation include synthetic and real-
world datasets comprising measurements from GNSS 
receivers. Correlation analysis and principal component 
analysis (PCA) are employed for variable selection and 
dimensionality reduction. The findings show the efficiency of 
the approach in detecting signal tampering and the uniqueness 
in the field of cyber threat analytics compared to the existing 
literature on the use of SVM-based approaches to detect 
GNSS signal tampering attempts. Furthermore, the authors 
highlighted the importance of prioritizing precise detection 
over mere success rates, emphasizing its criticality for safety-
critical applications. The performance measure used to 
evaluate the results was the detection success rate. The data 
revealed that the spoofing validation dataset achieved a 
success rate of 98.77%, while the meaconing validation 
dataset reached a success rate of 98.72%. 
VI. 
DL-BASED DETECTION METHODS 
Analogous to the previous section, we discuss in this 
section various DL-based detection methods of GPS spoofing 
attacks that were introduced in the literature, specifically for 
UAVs. Table II provides an overview of the results achieved 
through various DL methodologies. 
In [18], Galvan et al. developed a detection method using a 
CNN-based approach, leveraging inertial measurement unit 
(IMU) data within the flight control system. The authors 
trained the CNN model with anomalous data obtained from 
UAV simulators, a more cost-effective and safer alternative to 
using actual UAVs. Comparing this model against others, 
including LSTM, BiLSTM, CNN+LSTM, and ConvLSTM,  
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

8 
 
 TABLE II. SUMMARY OF RESULTS FOR DL-BASED DETECTION METHODS OF GPS SPOOFING ATTACKS ON UAVS
Ref. 
AI Method 
Additional 
Info. 
Dataset 
 
Evaluation Metrics 
 
 
AUC  
(%) 
 
 
Accuracy 
(%) 
 
 
Recall 
(%) 
 
 
F1- 
Score 
(%) 
 
 
Precision 
(%) 
 
MSE 
 
Detection 
Time 
 
 
Detection 
Rate (%) 
 
[18] 
CNN 
using an 
accelerometer, 
5 sec. time 
window & 
20% threshold 
level 
Developed 
88.1 
- 
- 
- 
- 
- 
- 
- 
LSTM 
- 
69.9 
- 
- 
- 
- 
- 
- 
- 
BiLSTM 
69.5 
- 
- 
- 
- 
- 
- 
- 
CNN + LSTM 
72.7 
- 
- 
- 
- 
- 
- 
- 
ConvLSTM 
79.3 
- 
- 
- 
- 
- 
- 
- 
[29] 
Conv 
Autoencoder 
- 
UAV 
Attack 
Dataset 
100 
99.75 
99.5 
98.51 
97.65 
- 
- 
- 
LSTM 
Autoencoder 
100 
99.72 
97.88 
98.33 
99.06 
- 
- 
- 
Denoising 
Autoencoder 
100 
99.35 
99.67 
96.38 
95.04 
- 
- 
- 
OC-SVM 
70.37 
93.6 
61.94 
61.97 
62.63 
- 
- 
- 
LOF 
92.47 
79.49 
79.77 
55.43 
56.12 
- 
- 
- 
IF 
95.03 
98 
80.08 
78.96 
79.18 
- 
- 
- 
[30] 
CNN 
- 
Developed 
- 
- 
97 
99 
100 
- 
- 
- 
[31] 
 
MVSK-MLP 
- 
Developed 
- 
92 
- 
- 
- 
0.06 
- 
- 
BOX-MLP 
- 
90 
- 
- 
- 
0.075 
- 
- 
WD-MLP 
- 
93 
- 
- 
- 
0.05 
- 
- 
[32] 
CNN 
- 
Developed 
- 
88 
80 
86 
95 
- 
- 
- 
[33] 
 
CNN 
500Hz 
doppler shift 
step and 0.5 
chip 
Developed 
- 
- 
- 
- 
- 
- 
0.0648ms 
>96 
GAN 
500Hz 
doppler shift 
step and 0.5 
chip 
- 
- 
- 
- 
- 
- 
0.2418ms 
> 95 
500Hz 
doppler shift 
step and >0.5 
chip 
- 
- 
- 
- 
- 
- 
- 
> 98 
Residual Signal 
Detection 
500Hz 
doppler shift 
step and 0.25 
chip 
- 
- 
- 
- 
- 
- 
0.0923ms 
- 
[34] 
STL with 
Multiclass 
SVM 
- 
Developed 
 
 
- 
94 
- 
- 
- 
- 
- 
- 
Multiclass 
SVM 
- 
78 
- 
- 
- 
- 
- 
- 
[35] 
 
LSTM binary 
classifier 
UAV-
Generalized 
Detectors 
Developed 
- 
97.79 
97.79 
97.81 
97.89 
- 
- 
- 
LSTM-Auto-
encoder OCC 
- 
94.98 
94.93 
94.93 
95.03 
- 
- 
- 
LSTM binary 
classifier 
UAV-Specific 
(Average 
- 
98.06 
- 
- 
- 
- 
- 
- 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

9 
 
LSTM-Auto-
encoder OCC 
value of all 
UAV models) 
- 
97.74 
- 
- 
- 
- 
- 
- 
[36] 
ANN 
- 
UAV 
Attack 
Dataset 
- 
91.68 
- 
- 
- 
- 
- 
- 
Naïve Bayes 
- 
87.26 
- 
- 
- 
- 
- 
- 
[37] 
 
RNN 
Highway 
scenario,  
4 layers with 
16 neurons 
Developed 
- 
98 
- 
- 
- 
0.0031 
- 
- 
RNN 
Smart city 
scenario, 
3 layers with 
16 neurons 
- 
- 
- 
- 
- 
0.0066 
- 
- 
LSTM-RNN 
Smart city 
scenario, 
4 layers with 
32 neurons 
- 
98.7 
- 
- 
- 
0.0097 
- 
- 
GRU-RNN 
 
Smart city 
scenario, 
4 layers with 
32 neurons 
- 
98.5 
- 
- 
- 
0.0097 
- 
- 
[38] 
LSTM 
- 
Developed 
- 
78 
- 
- 
- 
- 
3-5s 
- 
[39]  
LSTM 
- 
MAVLINK 
- 
99.93 
85.71 
92.31 
100 
- 
- 
- 
TEXTBAT 
- 
82.1 
75.58 
82.59 
91.04 
- 
- 
- 
SVM 
MAVLINK 
- 
96 
- 
95.99 
- 
- 
- 
- 
TEXTBAT 
- 
82.3 
- 
83.25 
- 
- 
- 
- 
MLP 
MAVLINK 
- 
99.93 
85.71 
92.29 
99.96 
- 
- 
- 
TEXTBAT 
- 
83.23 
67.14 
82.79 
87.07 
- 
- 
- 
RF 
MAVLINK 
- 
89.33 
- 
89.21 
- 
- 
- 
- 
TEXTBAT 
- 
56.77 
- 
47.52 
- 
- 
- 
- 
[40] 
 
ResNet 
- 
Developed 
- 
94.8 
97.9 
95.4 
93 
- 
- 
- 
SqueezeNet 
- 
89 
93.6 
90.3 
87.1 
- 
- 
- 
[41] 
LSTM 
Autoencoder 
- 
Developed 
- 
- 
96 
- 
- 
- 
- 
- 
[42] 
CNN 
- 
Developed 
- 
- 
- 
 
 
 
160us 
92.1 
LSTM 
- 
- 
- 
 
 
 
692us 
91.4 
BP 
- 
- 
- 
 
 
 
54us 
96.2 
SVM 
- 
- 
- 
 
 
 
- 
88.2 
CBA 
- 
- 
- 
 
 
 
367us 
99.1 
BiLSTM 
- 
- 
- 
 
 
 
- 
90.4 
CNN-BiLSTM 
- 
- 
- 
 
 
 
- 
92.8 
CNN-Attention 
- 
- 
- 
 
 
 
- 
87.6 
BiLSTM-
Attention 
- 
- 
- 
- 
- 
- 
- 
95.4 
, they utilized the receiver operating characteristic (ROC) 
curve for effectiveness assessment. The CNN model, 
especially with accelerometer data over a 5-second window 
and a 20% threshold, achieved an 88.10% AUC in detecting 
GPS spoofing. 
Fraser et al. proposed in [29] a CNN model incorporating 
autoencoders to identify GPS spoofing and other attacks in 
digital twin technology, using the UAV Attack Dataset [19] 
and analyzing 88 features. This model was compared with a 
one-class support vector machine (OC-SVM), isolation forest 
(IF), local outlier factor (LOF), denoising autoencoder, and 
LSTM autoencoder. Notably, the CNN autoencoder surpassed 
the LSTM variant in computational efficiency and delivered 
exceptional 100.00% AUC, 99.75% accuracy, 99.50% recall, 
98.51% F1-score, and 97.65% precision.  
Sung et al. crafted in [30] a one-dimensional CNN model 
using residual network (ResNet) architecture for small UAVs' 
spoofing detection. This model, featuring nine convolutional 
layers, a pooling layer, and a fully connected layer, utilizes 
SNR-related features. It achieved the following results: 97% 
recall, 99% F1-score, and 100% precision. The one-
dimensional CNN's simplicity, coupled with its low 
computational demand and rapid detection capability, makes it 
a practical solution for embedding in UAVs for efficient 
spoofing attack detection. 
In [31], three distinct MLP algorithms (WD-MLP, MVSK-
MLP, BOX-MLP) were evaluated, focusing on UAV 
connections to varying base stations. Utilizing a real-world 
dataset, these models, with statistical path-loss-based features, 
were assessed for mean squared error (MSE) and accuracy. 
The WD-MLP showed superior results with over 93% 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

10 
 
accuracy and 0.05 MSE. Subsequently, the authors explored in 
[32] a CNN-based model for UAV monitoring and control, 
integrating mobile network assistance. This model, comprising 
two convolutional layers, a pooling layer, a flattened layer, 
and three fully connected layers, assessed path loss differences 
for performance evaluation. The CNN with transfer learning 
approach achieved 88% accuracy, 80% recall, 86% F1-score, 
and 95% precision, underlining the efficacy of combining 
CNN with transfer learning for cost-effective GPS spoofing 
detection in UAVs. 
 
Li et al. proposed in [33] a method for effectively detecting 
spoofing signals that are highly synchronized with authentic 
signals using a general adversarial network (GAN). The model 
was trained using the authors' dataset, and its detection 
performance was compared to that of a CNN model and a 
traditional residual signal detection method. Although the 
GAN had a shorter training time of 1.2285ms compared to the 
CNN, the CNN achieved a faster detection time of 0.0751ms 
for a Doppler shift step of 250Hz and a pseudocode phase 
difference between the spoofing signal and the authentic signal 
0.25 chip. However, given identical circumstances, the GAN 
performed slightly better than the CNN, achieving a detection 
probability of over 98%. Furthermore, the GAN outperformed 
the traditional residual signal detection method significantly.   
In [34], Arthur et al. developed a cutting-edge method 
based on deep reinforcement learning. This method utilizes a 
deep-Q network specifically for dynamically adjusting the 
flight paths of UAVs. The technique integrates Self-Taught 
Learning with a multiclass SVM, targeting the precise 
detection of GPS spoofing, particularly in unknown areas. The 
architecture of the model includes an input layer, a hidden 
layer, and an output layer, and it processes 200 distinct 
attributes. The model, trained in a simulated setting, achieved 
a 94% accuracy in identifying GPS spoofing attacks. This 
capability allows UAVs to either safely return to their base or 
move to a secure area when such threats are detected. 
Although the experiment was conducted in a simulated 
environment, the findings suggest strong potential for 
applying this method in real-world scenarios. 
Agyapong et al. investigated in [35] the performance of 
two algorithms based on LSTM for detecting UAV spoofing: 
one was an LSTM binary classifier, and the other was an 
LSTM autoencoder functioning as a one-class classifier. These 
algorithms underwent training with datasets created by the 
GAZEBO simulator and were evaluated on a range of UAV 
models, such as the Quadrotor and Typhoon H480, among 
others. The LSTM binary classifier, composed of several 
LSTM layers, dropout layers, a fully connected layer, and a 
Softmax layer, delivered good outcomes. It was particularly 
effective with the Quadrotor model, demonstrating a 97.79% 
recall rate, a 97.81% F1-score, a 97.89% precision rate, and a 
99.56% accuracy in detection. Additionally, the authors 
conducted a comparative analysis of these models' efficiency 
in a simulated environment and executed hardware validation 
tests using the Intel NCS2. 
In [36], Azaha et al. conducted a comparative analysis of 
the Naïve Bayes and ANN algorithms for efficient detection. 
They employed a publicly available dataset for this analysis. It 
was observed that the ANN model, composed of an input 
layer, a hidden layer, and an output layer, surpassed the Naïve 
Bayes in performance. The ANN model achieved an accuracy 
value of 91.68%, in contrast to the 87.26% accuracy of Naïve 
Bayes. Furthermore, the ANN demonstrated a reduced error 
rate, underscoring its enhanced effectiveness in identifying 
GPS spoofing attacks. 
Xiao et al. delved in [37] into the effectiveness of various 
recurrent neural network (RNN) models for GPS spoofing 
detection. They focused on different environments, including 
smart city and highway scenarios. The models evaluated 
included a basic RNN, a long short-term memory recurrent 
neural network (LSTM-RNN), and a gated recurrent unit 
recurrent neural network (GRU-RNN). It was found that each 
model's performance was optimized for specific scenarios. In 
the highway environment, the basic RNN model emerged as 
the most effective, whereas the LSTM-RNN showed superior 
performance in the smart city setting. The LSTM-RNN, 
designed with four layers and 32 neurons, registered an 
accuracy of 98.70% and an MSE of 0.0097 in the smart city 
scenario. In contrast, the basic RNN model, equipped with 16 
neurons, attained an accuracy of 98% and an MSE of 0.0031 
in the highway context. 
Wang et al. introduced in [38] a detection method that 
integrates an LSTM neural network with a Kalman filter, 
setting it apart from conventional methods that solely rely on 
the Kalman filter. This algorithm, developed through real-
world experiments, incorporates many features, including 
velocity and GPS coordinates. Its performance was assessed 
based on two key metrics: accuracy and detection speed. The 
algorithm achieved an accuracy of 78% and could detect 
issues within 3-5 seconds. However, a quicker detection time 
might be necessary for effective prevention of spoofing 
attacks.  
Jullian et al. embarked in [39] on a comparative analysis of 
Multilayer Perceptron (MLP) and LSTM models in their 
capacity to detect GPS spoofing attacks. They trained and 
evaluated these models on two distinct datasets, MAVLINK 
and TEXTBAT, utilizing features like GPS coordinates and 
position logs. The configuration of the MLP model included 
four hidden layers for MAVLINK and three for TEXTBAT. In 
contrast, the LSTM model was structured with three hidden 
layers for MAVLINK and two for TEXTBAT. The study 
revealed that the MLP model was more effective on the 
TEXTBAT dataset, achieving an accuracy of 82.23%, a 
precision of 87.07%, a recall rate of 67.14%, and an F1-score 
of 82.79%, thus surpassing the LSTM model. The MLP 
model's 
performance 
was 
further 
validated 
through 
comparative analyses with other algorithms, including 
Random Forest, SVM, and autoencoder. 
Xue et al. introduced in [40] DeepSIM, which employs 
ResNet for on-ground detection, and Squeeze Network 
(SqueezeNet) for on-board detection to compare the real-time 
location of the UAV with a satellite image of the same area. 
The authors also employed visual features from their 
SATUAV dataset in their model and used data augmentation 
techniques to improve the collected features. The authors 
concluded that the ResNet approach achieves high results with 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

11 
 
94.8% accuracy, 93.0% precision, 97.9% recall, 5.2% error 
rate, and 95.4% F1-score, which is far better than the 
SqueezeNet approach. The major disadvantage of DeepSIM is 
that it relies heavily on satellite imagery, which can be 
expensive and may only sometimes be available in real-time 
scenarios.  
Tlili et al. proposed in [41] an LSTM autoencoder using 
the UAV Attack Dataset [19]. The proposed approach 
achieved a high detection accuracy of 96%. However, a 
limitation of this paper is the need for more comparison with 
other existing methods, making it difficult to assess the 
effectiveness of the proposed approach compared to other 
state-of-the-art methods.  
In [42], Wu et al. introduced a novel technique for real-
time detection of drone spoofing attacks through the analysis 
of sensor data. They developed a sophisticated model called 
convolutional neural network (CNN) – bidirectional long 
short-term memory (BiLSTM) -Attention, also known as 
CBA, which was specifically designed to differentiate between 
DoS attacks and GPS spoofing accurately. This model 
surpassed various other classification methods, such as CNN, 
long short-term memory (LSTM), back-propagation, and 
SVM. An essential aspect of the proposed approach was the 
incorporation of the Shapley additive explanations (SHAP) 
technique, which greatly enhanced the transparency of the 
model's 
decision-making 
process, 
enabling 
a 
clearer 
understanding of how the model reached its conclusions. The 
effectiveness of this system was validated in scenarios 
involving both spoofing and DoS attacks, showcasing its 
versatility in combating different types of threats. The authors 
also emphasized the importance of carefully selecting UAV 
sensor data, particularly GPS data with specific characteristics. 
This careful selection helps optimize computational efficiency 
and ensures rapid detection of attacks. 
Whelan et al. compared in [43] three different algorithms, 
OC-SVM, LOF, and Autoencoder, to detect GPS spoofing as a 
typical example of an external sensor-based attack. They 
applied their algorithms on six different types of UAVs: 3DR 
IRIS+, Holybro S500, Yuneec H480, DeltaQuad VTOL, 
Standard Tailsitter, and Standard Plane. The obtained results 
show that the DeltaQuad VTOL using the autoencoder 
algorithm achieved the highest F1-score, 99.73%, while the 
3DR IRIS+, Holybro S500, and Yuneec H480 using the LOF 
algorithm 
achieved 
the 
highest 
recall 
value: 
100%. 
Furthermore, DeltaQuad VTOL and Standard Tailsitter, using 
the autoencoder algorithm, achieved the highest precision 
value: 87.728%. The authors considered the F1-score to 
determine the overall highest performer.  Based on the 
findings, it was concluded that the autoencoder is the preferred 
algorithm for this approach, with an average F1-score of 
94.81%. The OC-SVM and LOF algorithms showed average 
F1-scores of 81.17% and 58.93%, respectively. 
Park et al. proposed in [44] an IDS that utilizes an 
autoencoder, a deep neural network (DNN) of unsupervised 
learning, to detect GPS spoofing attacks on UAVs. The 
authors trained the model using only benign data from the 
UAV attack dataset [19] and considered the following 
features: location, position and orientation, IMU, and system 
status. The proposed model identifies an attack by detecting 
significant differences between reconstruction losses from the 
benign flight and the flight under attack. To prevent 
overfitting, the authors utilized L1 and L2 regularizes. They 
also applied batch normalization to the encoder and decoder 
and optimized parameters with Adam optimizer to ensure 
practical model training. The authors concluded that the 
proposed model requires minimal data labeling effort 
compared to ML-based models. 
Ahn et al. introduced in [45] an unsupervised one-
dimensional CNN model for detecting anomalies in UAVs 
using INS data. The dataset used in the paper consisted of 
actual INS data from x70 drones. To improve the model's 
performance, a PCA feature extraction method was employed, 
and the model architecture consisted of 6 hidden layers. The 
following features are considered in their analysis: Inertial 
Position and Velocity, Accelerometer, Gyroscope, Position, 
Navigation State, and Arming State. The authors highlighted 
the limitations of using a two-dimensional CNN model for 
INS data due to the lack of spatial relationships between 
columns of the used algorithm. A limitation of the work was 
the absence of a comparison between the proposed model and 
other DL models, as well as the lack of providing results to 
analyze the performance of the proposed work. 
VII. DISCUSSION 
Most of the addressed methods performed simulations to 
validate their proposed models, and hence, they may not fully 
capture the complexities and challenges of real-world 
scenarios. Most of the authors also developed their datasets, 
while few of them used a common dataset, such as the open-
source UAV Attack Dataset [19], as shown in Table I and 
Table II. Some datasets are more significant than others, and it 
is well known that the effectiveness of an AI-based algorithm 
depends heavily on the dataset.  
Moreover, the adopted performance metrics to evaluate the 
proposed models vary from one work to another, as discussed 
in the paper and are shown in Table I and Table II. It is worth 
mentioning that the choice of metric should depend on the 
specific operational scenario of UAV use. For example, in 
military applications where missing an attack could be 
catastrophic, recall and detection rate might be prioritized. In 
contrast, in commercial delivery services, where false alarms 
could disrupt operations and cause economic losses, precision 
might be more important. A balanced approach can also be 
adopted using a combination of metrics that provide a holistic 
view of system performance to accommodate various 
operational scenarios. Therefore, when providing a new 
detection method, it is important for the researcher to highlight 
how metrics they adopt reflect the operational priorities and 
risk management strategies in their work. 
It is also well-known that the complexity of AI-based 
algorithms and their computational load usually play a 
significant role in their performance. Most of the works should 
have reported the computational complexity of the proposed 
algorithms and their effect on the performance of the UAVs in 
real operational scenarios. Increasing the complexity of an 
algorithm to achieve better GPS spoofing attack detection 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

12 
 
capabilities may not be suitable to be used in UAVs, taking 
into consideration that the operation of UAVs faces many 
realistic constraints, such as the computational capabilities of 
the embedded system’s processor, the power consumption, 
and the on-board battery size, among others.  
Although many kinds of onboard motion sensors and vision 
sensors are used in the navigation systems of UAVs [10]-[11], 
the data they provide could have been more efficiently utilized 
in developing the detection methods of GPS spoofing attacks 
on UAVs in the literature. Many multi-sensor fusion detection 
methods for such attacks are introduced in the literature for 
Autonomous Vehicles. As UAVs are a type of Autonomous 
Vehicle but with more special operational constraints than the 
other types, these detection methods can be adopted and 
modified to suit the UAVs’ operational characteristics. 
 
VIII. CONCLUSION 
 
In conclusion, GPS spoofing attacks are significant threats 
to UAVs. Detecting and preventing such attacks is essential 
for their safety, security, and proper operation. In this paper, 
we provided an overview of the different types and levels of 
GPS spoofing attacks on UAVs, in addition to the AI-based 
methods that have been introduced in the literature to detect 
such attacks.  
We showed that DL and ML are promising approaches for 
detecting GPS spoofing attacks on UAVs, highlighting the 
reported results of the many works in the literature. AI-based 
algorithms can learn to recognize patterns and anomalies in 
GPS signals that are indicative of spoofing attacks and can 
provide real-time detection and prevention of such attacks. 
However, there are still many challenges that need to be 
addressed to make AI-based detection methods more effective 
and reliable, as discussed in Section VII. In summary, the need 
for a large and common dataset built from multiple scenarios 
to conclude which DL and ML algorithm is the best for 
detecting such attacks; the complexity of the used AI-based 
algorithms, especially for the DL-based detection methods, 
and their impact on the UAVs’ resources; the reflection of the 
adopted metrics on the operational priorities and risk 
management strategies; and the use of on-board sensors, both 
inertial and vision sensors, more effectively. Furthermore, 
while the addressed papers’ results show promise for UAV-
specific detection algorithms, it is essential to note that many 
of the validations were conducted in a simulated environment 
and not tested in real-world scenarios, which could limit the 
generalizability of the findings or their accuracy. 
An 
essential 
recommendation 
for 
researchers 
and 
developers is to adopt a common dataset and similar 
performance metrics to evaluate an AI-based algorithm when 
developing new GPS spoofing detection methods on UAVs. 
This will reflect the level of enhancement of the proposed 
method when compared to others.  
Overall, AI-based methods have great potential for enhancing 
the security and safety of UAVs against GPS spoofing attacks. 
Our survey provides a valuable resource for researchers 
working in this field. It inspires future work to introduce more 
advanced and effective methods for detecting GPS spoofing 
attacks on UAVs. It is also helpful for practitioners to deploy 
effective UAV security systems based on the summarized 
findings of the conducted research in the literature. 
 
REFERENCES 
[1]   M. Mozaffari, W. Saad, M. Bennis, Y. H. Nam and M. Debbah, "A 
Tutorial on UAVs for Wireless Networks: Applications, Challenges, and 
Open Problems," in IEEE Communications Surveys & Tutorials, vol. 21, 
no. 3, pp. 2334-2360, 2019. 
[2]   F. Alrefaei, A. Alzahrani, H. Song and S. Alrefaei, "A Survey on the 
Jamming and Spoofing attacks on the Unmanned Aerial Vehicle 
Networks," 2022 IEEE IEMTRONICS, Toronto, ON, Canada, 2022, pp. 
1-7. 
[3]  X. Wei and B. Sikdar, "Impact of GPS Time Spoofing Attacks on Cyber 
Physical Systems," 2019 IEEE ICIT, Melbourne, VIC, Australia, 2019, 
pp. 1155-1160. 
[4]  M. T. Arafin and K. Kornegay, "Attack Detection and Countermeasures 
for Autonomous Navigation," 2021 55th Annual Conference on 
Information Sciences and Systems (CISS), Baltimore, MD, USA, 2021, 
pp. 1-6. 
[5]  Javaid, A. Y., Sun, W., Devabhaktuni, V. K., & Alam, M. (2012). Cyber 
security threat analysis and modeling of an unmanned aerial vehicle 
system. In Proceedings of the 2012 IEEE Conference on Technologies 
for Homeland Security (HST), Waltham, MA, USA, November 2012, 
pp. 585-590. 
[6]  K. Singh and A. K. Verma, "Threat modeling for multi-UAV Adhoc 
networks," TENCON 2017 - 2017 IEEE Region 10 Conference, Penang, 
Malaysia, 2017, pp. 1544-1549 
[7]  W.I. Alluhybi, O.H. Alhazmi, "Towards a threat model for unmanned 
aerial vehicles," Intelligent Computing and Innovation on Data Science: 
Proceedings of ICTIDS 2021. Springer, Singapore, 2021. 
[8]  A. Spyros, "A study of cybersecurity threats in UAVs and threat model 
approaches,” M.S. thesis, School of Science and Technology, 
International Hellenic University, Thessaloniki, Greece, 2022.  
[9]  B. Hofmann-Wellenhof, H. Lichtenegger, and J. Collins, “Global 
positioning system: theory and practice,” Springer Science & Business 
Media, 2012. 
[10]   J. Wang, M. Garratt, A. Lambert, J. J. Wang, S. Han, and D. Sinclair, 
“Integration of GPS/INS/vision sensors to navigate unmanned aerial 
vehicles,” The International Archives of the Photogrammetry, Remote 
Sensing and Spatial Information Sciences, vol. 37, no. part B1, pp. 963–
969, 2008. 
[11]  R. Munguía, “A GPS-aided inertial navigation system in direct 
configuration”, Journal of applied research and technology, vol. 12, no. 
4, pp. 803–814, 2014. 
[12]  J. Noh et al., “Tractor beam: Safe-hijacking of consumer drones with 
adaptive GPS spoofing”, ACM Transactions on Privacy and Security 
(TOPS), vol. 22, no. 2, pp. 1–26, 2019. 
[13]   N. O. Tippenhauer, C. Pöpper, K. B. Rasmussen, and S. Capkun, “On 
the requirements for successful GPS spoofing attacks”, 18th ACM 
conference on computer and communications security, 2011, pp. 75–86. 
[14]  Sung YH, Park SJ, Kim DY, Kim S. “GPS Spoofing Detection Method 
for Small UAVs Using 1D Convolution Neural Network,” Sensors. 2022 
Jan, 22(23), p. 9412. 
[15]   Man-Ki Yoon, Bo Liu, Naira Hovakimyan, and Lui Sha. “Virtualdrone: 
Virtual sensing, actuation, and communication for attack-resilient 
unmanned aerial systems,” 2017 ACM/IEEE ICCPS, p.p. 143–154. 
[16]  F. Fei et al., “Cross-layer retrofitting of uavs against cyberphysical 
attacks,” 2018 IEEE ICRA, 2018, p.p. 550–557.  
[17]  R. Mitchell and I. Chen. “Adaptive intrusion detection of malicious 
unmanned air vehicles using behavior rule specifications,” IEEE 
Transactions on Systems, Man, and Cybernetics: Systems, 44(5), 2014, 
p.p. 593– 604. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

13 
 
[18]  J. Galvan, A. Raja, Y. Li and J. Yuan, "Sensor Data-Driven UAV 
Anomaly Detection using Deep Learning Approach," 2021 IEEE 
MILCOM, San Diego, CA, USA, 2021, pp. 589-594. 
[19]   J. Whelan, T. Sangarapillai, and O. Minawi, "UAV Attack Dataset," 
Feb. 2020. 
[20]   K. S. Jasim, K. M. Ali Alheeti, and A. K. A. Najem Alaloosy, 
“Intelligent Detection System for Spoofing and Jamming Attacks in 
UAVs,” International Conference on Cybersecurity, Cybercrimes, and 
Smart Emerging Technologies, 2022, pp. 97–110. 
[21]  M. R. Manesh, J. Kenney, W. C. Hu, V. K. Devabhaktuni and N. 
Kaabouch, "Detection of GPS Spoofing Attacks on Unmanned Aerial 
Systems," 2019 16th IEEE CCNC, Las Vegas, NV, USA, 2019, pp. 1-6. 
[22]   H. Y. Avgin, “GPS Spoofing Attack Detection in Drone Using Machine 
Learning”, Southern University and Agricultural and Mechanical 
College, 2021. 
[23]  A. Shafique, A. Mehmood and M. Elhadef, "Detecting Signal Spoofing 
Attack in UAVs Using Machine Learning Models," IEEE Access, vol. 9, 
pp. 93803-93815, 2021. 
[24]  T. Talaei Khoei, S. Ismail, and N. Kaabouch, “Dynamic selection 
techniques for detecting GPS spoofing attacks on UAVs,” Sensors, vol. 
22, no. 2, p. 662, 2022. 
[25]  T. T. Khoei, A. Gasimova, M. A. Ahajjam, K. A. Shamaileh, V. 
Devabhaktuni, and N. Kaabouch, "A Comparative Analysis of 
Supervised and Unsupervised Models for Detecting GPS Spoofing 
Attack on UAVs," 2022 IEEE eIT, Mankato, MN, USA, 2022, pp. 279-
284. 
[26] G. Aissou, S. Benouadah, H. El Alami and N. Kaabouch, "Instance-
based Supervised Machine Learning Models for Detecting GPS 
Spoofing Attacks on UAS," 2022 IEEE 12th CCWC, Las Vegas, NV, 
USA, 2022, pp. 0208-0214. 
[27]  J. Whelan, A. Almehmadi, and K. El-Khatib, “Artificial intelligence for 
intrusion detection systems in Unmanned Aerial Vehicles,” Computers 
and Electrical Engineering, vol. 99, p. 107784, 2022. 
[28] S. Semanjski, I. Semanjski, W. De Wilde, and A. Muls, “Use of 
supervised machine learning for gnss signal spoofing detection with 
validation on real-world meaconing and spoofing data—part I”, Sensors, 
vol. 20, no. 4, p. 1171, 2020. 
[29]  B. Fraser, S. Al-Rubaye, S. Aslam and A. Tsourdos, "Enhancing the 
Security of Unmanned Aerial Systems using Digital-Twin Technology 
and Intrusion Detection," 2021 IEEE/AIAA 40th DASC, San Antonio, 
TX, USA, 2021, pp. 1-10. 
[30]  Y.-H. Sung, S.-J. Park, D.-Y. Kim, and S. Kim, "GPS Spoofing 
Detection Method for Small UAVs Using 1D Convolution Neural 
Network", Sensors, vol. 22, no. 23, p. 9412, 2022. 
[31] Y. Dang, C. Benzaïd, B. Yang and T. Taleb, "Deep Learning for GPS 
Spoofing Detection in Cellular-Enabled UAV Systems," 2021 NaNA, 
Lijiang City, China, 2021, pp. 501-506. 
[32]  Y. Dang, C. Benzaïd, T. Taleb, B. Yang, and Y. Shen, "Transfer 
Learning based GPS Spoofing Detection for Cellular-Connected UAVs," 
2022 IWCMC, Dubrovnik, Croatia, 2022, pp. 629-634. 
[33]  J. Li, X. Zhu, M. Ouyang, W. Li, Z. Chen and Q. Fu, "GNSS Spoofing 
Jamming Detection Based on Generative Adversarial Network," IEEE 
Sensors Journal, vol. 21, no. 20, pp. 22823-22832, Oct.15, 2021. 
[34]  M. P. Arthur, "Detecting Signal Spoofing and Jamming Attacks in UAV 
Networks using a Lightweight IDS," 2019 CITS, Beijing, China, 2019, 
pp. 1-5. 
[35]  R. A. Agyapong, M. Nabil, A. R. Nuhu, M. I. Rasul and A. Homaifar, 
"Efficient Detection of GPS Spoofing Attacks on Unmanned Aerial 
Vehicles Using Deep Learning," 2021 IEEE SSCI, Orlando, FL, USA, 
2021, pp. 01-08. 
[36]  N. A. W. Azaha and S. K. A. Khalid, "A Comparative Study of Drone 
GPS[ Spoofing Detection Algorithm Between Naïve Bayes and 
Artificial Neural Network", Applied Information Technology And 
Computer Science, 2021, vol. 2, no. 2, pp. 141–154. 
[37] K. Xiao, J. Zhao, Y. He, C. Li, and W. Cheng, "Abnormal Behavior 
Detection Scheme of UAV Using Recurrent Neural Networks," in IEEE 
Access, vol. 7, pp. 110293-110305, 2019. 
[38]  S. Wang, J. Wang, C. Su, and X. Ma, "Intelligent Detection Algorithm 
Against UAVs' GPS Spoofing Attack," 2020 IEEE 26th ICPADS, Hong 
Kong, 2020, pp. 382-389. 
[39]  O. Jullian, B. Otero, M. Stojilović, J. J. Costa, J. Verdú, and M. A. 
Pajuelo, "Deep Learning Detection of GPS Spoofing," 7th International 
Conference in Machine Learning, Optimization, and Data Science, 
Grasmere, UK, 2021. 
[40]  N. Xue, L. Niu, X. Hong, Z. Li, L. Hoffaeller, and C. Pöpper, “Deepsim: 
Gps spoofing detection on uavs using satellite imagery matching,” 
Annual computer security applications conference, 2020, pp. 304–319. 
[41]  F. Tlili, S. Ayed, L. Chaari, and B. Ouni, “Artificial intelligence based 
approach for fault and anomaly detection within uavs,” 36th AINA-
2022, Volume 1, 2022, pp. 297–308. 
[42] S. Wu, Y. Li, Z. Wang, Z. Tan, and Q. Pan, "A Highly Interpretable 
Framework for Generic Low-Cost UAV Attack Detection," IEEE 
Sensors Journal, vol. 23, no. 7, pp. 7288-7300, 1 April 1, 2023. 
[43]  J. Whelan, T. Sangarapillai, O. Minawi, A. Almehmadi, and K. El-
Khatib, “Novelty-based intrusion detection of sensor attacks on 
unmanned aerial vehicles,” 16th ACM symposium on QoS and security 
for wireless and mobile networks, 2020, pp. 23–28. 
[44] K. H. Park, E. Park, and H. K. Kim, “Unsupervised intrusion detection 
system for unmanned aerial vehicle with less labeling effort,” 21st 
International Conference on Information Security Applications, WISA, 
Jeju Island, South Korea, 2020, pp. 45–58. 
[45]  H. Ahn, "Deep Learning based Anomaly Detection for a Vehicle in 
Swarm Drone System," 2020 ICUAS, Athens, Greece, 2020, pp. 557-
561. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:23:23 UTC from IEEE Xplore.  Restrictions apply.
