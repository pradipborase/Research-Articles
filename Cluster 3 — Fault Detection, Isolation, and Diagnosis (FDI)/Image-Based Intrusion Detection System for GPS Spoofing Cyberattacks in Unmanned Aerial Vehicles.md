# Image-Based Intrusion Detection System for GPS Spoofing Cyberattacks in Unmanned Aerial Vehicles.pdf

## Page 1

1
Image-based Intrusion Detection System for GPS
Spoofing Cyberattacks in Unmanned Aerial Vehicles
Mohamed Selim Korium, Ahmed Mahmoud Ahmed, Mohamed Saber, Arun Narayanan, and Pedro H. J. Nardelli.
Abstract—The operations of unmanned aerial vehicles (UAVs)
are susceptible to cybersecurity risks, especially because of their
strong reliance on the Global Positioning System (GPS) and radio
frequency (RF) sensors. GPS and RF sensors are vulnerable to
potential threats such as spoofing attacks that can cause the
UAVs to behave erratically. Since these threats are widespread
and potent, it is imperative to develop effective intrusion detection
systems. In this paper, we present a deep learning-based method-
ology for detecting GPS spoofing cyberattacks. We combine
convolutional neural networks with transfer learning to design
a method that is fast, accurate, and general. The effectiveness
of the proposed solution is demonstrated by extensive numerical
experiments carried out using benchmark datasets. We achieved
an accuracy of 100% within a running time of 120.64 s and a
detection time of 2.035 s in the case of the training dataset.
Further, using this trained model, we achieved an accuracy
of 99.25% within a detection time of 2.721 s on an unseen
dataset that was unrelated to the one used for training the
model. Our results demonstrate that the proposed Image-based
intrusion detection method outperforms the existing solutions
while providing a general model for detecting cyberattacks
included in unseen datasets.
Index Terms—Unmanned aerial vehicles, CNN architectures,
Transfer learning, Learning and loss curves
I. INTRODUCTION
A. Background
Unmanned aerial vehicles (UAVs), commonly referred to as
drones, are aircraft that fly automatically without any human
pilot, crew, or passengers on board. UAVs were originally
employed for military tasks, such as surveillance, bomb de-
tection, delivery of armed payloads, and various missiles,
such as AGM-114 Hellfire used by the United States [1].
In recent times, UAVs have also attracted significant interest
from civilian industries for their potential applications for
various civil requirements such as entertainment, inspection,
surveillance, and mapping, assistance during natural disasters,
and intelligent urban traffic control [2]. Further, according to
some studies [3], [4], the market value of UAVs is expected
to reach $1.85 billion by the year 2024.
Most civilian tasks rely heavily on the radio frequency
(RF) band that enables data transmission, such as real-time
video streaming, sensor data [5], and signals received from
the Global Navigation Satellite System (GNSS) that provides
positioning, navigation, and timing services [6]. Examples of
MSK, AN, and PHJN are with Lappeenranta–Lahti University of Technol-
ogy, Finland. AMA is with Zagazig University. This paper is partly supported
by: (i) Research Council of Finland (former Academy of Finland) via (a)
EnergyNet Fellowship n.321265/n.328869; and (b) X-SDEN project n.349965;
and (ii) by Jane and Aatos Erkko Foundation via STREAM project. Contact:
mohamed.korium@lut.fi
a GNSS include Global Positioning System (GPS) owned
by the United States, Global Navigation Satellite System
(GLONASS) owned by Russia, Galileo Global Navigation
Satellite System owned by the EU, and Quasi-Zenith Satellite
System owned by Japan.
However, modern improvements in the connectivity of UAV
networks for executing tasks have significantly increased the
cybersecurity risks. This is due to the fact that UAVs primarily
rely on GPS and RF sensors that are easily exposed to potential
cybersecurity threats, such as spoofing attacks [7]. In a spoof-
ing attack, counterfeit GPS signals control the command func-
tions and steal sensitive data by replacing the GPS signals with
a false signal that mimics the GPS format, causing the UAV
to be set to a wrong trajectory [8]. There are several examples
of spoofing attacks occurring in the real world. Researchers at
the University of Texas took control of an $80 million yacht
in the Mediterranean Sea by changing the trajectory of the
yacht for about 100 m [9]. Iranian forces successfully spoofed
a U.S. Lockheed Martin RQ-170 Sentinel UAV, forcing it
to change its destination to Iran in December 2011 [10].
Researchers at Virginia Tech, China, and Microsoft changed
the destination of an autonomous vehicle by manipulating the
navigation system using their own-built $225 GPS spoofer in
2018 [11]. These studies were investigating the vulnerability
of GPS systems to spoofing attacks by using software-defined
radios (SDRs), which encompass many devices, such as High
Amplitude Complex Keying Radio Frequency One (HackRF
One), Great Scott Gadgets HackRF software-defined radio
(HackRF), Universal Software Radio Peripheral (USRP), and
Analog devices Active Learning Module - Pluto (ADALM-
Pluto) [12]. SDR devices are a type of radio communication
system that receive and generate signals using software by
converting signals into RF signals (GPS signals) on a general-
purpose computer instead of traditional hardware components
like filters and amplifiers, making them more adaptable and re-
configurable for attackers compared with traditional hardware
components [12]. To conduct a GPS spoofing attack by using
an SDR device, the cyber-malicious agent (i) first identifies the
authentic GPS signal that the UAV receives; (ii) uses a GPS
signal simulator like the Global Position System–Software-
Defined Radio simulator (GPS-SDR-SIM) [13] or the Global
Navigation Satellite System–Software-Defined Radio Library
(GNSS-SDRLIB) software [14] to parse the CSV file created
by the cyber-malicious agent that holds the spoofed location
and number of movements in the Earth-centered, Earth-fixed
coordinate system (ECEF) format; (iii) employs the SDR
device to convert the GPS baseband signal data streams created
by the GPS signal simulator into GPS signals (the desired
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 2

2
signal by the hacker); and (iv) transmits the spoofed GPS by
the SDR to the UAV after adjusting the frequency and the
signal power. As a result, the UAV will lose the authentic GPS
signal that indicates the true location and time and will lock
onto the spoofed GPS signal in 15 to 300 s depending on the
embedded algorithms and the chosen spoofed GPS strategy.
Therefore, GPS spoofing has severe effects on applications that
depend on synchronization (accurate positioning and timing).
B. Related research, its limitations, and our contribution
In the context of UAV cyberattacks, previous studies have
focused on conventional methods of signal processing and
cryptography to analyze and defend against a spoofing GPS
attack: (i) the cryptography technique involves encrypting the
satellite codes received and sent by the GPS receiver. This
technique requires a public key to decrypt the encrypted code;
a digital signature to verify the authenticity and integrity of
the code; a key management system to generate the pub-
lic and private keys; and a secure communication protocol
to grant the authenticity and integrity transmission of the
encrypted and signed code by a digital signature between
the satellites and the GPS receiver. However, this technique
has a substantial cost: it adds complexity and may not be
compatible with older versions of receivers and signals; (ii)
the signal distortion detection technique tries to find any
anomalies by monitoring the quality and characteristics of the
GPS signal. The technique is implemented by measuring the
strength of the signal and the frequency compared with GPS
signals under normal conditions; however, it cannot detect
complicated spoofing attacks that could seamlessly shift to the
GPS receiver without any abrupt changes or errors; and (iii) the
direction-of-arrival sensing technique uses multiple antennas
to estimate the original GPS signal direction and compares it
with the authentic GPS signal direction or the known direction
of the satellites. The drawback of this technique is that it is
affected by environmental factors that may block the GPS
signals [15]–[17].
Kwon et al. [18] used the probability density function
(PDF) to evaluate the accelerometer reading from an inertial
measurement unit (IMU) to detect a GPS spoofing attack. The
proposed method is carried out by monitoring the difference
in the accelerometer readings under standard authentic GPS
signals and spoofed GPS signals.
In [19], [20], the authors used the outputs of accelerometers
that measure linear acceleration and the results of onboard
gyroscopes that measure angular velocity or rotation rate, re-
spectively. Both studies compare the outputs of IMU measure-
ments that are computed from both the UAV and the GPS to
determine whether the outputs are match. If the outputs of the
IMU measurement do not match the GPS outputs, it indicates
that the GPS is spoofed. However, IMU measurements are
prone to various errors, such as bias and noise, that may affect
the measurements of angular rate and acceleration, which are
integrated into the inertial navigation system (INS). This error
accumulation results in an inaccurate state of the UAV, making
it hard to distinguish between standard authentic GPS signals
and spoofed GPS signals [21].
Other studies [22], [23] have suggested that using artificial
intelligence (AI) algorithms may have some advantages over
all of the above techniques because the algorithms may gain
experience from diverse spoofed GPS scenarios. In [24],
the authors proposed a Long Short-Term Memory (LSTM)
algorithm to detect GPS spoofing attacks by predicting Un-
manned Aircraft System (UAS) paths and comparing them
with the authentic GPS positioning signal. This comparison
allows the algorithm to confirm whether the UAS is following
an authentic or a spoofed trajectory. Although the detection
accuracy of the proposed model reached 78%, the method
is not applicable if the UAV shifts smoothly to the spoofed
GPS with a small error deviation compared with the accepted
threshold that the cyber-malicious agent has predefined.
Semanjski et al. [25] used a known supervised learning
algorithm, C-Support Vector Machine (C-SVM), to detect GPS
spoofing attacks depending on the features of the receiver
clock that synchronizes with the satellites to determine the
location of the UAV in real time. This allowed the authors
to monitor the behavior of the receiver clock during both
authentic and spoofed GPS signals. They claimed that the
cross-validation accuracy of the C-SVM model and the overall
accuracy were 97.8% on real-world data. However, they did
not mention how they handled imbalanced datasets. Moreover,
in their study, the GPS spoofing attack is an unusual occur-
rence, and thus, the number of normal samples is much higher
than the malicious samples. As a result, since the C-SVM is
very sensitive to imbalanced datasets, the model may have
a high overall accuracy but perform inaccurately on minor
classes.
In [26], the authors employed the Multilayer Perceptron
model (MLP) to detect GPS spoofing attacks by using path loss
measurements collected from nearby cellular base stations.
Their model achieved an accuracy of 80% with one base
station and 93% with three base stations. However, this method
relies on the cellular network, which, itself, could be jammed,
affecting the path loss measurements and leading to inaccurate
detection. Moreover, UAVs are used to perform in high-risk
environments, and there may be issues with cellular network
connectivity in urban or dead zone areas.
Whelan et al. in [27] and [28], used anomaly detection
models such as one-class support vector machine, local outlier
factor, and autoencoder to detect GPS spoofing and jamming
based on their proprietary dataset named UAV Attack Datasets.
The models were trained on flight data only (no attacks occur)
to recognize normal behavior, allowing the proposed models
to detect any deviation to be flagged as a cyberattack. The
performance of their models achieved macro-averaged F1-
score of 90.57% and 94.3% for GPS spoofing and jamming
respectively.
Thus, the existing traditional signature-based detection
strategies and intrusion detection systems (IDSs) presented
above have the following limitations: (i) many of these studies
do not mention how to handle imbalanced datasets; (ii) most
of the studies achieved a high accuracy without showing any
learning or loss curves for training and validation; (iii) most
of the studies did not test the proposed model with an unseen
GPS spoofing dataset; and (iv) only a few studies considered
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 3

3
the detection and execution time, although they are essential in
cybersecurity, where time-sensitive activities must be carried
out while detecting and thwarting UAV cyberattacks and the
proposed models are computationally expensive. Therefore, it
is crucial to develop a detection system to protect UAVs from
spoofing attacks. The main contributions of this paper to bridge
this gap in the previous researches are:
• We introduce an image-based intrusion detection frame-
work that employs convolutional neural network architec-
tures with transfer learning for detecting GPS spoofing
attacks;
• We discuss the uses of different oversampling techniques,
such as the Synthetic Minority Oversampling Technique
with the Edited Nearest Neighbors and Adaptive Syn-
thetic Sampling algorithm, and we determine the most
suitable oversampling technique for the given datasets;
• We employ data transformation with pipeline optimiza-
tion method to streamline the time taken for image
loading and processing, harmonizing feature dimensions
to address discrepancies in the number of features for
training and unseen datasets using principal component
analysis, and Bayesian optimization with tree Parzen
estimator to reduce the overfitting;
• We show, for the first time, how a high-accuracy model
that overfits can cause a problem in detecting cyberattacks
by not generalizing properly, and propose a method
to reduce overfitting and to generalize well to unseen
dataset;
• We discuss the significance of illustrating the combina-
tion of the transfer learning, learning curves, and loss
curves in one plot to illustrate the effectiveness of the
chosen existing deep learning methods, and to evaluate
the performance and the convergence of the proposed
models.
To the best of our knowledge, no previous work has
proposed such an image-based intrusion detection method
that combines CNN architecture models with transfer learning
to detect GPS spoofing attacks from a UAV attack dataset;
illustrated a plot that combines learning and loss curves for
training and validation before and after applying transfer learn-
ing; evaluated the proposed models with many different clas-
sification metrics; meticulously detailed the testing process;
or rigorously evaluated the proposed models using unseen
datasets. Developing a model to identify diverse GPS spoofing
attacks poses a formidable challenge due to the various types
of UAVs with different types of sensors, and communication
protocols. This diversity in UAV types and features increases
the complexity and intensifies the intrusion detection problem,
resulting in a shortage of model performance due to the diverse
set of features in UAVs that the model has not been trained
on. Therefore, prior research works that have implemented
machine learning approaches or proposed their algorithms and
achieved high accuracies have often demonstrated their models
only on specific dataset. However, the generalizability of these
models to unseen datasets remains uncertain.
The rest of the paper is organized as follows. Section II
explains the key concepts behind the implementation of the
models, introduces the proposed framework, and provides a
comprehensive description of the characteristics of the training
and unseen datasets. Section III demonstrates the proposed
model evaluation metrics, the step time, and the curves (learn-
ing and loss) for the best-performing proposed models. Section
IV introduces and explains the model evaluation metrics for
the best-fit models; presents the numerical results of the
application of proposed models on an unseen dataset; and
discusses the advantages of our framework and the challenges
encountered during the experimentation. Section V concludes
the paper.
II. PROPOSED FRAMEWORK
A. System Architecture
The objective of the present contribution is to develop
an image-based intrusion detection method employing deep
learning models with highly accurate forecasting information
of GPS spoofing cyberattacks, obtained from UAV Attack
Datasets1. The datasets consist of logs from benign flights
and other flights that experience GPS spoofing attacks in
two different formats: comma-separated values (CSV) and
universal log (ULOG) files: they were created by Whelan et
al. [8] and other authors from Ontario Tech University and the
University of Tabuk.
In this experiment, the UAVs are equipped with an open-
source flight controller named Pixhawk 4 flight controller
[29] running the PX4 Autopilot software and launched in
Shanghai, China, by the QGroundControl software that allows
the user to execute the mission and monitor it in real-time [30].
During the flight, the UAVs receive authentic GPS signals from
the Keysight EXG N5172B signal generator, while the agent
simultaneously uses the GPS-SDR-SIM tools to generate fake
GPS signals [31]. HackRF transmits the spoofed GPS signals
with the same frequency band according to international regu-
lations and a higher power than the authentic signal so that the
UAV can lock onto the spoofed GPS. Moreover, to guarantee
a successful hijack, the agent broadcasts white Gaussian noise
on the GPS frequency band to jam the GPS signals in order
to prevent the UAV from receiving authentic GPS signals.
Further, each UAV flight has different flight dynamics and
characteristics that may affect a model’s detection of GPS
cyberattacks. The generated datasets are thereby useful for
evaluating the performance of the models under GPS spoofing
and ping DoS attacks, because they contain both simulation
and live flights of different types of UAVs, such as Holybro
S500, Yuneec H480, DeltaQuad VTOL, Standard Tailsitter,
Standard Plane, and 3DR IRIS [27], [28].
In this paper, we propose an image-based IDS model
based on CNN architectures with transfer learning to detect
GPS cyberattacks. Thus, the proposed deep learning model
architecture in Fig. 1 is designed not only to achieve a
high classification accuracy on the training dataset but also
to generalize well to other datasets relevant to GPS attack
contexts. Therefore, our IDS model is evaluated by using many
different classification metrics and moreover, the model is
1https://https://ieee-dataport.org/open-access/uav-attack-dataset
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 4

4
tested on an unseen dataset to ensure successful generalization
on a new dataset. Additionally, we introduced a plot that
combines learning and loss curves for training and validation
before and after applying transfer learning, which will be
presented later Section.
The proposed image-based IDS model consists of the fol-
lowing seven main stages:
1) Data Collection: Collecting network traffic datasets in
one comma-separated values file;
2) Data Preprocessing: Removing duplicated rows, han-
dling the missing values, converting raw data into a
format that deep learning models can use for detection,
reducing the number of features, and balancing the
dataset;
3) Data Representation: Converting tabular data into
three-dimensional array images and saving them as a
PNG file;
4) Data Splitting: Splitting the train-test-validation split
for the dataset as follows: An 80%-13.33%-6.67% train-
validation-test split is used to generate a training set with
80% of the data samples, a validation set with 2/3 of the
original 20% of the data samples, and a test set with 1/3
of the original 20% of the data samples;
5) Data Augmentation: This is applied randomly to each
image in the training set in the following manner. The
image is randomly flipped horizontally and/or vertically
with a probability of 0.5; the image is randomly rotated
up to 20% of its width and height; and the image is
randomly zoomed in or out by up to 10%;
6) Model Training: Using training CNN architecture mod-
els, such as MobileNetV2, Xception, VGG16, VGG19,
ResNet152, InceptionResNetV2, and InceptionV3, with
transfer learning;
7) Model detection: Evaluating the detections for each
CNN architecture model, and demonstrating the learning
and loss curves for training and validation.
B. Data preprocessing
In order to obtain a high-performance IDS model for de-
tecting GPS attacks, we used two datasets created by Whelan
et al. [8] in our paper: (i) a training dataset containing about
85 sensor files with information on actuator controls, battery
status, vehicle air data, and attitude, for five different UAVs;
and (ii) an unseen dataset containing about 268 sensor files
for one UAV named 3DR IRIS+. The differences between the
datasets are presented in Table I.
However, the datasets have a few limitations:
• There are some duplicated rows that may cause biasing
and reduce the standard deviation of the dataset. There-
fore, it is necessary to remove these duplicated rows
before conducting any further experiments.
• The datasets are vulnerable to the problem of high-class
imbalance, which can lead to a low accuracy and a high
false positive rate.
• Both datasets have a high number of outliers in some
features, such as the quaternion q[0,1,2,..] that describes
the position of the UAVs in space, delta q reset[0] that
TABLE I
DESCRIPTIVE STATISTICS OF THE UAV ATTACK AND UNSEEN DATASETS
Descriptive statistics
Training dataset
Unseen dataset
Number of UAVs
5 different UAVs
1 UAV
Number of features
85
268
Cyberattacks
GPS spoofing
attack
GPS spoofing
and
Ping Dos attack
Mean
1.16003e+07
2.9569e+06
Median
2.9149e-02
3.6226e-04
Standard Deviation
1.5951e+08
8.2505e+07
Interquartile Range
1.2620
1.0
Variance
2.5445e+16
6.8072e+15
indicates the difference between previous and current
quaternion, and dist bottom valid, which is the validation
of the distance to the ground.
• The training and testing datasets have a high number of
features, 85 and 268, respectively, which increases the
model complexity and chances of overfitting [32].
If the datasets are not correctly preprocessed to address and
mitigate the limitations of the datasets, the input data might
have a different format or shape than what is expected by the
proposed models. The models might then take a long time to
converge. Moreover, increased data complexity often leads to
poor performances, with many models over- or under-fitting.
Therefore, data preprocessing is one of the most important
stages, having a significant impact on the performance of our
proposed model. The preprocessing involves converting raw
data into a format that deep learning algorithms can use to
generate predictions, eliminate noise and outliers, and reduce
the impact of irrelevant features. Hence, to create an IDS
model with a high performance and an ability to generalize
well to a new dataset, a few measures must be taken [33].
Raw datasets with different feature scales cause difficulties
to the deep learning models during learning and result in slow,
or no, convergence. Therefore, the dataset is normalized by
Quantile Transformer Normalization to ensure that all
the numeric features have a comparable range of 0 to 1 [34],
and the labels of the datasets are converted into numerical
values between 0 and n −1 by using a LabelEncoder from
the sklearn library [35].
Because of the significant number of features and data
logs in the dataset, it is worth reducing the dimensions of
the data before training them with deep learning models to
minimize the complexity and improve the performance of
the model. Therefore, we implemented Principal Component
Analysis (PCA), a dimensional reduction technique to re-
duce the number of features into principal components while
keeping the most relevant data [36]. PCA can be performed
mathematically in many ways; however, in our study, it was
carried out by multiplying the standardized data with the
matrix of the eigenvectors of the covariance matrix, resulting
in a new dataset with fewer dimensions [37]. This involves
(i) standardizing the range of the continuous initial variables
to transform all the variables into the same scale to prevent a
biased result; (ii) calculating the covariance matrix to address
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 5

5
Fig. 1. Proposed image-based intrusion detection framework.
the relationship between the variables in the data as follows:
1
n −1(X −¯X)T (X −¯X)
(1)
where n is the number of samples, X is the data matrix, and
¯
X is the mean vector; and (iii) calculating the eigenvectors
with eigenvalues to determine the principal components based
on the proportion of variance described by each component.
Σv = λv
(2)
where Eq. 1 is used to obtain eigenvalues (λ) and correspond-
ing eigenvectors (v) for obtaining the desired reduced dimen-
sionality [38]. These calculations are necessary for defining
the number of principal components to transform the data
into a new space [37]. In our studies, the number of principal
components is visually illustrated by using a scree plot as
shown in Fig. 2.
Imbalanced datasets are datasets with an uneven or unequal
distribution of observations, indicating that certain class labels
may have a large number of observations while others have
fewer, as shown in Fig. 3. Imbalanced datasets are mainly
solved by oversampling the minority class or undersampling
the majority class, which can be achieved through techniques
such as synthetic minority oversampling techniques (SMOTE),
SMOTE with Edited Nearest Neighbors (SMOTE-ENN), and
various other balancing methods available in scikit-learn for
handling imbalanced datasets [39]. The core idea of the
balancing methods is encapsulated in the following formula:
Xnew = Xinst + λ · (Xj −Xinst),
j = 1, 2, . . . , k
(3)
where λ ∈[0, 1] is a random number and Xj is a randomly
selected sample from the set {X1, X2, . . . , Xk} of k nearest
neighbors of Xins [40].
0
20
40
60
80
Number of Components
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Cumulative Explained Variance
32 components
Explained Variance vs. Number of Components
Fig. 2. Scree Plot of cumulative explained variance for principal component
analysis.
SMOTE-ENN is one of the hybrid methods that combine
both oversampling and undersampling techniques to address
the imbalance class by creating new instances for the minor-
ity classes [39], then employs the edited closest neighbors
(ENN) algorithm technique to eliminate noisy and border-
line samples by comparing each synthetic sample with its
k-nearest neighbors (KNN) [41]. Unlike random sampling,
which simply duplicates the instances and may cause over-
fitting [42]. The combination of these two techniques aims
to reduce the overfitting that might occur due to SMOTE
and to remove some noisy samples by the (ENN) algorithm.
However, removing noisy samples by using the ENN may also
eliminate some informative samples, which results in a loss
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 6

6
of valuable information and a low classification performance
[43]. Therefore, we used the Adaptive Synthetic Sampling
algorithm (ADASYN) method for oversampling imbalanced
datasets, which addresses the limitations of the SMOTE and
the SMOTE-ENN by the following method:
• Generating more synthetic examples, using a density
distribution function in the difficult regions of the feature
space, where the class distributions are sparse, dense, and
harder to learn [44], [45];
• Performing better on highly imbalanced datasets, as
shown in Fig. 3, by randomly and diversely choosing
the nearest neighbors that have more influence on the
synthetic sample, which can reduce the overfitting and
improve the model generalization to an unseen dataset
[46].
ADASYN algorithm key steps for synthetic sample generation
can be represented as [44]:
si = xi + (xzi −xi) × λ
(5)
The process involves creating synthetic samples (si) based
on adding a scaled difference between the original instance
and its neighbor (xzi −xi), where (xi) is an instance in the
n dimensional feature space X (original instance), xzi is a
randomly chosen neighbor from the minority class (selected
neighbor), and λ is a random number that acts as scaling factor
that used to scale the difference between the original instance
and its randomly neighbor number.
Fig. 3. Bar plot for the UAV dataset.
After preprocessing the dataset, we employed the network
traffic image transformation technique, which is one of the
data transformation methods used to convert the data into three
channels of color images (red, green, and blue), because the
CNN architecture models work effectively on images with an
8-bit depth (0 to 255) providing high-resolution data [47].
We carried out the network traffic image transformation by
dividing the data samples into chunks based on the feature
sizes. In our case, the training dataset has about 32323 features
in an image that is transformed into (32 × 32 × 3), and each
chunk has 32 consecutive data samples. The image generation
for the Benign and GPS spoofing attacks is shown in Fig. 4.
0
10
20
30
0
5
10
15
20
25
30
Normal
0
10
20
30
0
5
10
15
20
25
30
GPS Spoofing
Fig. 4. Image generation for each class.
The datasets used in our paper were split by the holding split
or train-validation-test split method, which involves splitting
the datasets into three subsets: training, validation, and test.
As mentioned in [48], the aim of using this method is to
• avoid the over-fitting issue where the model achieves a
high accuracy only on the training dataset and a low
accuracy on an unseen dataset. Therefore, by having a
subset of the testing set, the model can be expected to
perform well on an unseen dataset.
• avoid the under-fitting issue where the model learns
poorly from the training dataset. By using a large subset
of the training set, the model will learn from and capture
the complexity of the dataset.
• achieve the best trade-off between bias and variance by
using the subset of the validation set.
Data augmentation is one of the methods that are used to
increase the training data by generating additional training
samples so that the model can generalize well to unseen
datasets (e.g., by employing the Keras Sequential API). The
common data augmentation techniques used in deep learning
are rotating, flipping, scaling, cropping, or adding noise to
the existing training data to improve the model performance
and reduce overfitting [49]. In this study, three random trans-
formations are applied to the images: horizontal and vertical
flipping, rotation, and zooming.
Loading datasets for training the deep learning models
after the data preprocessing and augmentation can result in
a high computational time. Therefore, the last critical step
for reducing the computational time is to use data pipeline
optimization, which involves various techniques like parallel
processing, caching, prefetching, and compression. The aim
of this step is to prepare and load the dataset without using a
high capacity of the CPU and GPU resources while reducing
the data transmission and the delay of memory access [50].
In our study, we reduced the computational time by using the
prefetching technique that overlaps the data preprocessing and
model training stages to speed up the training process. The aim
of this step is to fetch the elements of the dataset in advance
so that they are ready to be utilized by the next step [51].
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 7

7
C. Transfer learning with Convolutional Neural Network ar-
chitectures
CNNs are an artificial neural network (ANN) that have
become a critical and popular architecture in deep learning
particularly for image classification tasks as they can extract
features from the input image and classify them into one of
several predefined classes [52].
CNN architectures that are used for image classification
tasks have several convolutional layers, followed by activation,
spooling, dropout, and fully-connected layers. Convolutional
layers are used to extract features from the input image by
a set of filters or kernels. Each filter applies a convolution
operation to create a feature map that highlights particular
features in the input image to generate accurate predictions.
By stacking multiple convolutional layers, the network can
learn increasingly complex features from the input image.
Activation layers, such as Rectified Linear Unit (ReLU) create
nonlinearity in the network by selecting all the positive values
in the feature map and setting all the negative values to zero.
This allows the network to learn more features from images
and improve its accuracy on image classification tasks. The
pooling layer in the CNN is used to retain the most crucial
data while downsampling the size of the feature created by the
convolutional layers. Limiting the number of parameters while
keeping the most crucial data aids in minimizing the compu-
tational complexity of the network and preventing overfitting.
Dropout layers are used to prevent overfitting by randomly
dropping out some of the neurons in the network during
training. Fully-connected layers are used to connect all the
features extracted by the previous layers and generate the final
output.
The majority of CNN models contain three layers: a bottom
layer that learns basic features such as edges; a middle layer
that learns more intricate patterns such as shapes; and a
top layer that learns high-level representations tailored to
the dataset and task. By utilizing a pretrained CNN model,
we can fine-tune only the top layers for our task while
still leveraging the knowledge feature patterns learned by
the bottom and intermediate layers. This technique is called
transfer learning, which enables a new model to leverage
the knowledge acquired by a pretrained model that has been
trained on a large dataset [53]. This knowledge is gained by
transferring the weights of the pretrained model to the new
model trained on another dataset [54]. Moreover, by fine-
tuning a pretrained model, we can achieve a high accuracy
while using less computational resources. The fine-tuning
phase converges more quickly than when training the CNN
model from scratch and the risk of overfitting is reduced by
preventing the model from remembering the training data.
Therefore, in the context of CNN image classification, transfer
learning has been successfully applied to many image process-
ing tasks, because the captured patterns trained by the CNN
model (pretrained model) on a large dataset are applicable to
many different tasks.
ImageNet is a large-scale dataset that has more than one
million labeled images belonging to 1000 different classes, and
it is commonly used as a benchmark for image classification
tasks. CNN architectures that are trained on the ImageNet
dataset are considered some of the best models for image
classification tasks due to their ability to learn from the
complex features of raw image pixels and the use of transfer
learning, which enables them to be fine-tuned for a wide range
of tasks [53]. Therefore, we used CNN architectures, such
as MobileNetV2, VGG16, VGG19, InceptionV3, Inception-
ResNetV2, Xception, and ResNet152, to train our training
dataset and detect GPS spoofing by using transfer learning.
MobileNetV2 is a lightweight architecture that has achieved an
accuracy of 71.8% on the ImageNet dataset. It has 155 layers
consisting of depthwise separable convolutions to reduce the
number of parameters and linear bottlenecks to reduce the
computational time and cost required to train the model; the
last two layers are fully connected layers. VGG16 and VGG19
were developed by the Visual Geometry Group (VGG) at the
University of Oxford. Both the models have achieved a top-
5 error rate of 7.4% and 6.8% and an accuracy of 71.5%
and 71.1%, respectively, on the ImageNet dataset. The key
difference is that VGG19 has more filters in each layer, which
makes it a more complex model. InceptionV3, developed by
Google in 2015, has 48 convolutional layers and 3 fully
connected layers, and it has achieved an accuracy of 78.0% on
the ImageNet dataset. It uses the batch normalization technique
that normalizes the activations of each layer to improve the
accuracy of the model and reduces the overfitting issues of
the model. The InceptionResNetV2 model was introduced by
Google in 2016; it is an updated version of InceptionV3.
The key difference is that InceptionV3 has 48 layers, while
InceptionResNetV2 has 572 layers, which makes it possible
to capture more complex features in the images. Xception
is an extension of Inception that uses depthwise separable
convolutions and a global average pooling layer at the end of
the model to reduce overfitting and improve generalization. It
has achieved an accuracy of 79.0% on the ImageNet dataset.
ResNet152 is a deep architecture that has 152 layers and a
total of 60.4 million parameters. It has achieved an accuracy
of 78.6% on the ImageNet dataset and uses residual connec-
tions to address the vanishing gradient problem. The design
of the bottleneck structures of those algorithms reduces the
dimensionality of the feature maps, reduces the computational
cost, and the risk of overfitting [55].
III. PERFORMANCE EVALUATION
The deep learning models proposed in this study were im-
plemented on the UAV attacks dataset using Keras libraries and
Scikit-learn. The models were trained by the computational
resources provided by CSC - IT Center for Science Ltd.,
a nonprofit organization that offers IT services for research,
education, and public administration in Finland. The computer
configuration utilized for these experiments consists of Xeon
Gold 6230 (2 x 20 cores @ 2,1 GHz) with a NVIDIA V100
(Tesla V100-SXM2 GPU) and 300 GB of memory.
To evaluate the performance of the proposed deep learning
models on a highly imbalanced dataset for predicting GPS
spoofing attacks, we focused on the following:
• We studied the following classification metrics to measure
how well the proposed models will classify the spoofed
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 8

8
GPS signal events: accuracy (ACC), which shows the
accuracy of classification for each stage; detection rate
(DR/recall), which is the ratio between the detected attack
data and the total abnormal data; harmonic precision-
recall mean (F1-score), which is used as a statistical
measure to rate the model performance as it depends
on two factors, precision (PRE) and DR/recall; receiver
operating characteristic area under the curve (ROC AUC),
which measures how the proposed models will perform
to know the difference between authentic and spoofed
GPS signals (positive and negative classes); precision-
recall area under the curve (PR AUC), which measures
the trade-off (balance) between precision and recall;
balanced accuracy (BAC), which is the average recall of
the benign and spoofed GPS signals and is a useful metric
for imbalanced datasets; Matthews correlation coefficient
(MCC), which is a statistical tool based on chi-square
statistics used to measure the difference between the
predicted values and the actual values; and Jaccard score
(JSC), which measures the similarity between the labels,
i.e., benign and spoofed GPS signals.
• We employed multiple loss function metrics, such as
logarithmic loss function (Log Loss), which measures
how good the performance of a model is by computing
the differential between the predicted probabilities (the
outputs of the model) and the actual values (true labels),
and zero-one loss, which measures how many times the
predicted label does not match the true label.
• We used the learning and loss curves for training and
validation to monitor the performance of the model, i.e,
whether it is overfitting, underfitting, or is a good fit.
This allows us to track the deterioration of the learning
performance of the proposed models.
• We used the confusion matrix to summarize the perfor-
mance of the CNN models on a set of test and validation
datasets. This is critical when dealing with imbalanced
datasets and helps us to examine the model prediction
errors by monitoring the false positive and false negative
values.
• We computed both the running time of the models using
the “time” library and the elapsed time per step (step
time) to calculate how long the models need to process
one batch during the testing phase.
• We evaluated the generalization of our models by testing
them on unseen datasets.
The results of evaluating the proposed models for both
the testing and validation datasets presented in Table II
demonstrated that all the models achieved high accuracies.
Even though the proposed models and the models in the
literature achieved high accuracies, this does not necessarily
mean such well-performing models that could generalize well
to an unseen dataset. Therefore, we provided the learning and
lose curves for our best-performing models to help us track
the improvement or deterioration of the learning performance
of the model by plotting both the training and validation loss
and accuracy over epoch in one graph as shown in Figs. 5, 6
and 7.
2
4
6
8
10
Epochs
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
Loss
Training and Validation Loss
Train Loss
Validation Loss
Train Accuracy
Validation Accuracy
Start Fine Tuning
0.825
0.850
0.875
0.900
0.925
0.950
0.975
1.000
Accuracy
Fig. 5. Learning and loss curves for the Residual Networks model with 50
layers and a running time of 117.43 s.
2
4
6
8
10
Epochs
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Loss
Training and Validation Loss
Train Loss
Validation Loss
Train Accuracy
Validation Accuracy
Start Fine Tuning
0.80
0.85
0.90
0.95
1.00
Accuracy
Fig. 6. Learning and loss curves for the Visual Geometry Group model with
19 layers and a running time of 120.64 s.
2
4
6
8
10
Epochs
0.00
0.05
0.10
0.15
0.20
0.25
0.30
Loss
Training and Validation Loss
Train Loss
Validation Loss
Train Accuracy
Validation Accuracy
Start Fine Tuning
0.84
0.86
0.88
0.90
0.92
0.94
0.96
0.98
1.00
Accuracy
Fig. 7. Learning and loss curves for the Residual Network with 152 layers
and a running time of 309 s.
IV. RESULTS AND DISCUSSION
To construct a generalized robustness model to avoid overfit-
ting issues, we trained the CNN models with transfer learning
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 9

9
TABLE II
CLASSIFICATION REPORT FOR THE TESTING AND VALIDATION DATASETS OF THE UAV ATTACK DATASET
Classification report for the testing dataset with transfer learning
Classification Metrics
Models
ResNet-50
MobileNet-v2
Xception
VGG-16
VGG-19
ResNet-152
Inception
ResNet-v2
Inception-v3
Accuracy (%)
99.652
91.184
99.652
99.479
100
100
99.652
99.652
Precision (%)
99.654
93.127
99.654
99.483
100
100
99.654
99.654
Recall (%)
99.657
91.840
99.652
99.479
100
100
99.652
99.652
F1-score (%)
99.656
91.871
99.652
99.478
100
100
99.652
99.652
F1-score for each
type of attack (%)
[99.690,
99.604]
[92.205,
91.438]
[99.705,
99.576]
[99.554,
99.373]
[100,
100]
[100,
100]
[99.693,
99.6]
[99.698,
99.590]
Confusion Matrix
[[322 0]
[2 252]]
[[278 47]
[0 251]]
[[339 0]
[2 235]]
[[335 0]
[3 238]]
[[319 0]
[0 257]]
[[334 0]
[0 242]]
[[325 0]
[2 249]]
[[331 0]
[2 243]]
ROC AUC (%)
99.606
92.769
99.578
99.377
100
100
99.601
99.591
PR AUC (%)
99.559
84.228
99.503
99.276
100
100
99.550
99.538
Balanced Accuracy (%)
99.606
92.769
99.578
99.377
100
100
99.601
99.591
Matthews Correlation
Coefficient
0.99297
0.84880
0.99284
0.98933
1.0
1.0
1.0
0.99291
Jaccard Score
0.99212
0.84228
0.99156
0.98755
1.0
1.0
0.99203
0.99183
Log Loss
0.12515
2.94106
0.12515
0.18772
2.224e-16
2.220e-16
2.220e-16
0.12515
Zero-One Loss
0.00347
0.08159
0.00347
0.00520
0.0017
0.0
0.0
0.00347
Specificity
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
Step time (s)
1.35
0.19
1.43
1.46
2.90
1.79
2.78
1.31
Classification Report for validation dataset with transfer learning
Classification Metrics
Models
ResNet-50
MobileNet-v2
Xception
VGG-16
VGG-19
ResNet-152
Inception
ResNet-v2
Inception-v3
Accuracy (%)
100
90.674
99.289
99.555
100
99.911
99.467
99.111
Precision (%)
100
92.234
99.298
99.555
100
99.911
99.472
99.125
Recall (%)
100
90.674
99.289
99.555
100
99.911
99.467
99.111
F1-score (%)
100
90.722
99.288
99.555
100
99.911
99.466
99.117
F1-score for each
type of attack (%)
[100,
100]
[91.154,
90.140]
[99.383,
99.161]
[99.612,
99.480]
[100,
100]
[99.922,
99.895]
[99.536,
99.373]
[99.223,
98.962]
Confusion Matrix
[[642 0]
[0 484]]
[[541 105]
[0 480]]
[[645 0]
[8 251]]
[[642 0]
[5 479]]
[[657 0]
[0 469]]
[[645 0]
[1 480]]
[[644 0]
[6 476]]
[[639 0]
[10 477]]
ROC AUC (%)
100
91.873
99.168
99.483
100
99.896
99.377
98.973
PR AUC (%)
100
82.051
99.047
99.410
100
99.880
99.288
98.834
Balanced Accuracy (%)
100
91.873
99.168
100
99.483
99.896
99.377
98.973
Matthews Correlation
Coefficient
1.0
0.82894
0.98555
0.99096
1.0
0.99818
0.98915
0.982025
Jaccard Score
1.0
0.820512
0.98336
0.98966
1.0
0.99792
0.98755
0.979466
Log Loss
2.2204e-16
3.36108
0.25608
0.16005
2.2204e-16
0.03201
0.19206
0.32010
Zero-One Loss
0.0
0.0932
0.007104
0.00444
0.00173
0.00088
0.00532
0.00888
Specificity
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
Step Time (s)
1.34
1.19
2.42
3.42
4.53
3.77
9.129
1.30
to exploit the knowledge and features gained from a significant
number of images and classes in the ImageNet classification
dataset. We applied partial transfer learning for parameter
transfer in our study by freezing the lower layers of the
pretrained model and then fine-tuning the higher layers for
our task.
After the partial transfer learning was implemented, the
overall performance of the proposed models improved ap-
proximately by 0.8% to 2.08%. The partial transfer learning
configuration and running time for the proposed models are
presented in Table III.
The green vertical line in learning and loss curves serves
as a visual indicator of the utilization of the partial transfer
learning on the proposed models, preventing it from under- or
overfitting. The curves before the green line demonstrate that
the models are overfitting since the training undergoes without
partial transfer learning as shown in learning and loss curves
figures, and the confusion matrix indicates that the proposed
models are not performing well in correctly identifying GPS
cyberattacks, as shown in Table IV. Post the green line, the
training incorporates partial transfer learning. Learning and
loss curves figures aim to emphasize the influence of partial
transfer learning on the model’s overall performance as shown
in Table II.
TABLE III
PARTIAL TRANSFER LEARNING CONFIGURATION AND RUNNING TIME FOR
THE CNN MODELS
Models
Total
layers
Frozen
layers
Unfrozen
layers
RT (s)
DT (s)
ResNet-50
175
1 to 150
151 to 175
117.43
1.951
MobileNet-v2
154
1 to 132
133 to 154
77.3
1.289
Xception
132
1 to 113
114 to 132
120.41
2.035
VGG-16
19
1 to 16
17 to 19
120.85
3.241
VGG-19
22
1 to 18
19 to 22
120.64
3.086
ResNet-152
515
1 to 443
444 to 515
309
5.102
Inception
ResNet-v2
780
1 to 671
672 to 780
181.4
9.203
Inception-v3
311
1 to 267
268 to 311
106.4
1.964
Although we employed many classification metrics to eval-
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 10

10
uate our proposed models, we focused on the F1-score metric
and confusion matrix result values as the accuracy measures.
In most real-world classification situations, the data might
have an imbalanced class distribution, which can mislead
other metrics, such as accuracy, but the F1-score metric and
the confusion matrix provide a balanced evaluation. The F1-
score considers both precision and recall metrics, thus making
it a better indicator of a model’s ability to generalize well
to unseen data, and the confusion matrix provides a clear
evaluation of how well the proposed models will perform in
terms of correct or incorrect predictions.
TABLE IV
CLASSIFICATION REPORT FOR TESTING AND VALIDATION DATASETS
BEFORE APPLYING PARTIAL TRANSFER LEARNING
Metrics for
testing
dataset
Models
ResNet-50
ResNet-152
VGG-19
Inception-v3
Acc (%)
98.611
99.652
98.784
98.437
PR (%)
98.643
99.654
98.810
98.479
Rec (%)
98.611
99.652
98.784
98.437
F1 (%)
98.607
99.652
98.782
98.433
F1\attack (%)
[98.809,
98.333]
[99.700,
99.586]
[98.940,
98.574]
[98.634,
98.174]
CM
[[332 0]
[8 236]]
[[333 0]
[2 241]]
[[327 0]
[7 242]]
[[325 0]
[9 242]]
Metrics for
validation
dataset
Models
ResNet-50
ResNet-152
VGG-19
Inception-v3
Acc (%)
98.579
98.401
97.957
98.490
PR (%)
98.613
98.445
98.026
98.529
Rec (%)
98.579
98.401
97.957
98.490
F1 (%)
98.575
98.397
97.949
98.486
F1\attack (%)
[98.765,
98.326]
[98.606,
99.125]
[98.284,
97.475]
[98.674,
98.245]
CM
[[640 0]
[16 470]]
[[637 0]
[18 471]]
[[659 0]
[23 444]]
[[633 0]
[17 476]]
The evaluation of the proposed models for both the testing
and validation datasets presented in Table II demonstrated that
all the models achieved high accuracies, and the best models
for the UAV attack dataset are the VGG-19 and ResNet-152
models for the following reasons:
• The VGG-19 and ResNet-152 models successfully iden-
tified a large number of actual GPS attacks that occurred
(positive cases). The true positives in the confusion
metrics indicated that the models detected 319 and 334
actual cyberattacks for the testing dataset, and 657 and
645 for the validation dataset respectively. On the other
hand, the confusion metrics for the other models, such
as VGG-16 and Inception-v3, indicated that the models
failed to detect some GPS spoofing attacks.
• The training logs indicate that the proposed models have
low training and validation losses of 0.0027 and 0.0032,
respectively, for the VGG-19 model, and low training
and validation losses of 0.0019 and 0.0016, respectively,
for the ResNet-152 model. These results suggest that
both models perform well on the training and validation
datasets.
• The Matthews correlation coefficient and the loss function
metrics, such as log loss and zero-one, indicate that the
model achieved perfect prediction by learning the under-
lying patterns and could generalize well to a different
dataset.
• The learning and loss curves for both models indicate
that the models are not overfitting, as shown in Figs. 6
and 7.
Achieving a high performance rate as shown in the classifi-
cation report in Table II is a desirable outcome, but it does not
indicate a complete evaluation of the model performance. A
comprehensive evaluation involves considering the ability of
the model to generalize well and to identify complex patterns
and features of different underrepresented attacks, such as
GPS spoofing attacks, apart from the normal network behavior
(benign traffic). As a result, we also tested our models with
an unseen dataset that contains 268 features for one UAV
named 3DR IRIS+. The differences between the training and
the unseen datasets are shown in Table I.
The evaluation of the proposed models on the unseen
datasets, shown in Table V, demonstrates that the VGG-19 and
ResNet-152 models achieved the highest accuracies and F1
scores. However, the confusion metrics show that the models
failed to detect some instances (cyberattacks) that occurred.
The reason behind this is that these instances were related to
the Ping DoS attacks, and our models were designed to detect
GPS spoofing attacks.
TABLE V
CLASSIFICATION REPORT FOR THE PROPOSED MODELS ON UNSEEN
DATASETS
Metrics for
unseen
dataset
Models
ResNet-50
ResNet-152
VGG-19
Inception-v3
Acc (%)
75.250
99.0
99.25
46.437
PR (%)
83.673
98.018
98.260
21.564
Rec (%)
75.250
99.0
99.25
46.437
F1 (%)
74.416
98.999
99.249
29.452
F1\attack (%)
[71.345,
78.217]
[99.083,
98.899]
[99.326,
99.153]
[63.422,
0.0]
MCC
0.59248
0.98003
0.98491
0.0
Jacc
0.64227
0.97823
0.98321
0.0
Log Loss
8.92080
0.36043
0.27032
19.305
ZOL
0.24750
0.01000
0.00749
0.53562
CM
[[493 392]
[4 711]]
[[865 0]
[16 719]]
[[885 0]
[12 703]]
[[743 0]
[857 0]]
Although, the learning curve for ResNet-50 also revealed
that the model did not exhibit overfitting as shown in Fig.
5, the model performance exhibited suboptimal performance
on unseen datasets. This is due to the fact that ResNet-152
has more layers, parameters (has 152 layers and 60 million
parameters), and more bottleneck structure in each residual
block compared to ResNet-50 (50 layers and 25 million
parameters) [56], which allows the model to generalize well to
a new dataset in terms of domain or distribution [55]. However,
the inception-v3 model showed a poor performance on the
unseen dataset with an accuracy of 46.437% and an F1-score
of 29.452%. This is due to the fact that the learning and loss
curves demonstrated that the model is overfitting as shown in
Fig. 8, although it achieved a high accuracy of 99.6% on the
testing dataset as shown in Table II. Therefore, it is critical to
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 11

11
monitor the learning and loss curves even if the model achieves
high evaluation metrics on the training dataset.
2
4
6
8
10
Epochs
0.00
0.05
0.10
0.15
0.20
0.25
Loss
Training and Validation Loss
Train Loss
Validation Loss
Train Accuracy
Validation Accuracy
Start Fine Tuning
0.92
0.94
0.96
0.98
1.00
Accuracy
Fig. 8. Learning and loss curves for the Inception-Residual Version 3 model
with a running time of 106.4 s demonstrated that the model is overfitting.
As a result, the parameters for Inception-v3 are tuned
using a commonly used approach, the Bayesian optimization
technique with Tree-structured Parzen Estimator (BO-TPE)
algorithm in the Hyperopt library because of its sample effi-
ciency [57]. Since there are many important hyperparameters
in terms of accuracy, speed, and handling false negatives
and false positives to prevent the overfitting, the chosen
parameters for the Inception-v3 model are shown in Table
VI. After implementing Hyperopt (BO-TPE), the performance
of inception-v3 improved by approximately 0.35%, and the
model is a good fit, as shown in Fig. 9.
TABLE VI
HYPERPARAMETER (BO-TPE) OPTIMIZATION CONFIGURATION FOR
INCEPTION-RESIDUAL VERSION 3 MODEL
Hyperparameter
Search Range
Optimal Value
Frozen
[1, 780]
50
Epochs
[1, 20]
7
Patience
[2, 5]
4
Learning rate
[0.00003,
0.00009]
8e-05
Dropout
[0.2, 0.5]
0.4
Weight decay
[1e-9, 1e-3]
5.578e4
Optimizer
[Adam, SGD,
RMSprop]
Adam
RT (s)
2184
The learning and loss curve for the inception-v3 model
in Fig. 8 demonstrated that the generalization gap between
the validation and training losses indicates a lack of conver-
gence. Therefore, to improve the learning and loss curve, we
added the regularization parameter ’weight decay’ into the
hyperparameter tuning process using the BO-TPE algorithm in
Hyperopt as shown in Table VI. As a result, the generalization
gap has decreased as shown in Fig. 9 compared with Fig. 8.
In our study, we creatively used and combined existing
deep learning approaches to effectively detect GPS spoofing
cyberattacks with high accuracy and a low execution time,
as shown in Table II, V, and VII. Further, to ensure a
fair and valid comparison with other methods, we compared
our performance method with different methods by using
the same dataset for GPS spoofing attack and employed the
same evaluation metrics as in Whelan et al. [28], including,
Precision, Recall, and F1-score as shown in Table VIII.
1
2
3
4
5
6
7
Epochs
0.0
0.2
0.4
0.6
0.8
Loss
Training and Validation Loss
Train Loss
Validation Loss
Train Accuracy
Validation Accuracy
Start Fine Tuning
0.6
0.7
0.8
0.9
1.0
Accuracy
Fig. 9. Learning and loss curves for the Inception-Residual Version 3 model
with Hyperopt and a running time of 75.1 s.
TABLE VII
CLASSIFICATION REPORT FOR INCEPTION-RESIDUAL VERSION 3 ON
TRAINING AND UNSEEN DATASETS: HYPEROPT (BO-TPE)
OPTIMIZATION
Classification
Metrics
Training Dataset
New dataset (unseen)
Testing
Validation
Testing
Validation
Acc (%)
100
100
99.062
98.562
F1 (%)
100
100
99.061
98.556
F1\attack (%)
[100, 100]
[100, 100]
[99.168,
98.926]
[98.869,
98,025]
CM
[[336 0]
[0 240]]
[[648 0]
[0 478]]
[[894 0]
[15 691]]
[[1006 0]
[23 571]]
ST (s)
1.31
1.30
No training
RT (s)
75.1
DT (s)
1.957
3.703
TABLE VIII
COMPARISON BETWEEN THE LATEST PROPOSED BASED ON UAV ATTACK
DATASET.
Model
Classes
Precision
Recall
F1
Autoencoder [28]
Benign
99.36
94.81
97.03
Malicious
74.72
96.18
84.10
Inception-v3 + Hyperopt
Benign
100
100
100
Malicious
100
100
100
In this paper, we identified the following limitations and
challenges for the problem investigated in this paper:
• Selecting an appropriate technique to build a high-
performance model in terms of high accuracy without
overfitting issues, low running and detection time, and
generalizing well to unseen datasets is a formidable
challenge. The fact that there are a multitude of models,
diverse feature reduction methods, such as random forest
regressor (RFR) and PCA, and different methods of data
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 12

12
normalization techniques, such as min-max, Z-score, and
Quantile transformer normalization, makes the decision-
making process complex and intricate.
• Transfer learning can lead the proposed models to a
poor performance or overfitting, if we fine-tune many
layers, and using a complex pretrained model may require
high computational resources if the features learned by
the pretrained model are irrelevant for detecting a GPS
spoofing attack.
Our proposed Image-based Intrusion Detection System for
detecting GPS spoofing cyberattacks attempts to overcome
these limitations. We observed several trends and patterns that
demonstrate the effectiveness of our approach:
• In addition to the normal network behavior (benign
traffic), the proposed models also successfully identified
complex patterns and features of GPS spoofing attacks
by using partial transfer learning techniques to reduce
overfitting and minimize the false negatives and positives.
• The proposed model was trained on dimensionality-
reduced features that exhibit strong correlations and are
comparable with various GPS cyberattack datasets. This
indicates the robustness of the model and its potential for
real-world applications.
• The learning and loss curves showed that the training
score and the validation score converged to a similar value
as the number of training samples increased. This indi-
cates that the proposed model has a good generalization
ability and could perform well on unseen data.
V. CONCLUSION
UAVs are attracting significant interest among both military
and civilian industries due to their ability to perform critical
tasks in high-risk environments. At the same time, cyberattacks
such as GPS spoofing attacks are also increasing significantly,
constituting a serious threat to human lives. In this paper, we
have proposed an Image-based intrusion detection system for
detecting GPS spoofing attacks based on CNN architecture
models with transfer learning. Our method was able to suc-
cessfully learn and identify normal sensor values based on
historical flight logs. The proposed models were evaluated on
imbalanced datasets that include many different UAVs with
different flight dynamics and characteristics affecting the GPS
receiver’s performance. The numerical results demonstrated
that the selected methods enhance the performance of the
model, leading to improved detection capabilities when tested
on unseen datasets. The experimental results showed that the
Visual Geometry Group 19-layer model and the optimized
Inception version 3 model using the tree-structured Parzen
Estimator algorithm with transfer learning achieved a high
accuracy of 100%. Remarkably, the Visual Geometry Group
19-layer model and the optimized Inception version 3 also
achieved a high accuracy of 99.2% and 99.06% on the unseen
dataset respectively. Further, the model results demonstrated
the feasibility of the proposed models in real-time data.
In the future, we plan to focus on different datasets and
applications using different approaches such as an online
adaptive model that can update itself on new available datasets.
This will enable the model to remain accurate and relevant to
new datasets.
REFERENCES
[1] B. L. Curry and A. W. C. M. A. AL, “Turn points in the air using
historical examples to illustrate usaf doctrine,” Ph.D. dissertation, 1997.
[2] D. D. Nguyen, J. Rohacs, and D. Rohacs, “Autonomous flight trajectory
control system for drones in smart city traffic management,” ISPRS
International Journal of Geo-Information, vol. 10, no. 5, p. 338, 2021.
[3] I. Guvenc, F. Koohifar, S. Singh, M. L. Sichitiu, and D. Matolak,
“Detection, tracking, and interdiction for amateur drones,” IEEE Com-
munications Magazine, vol. 56, no. 4, pp. 75–81, 2018.
[4] G. Nacouzi, J. D. Williams, B. Dolan, A. Stickells, D. Luckey, C. Lud-
wig, J. Xu, Y. Shokh, D. M. Gerstein, and M. Decker, Assessment of
the proliferation of certain remotely piloted aircraft systems: response
to section 1276 of the national defense authorization act for fiscal year
2017.
RAND Corporation Santa Monica, CA, 2018.
[5] N.
Norhashim,
N.
M.
Kamal,
Z.
Sahwee,
S.
A.
Shah,
and
D. Sathyamoorthy, “The effects of jamming on global positioning system
(gps) accuracy for unmanned aerial vehicles (uavs),” in 2022 Inter-
national Conference on Computer and Drone Applications (IConDA).
IEEE, 2022, pp. 18–22.
[6] L. Eldredge, P. Enge, M. Harrison, R. Kenagy, S. Lo, R. Loh, R. Lilly,
M. Narins, and R. Niles, “Alternative positioning, navigation & timing
(pnt) study,” in International civil aviation organisation navigation
systems panel (NSP), Working Group Meetings, Montreal, Canada,
2010.
[7] N. O. Tippenhauer, C. P¨opper, K. B. Rasmussen, and S. Capkun, “On
the requirements for successful gps spoofing attacks,” in Proceedings of
the 18th ACM conference on Computer and communications security,
2011, pp. 75–86.
[8] J. Whelan, A. Almehmadi, J. Braverman, and K. El-Khatib, “Threat
analysis of a long range autonomous unmanned aerial system,” in 2020
International Conference on Computing and Information Technology
(ICCIT-1441).
IEEE, 2020, pp. 1–5.
[9] D. P. Shepard, J. A. Bhatti, T. E. Humphreys, and A. A. Fansler,
“Evaluation of smart grid and civilian uav vulnerability to gps spoofing
attacks,” in Proceedings of the 25th International Technical Meeting of
The Satellite Division of the Institute of Navigation (ION GNSS 2012),
2012, pp. 3591–3605.
[10] A. Ruegamer, D. Kowalewski et al., “Jamming and spoofing of gnss
signals–an underestimated risk?!” Proc. Wisdom Ages Challenges Mod-
ern World, vol. 3, pp. 17–21, 2015.
[11] K. C. Zeng, S. Liu, Y. Shu, D. Wang, H. Li, Y. Dou, G. Wang,
and Y. Yang, “All your {GPS} are belong to us: Towards stealthy
manipulation of road navigation systems,” in 27th USENIX security
symposium (USENIX security 18), 2018, pp. 1527–1544.
[12] J. Gaspar, R. Ferreira, P. Sebasti˜ao, and N. Souto, “Capture of uavs
through gps spoofing using low-cost sdr platforms,” Wireless Personal
Communications, vol. 115, pp. 2729–2754, 2020.
[13] R. Ferreira, J. Gaspar, P. Sebastiao, and N. Souto, “Effective gps
jamming techniques for uavs using low-cost sdr platforms,” Wireless
Personal Communications, vol. 115, pp. 2705–2727, 2020.
[14] T. Suzuki and N. Kubo, “Gnss-sdrlib: An open-source and real-time gnss
software defined radio library,” in Proceedings of the 27th International
Technical Meeting of The Satellite Division of the Institute of Navigation
(ION GNSS+ 2014), 2014, pp. 1364–1375.
[15] A. J. Kerns, D. P. Shepard, J. A. Bhatti, and T. E. Humphreys,
“Unmanned aircraft capture and control via gps spoofing,” Journal of
field robotics, vol. 31, no. 4, pp. 617–636, 2014.
[16] M. L. Psiaki and T. E. Humphreys, “Gnss spoofing and detection,”
Proceedings of the IEEE, vol. 104, no. 6, pp. 1258–1270, 2016.
[17] ——, “Protecting gps from spoofers is critical to the future of naviga-
tion,” IEEE spectrum, vol. 10, 2016.
[18] K.-C. Kwon and D.-S. Shim, “Performance analysis of direct gps
spoofing detection method with ahrs/accelerometer,” Sensors, vol. 20,
no. 4, p. 954, 2020.
[19] J.-H. Lee, K.-C. Kwon, D.-S. An, and D.-S. Shim, “Gps spoofing detec-
tion using accelerometers and performance analysis with probability of
detection,” International Journal of Control, Automation and Systems,
vol. 13, pp. 951–959, 2015.
[20] Z. Feng, N. Guan, M. Lv, W. Liu, Q. Deng, X. Liu, and W. Yi,
“An efficient uav hijacking detection method using onboard inertial
measurement unit,” ACM Transactions on Embedded Computing Systems
(TECS), vol. 17, no. 6, pp. 1–19, 2018.
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed

## Page 13

13
[21] Y. Dang, C. Benza¨ıd, B. Yang, and T. Taleb, “Deep learning for gps
spoofing detection in cellular-enabled uav systems,” in 2021 Interna-
tional Conference on Networking and Network Applications (NaNA).
IEEE, 2021, pp. 501–506.
[22] S. Dasgupta, T. Ghosh, and M. Rahman, “A reinforcement learning
approach for global navigation satellite system spoofing attack detection
in autonomous vehicles,” Transportation research record, vol. 2676,
no. 12, pp. 318–330, 2022.
[23] S. C. Bose, “Gps spoofing detection by neural network machine learn-
ing,” IEEE Aerospace and Electronic Systems Magazine, vol. 37, no. 6,
pp. 18–31, 2021.
[24] S. Wang, J. Wang, C. Su, and X. Ma, “Intelligent detection algorithm
against uavs’ gps spoofing attack,” in 2020 IEEE 26th International
Conference on Parallel and Distributed Systems (ICPADS). IEEE, 2020,
pp. 382–389.
[25] S. Semanjski, A. Muls, I. Semanjski, and W. De Wilde, “Use and
validation of supervised machine learning approach for detection of gnss
signal spoofing,” in 2019 International Conference on Localization and
GNSS (ICL-GNSS).
IEEE, 2019, pp. 1–6.
[26] Y. Dang, C. Benzaid, B. Yang, and T. Taleb, “Deep learning for gps
spoofing detection in cellular enabled unmanned aerial vehicle systems,”
arXiv preprint arXiv:2201.00568, 2022.
[27] J. Whelan, T. Sangarapillai, O. Minawi, A. Almehmadi, and K. El-
Khatib, “Novelty-based intrusion detection of sensor attacks on un-
manned aerial vehicles,” in Proceedings of the 16th ACM symposium
on QoS and security for wireless and mobile networks, 2020, pp. 23–
28.
[28] J. Whelan, A. Almehmadi, and K. El-Khatib, “Artificial intelligence for
intrusion detection systems in unmanned aerial vehicles,” Computers
and Electrical Engineering, vol. 99, p. 107784, 2022.
[29] E. Ebeid, M. Skriver, and J. Jin, “A survey on open-source flight control
platforms of unmanned aerial vehicle,” in 2017 euromicro conference on
digital system design (dsd).
IEEE, 2017, pp. 396–402.
[30] J. Del Arco, D. Alejo, B. C. Arrue, J. A. Cobano, G. Heredia, and
A. Ollero, “Multi-uav ground control station for gliding aircraft,” in 2015
23rd Mediterranean Conference on Control and Automation (MED).
IEEE, 2015, pp. 36–43.
[31] T. Gu, Z. Fang, Z. Yang, P. Hu, and P. Mohapatra, “Mmsense: Multi-
person detection and identification via mmwave sensing,” in Proceedings
of the 3rd ACM Workshop on Millimeter-wave Networks and Sensing
Systems, 2019, pp. 45–50.
[32] J. Miao and L. Niu, “A survey on feature selection,” Procedia Computer
Science, vol. 91, pp. 919–926, 2016.
[33] H. Chen, J. Wang, and D. Shi, “A data preparation method for machine-
learning-based power system cyber-attack detection,” in 2018 Interna-
tional Conference on Power System Technology (POWERCON).
IEEE,
2018, pp. 3003–3009.
[34] Z. Wu, H. Zhang, P. Wang, and Z. Sun, “Rtids: A robust transformer-
based approach for intrusion detection system,” IEEE Access, vol. 10,
pp. 64 375–64 387, 2022.
[35] E. Bisong, “Introduction to scikit-learn,” in Building Machine Learning
and Deep Learning Models on Google Cloud Platform. Springer, 2019,
pp. 215–229.
[36] H. Rajadurai and U. D. Gandhi, “An empirical model in intrusion
detection systems using principal component analysis and deep learning
models,” Computational Intelligence, vol. 37, no. 3, pp. 1111–1124,
2021.
[37] H. Abdi and L. J. Williams, “Principal component analysis,” Wiley
interdisciplinary reviews: computational statistics, vol. 2, no. 4, pp. 433–
459, 2010.
[38] C. Labr´ın and F. Urdinez, “Principal component analysis,” in R for
Political Data Science.
Chapman and Hall/CRC, 2020, pp. 375–393.
[39] Z. Chen, Q. Yan, H. Han, S. Wang, L. Peng, L. Wang, and B. Yang,
“Machine learning based mobile malware detection using highly im-
balanced network traffic,” Information Sciences, vol. 433, pp. 346–364,
2018.
[40] M. Injadat, A. Moubayed, A. B. Nassif, and A. Shami, “Multi-stage
optimized machine learning framework for network intrusion detection,”
IEEE Transactions on Network and Service Management, vol. 18, no. 2,
pp. 1803–1816, 2020.
[41] X. Zhang, J. Ran, and J. Mi, “An intrusion detection system based on
convolutional neural network for imbalanced network traffic,” in 2019
IEEE 7th International Conference on Computer Science and Network
Technology (ICCSNT).
IEEE, 2019, pp. 456–460.
[42] I. Gonc¸alves, S. Silva, J. B. Melo, and J. M. Carreiras, “Random
sampling technique for overfitting control in genetic programming,”
in Genetic Programming: 15th European Conference, EuroGP 2012,
M´alaga, Spain, April 11-13, 2012. Proceedings 15.
Springer, 2012,
pp. 218–229.
[43] G. E. Batista, R. C. Prati, and M. C. Monard, “A study of the behavior
of several methods for balancing machine learning training data,” ACM
SIGKDD explorations newsletter, vol. 6, no. 1, pp. 20–29, 2004.
[44] H. He, Y. Bai, E. A. Garcia, and S. Li, “Adasyn: Adaptive synthetic
sampling approach for imbalanced learning,” in 2008 IEEE interna-
tional joint conference on neural networks (IEEE world congress on
computational intelligence).
IEEE, 2008, pp. 1322–1328.
[45] S. Barua, M. M. Islam, X. Yao, and K. Murase, “Mwmote–majority
weighted minority oversampling technique for imbalanced data set learn-
ing,” IEEE Transactions on knowledge and data engineering, vol. 26,
no. 2, pp. 405–425, 2012.
[46] A. Glazkova, “A comparison of synthetic oversampling methods for
multi-class text classification,” arXiv preprint arXiv:2008.04636, 2020.
[47] J. Krupski, W. Graniszewski, and M. Iwanowski, “Data transformation
schemes for cnn-based network traffic analysis: A survey,” Electronics,
vol. 10, no. 16, p. 2042, 2021.
[48] R. Kohavi et al., “A study of cross-validation and bootstrap for accuracy
estimation and model selection,” in Ijcai, vol. 14, no. 2.
Montreal,
Canada, 1995, pp. 1137–1145.
[49] H. Inoue, “Data augmentation by pairing samples for images classifica-
tion,” arXiv preprint arXiv:1801.02929, 2018.
[50] V. Sze, Y.-H. Chen, T.-J. Yang, and J. S. Emer, “Efficient processing of
deep neural networks: A tutorial and survey,” Proceedings of the IEEE,
vol. 105, no. 12, pp. 2295–2329, 2017.
[51] Z. Wang, L. Cheng, H. Wang, W. Zhao, and X. Song, “Energy optimiza-
tion by software prefetching for task granularity in gpu-based embedded
systems,” IEEE Transactions on Industrial Electronics, vol. 67, no. 6,
pp. 5120–5131, 2019.
[52] Q. A. Al-Haija, C. D. McCurry, and S. Zein-Sabatto, “Intelligent self-
reliant cyber-attacks detection and classification system for iot communi-
cation using deep convolutional neural network,” in Selected Papers from
the 12th International Networking Conference: INC 2020 12. Springer,
2021, pp. 100–116.
[53] D. Petrov and T. M. Hospedales, “Measuring the transferability of
adversarial examples,” arXiv preprint arXiv:1907.06291, 2019.
[54] M. M. Leonardo, T. J. Carvalho, E. Rezende, R. Zucchi, and F. A.
Faria, “Deep feature-based classifiers for fruit fly identification (diptera:
Tephritidae),” in 2018 31st SIBGRAPI conference on graphics, patterns
and images (SIBGRAPI).
IEEE, 2018, pp. 41–47.
[55] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
recognition,” in Proceedings of the IEEE conference on computer vision
and pattern recognition, 2016, pp. 770–778.
[56] A. Khetan and Z. Karnin, “Prunenet: Channel pruning via global
importance,” arXiv preprint arXiv:2005.11282, 2020.
[57] M. Feurer, A. Klein, K. Eggensperger, J. Springenberg, M. Blum, and
F. Hutter, “Efficient and robust automated machine learning,” Advances
in neural information processing systems, vol. 28, 2015.
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4747893
Preprint not peer reviewed
