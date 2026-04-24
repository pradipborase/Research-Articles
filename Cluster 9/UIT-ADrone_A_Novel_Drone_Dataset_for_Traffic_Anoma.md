# UIT-ADrone_A_Novel_Drone_Dataset_for_Traffic_Anoma.pdf

## Page 1

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
1
UIT-ADrone: A Novel Drone Dataset for Traffic
Anomaly Detection
Tung Minh Tran
, Tu N. Vu
, Tam V. Nguyen
, Khang Nguyen*
Abstract—Anomaly detection plays an increasingly important
role in video surveillance and is one of the issues that has
attracted various communities, such as computer vision, machine
learning, and data mining in recent years. Moreover, drones
equipped with cameras have quickly been deployed to a wide
range of applications, starting from border security applications
to street monitoring systems. However, there is a notable lack of
adequate drone-based datasets available to detect unusual events
in the urban traffic environment, especially in roundabouts, due
to the density of interaction between road users and vehicles.
To promote the development of anomalous event detection with
drones in the complex traffic environment, we construct a novel
large-scale drone dataset to detect anomalies involving realistic
roundabouts in Vietnam, covering a large variety of anomalous
events. Traffic at a total of three different roundabouts in
Hochiminh city was recorded from a camera-equipped drone.
The resulting dataset contains 51 videos with total data traffic of
nearly 6.5 hours, captured across 206K frames with ten abnormal
event types. Based on this dataset, we comprehensively evaluate
the current state-of-the-art algorithms and what anomaly detec-
tion can do in drone-based video surveillance. This study presents
a detailed description of the proposed UIT-ADrone dataset,
along with information regarding data distribution, protocols for
evaluation, baseline experimental results on our dataset and other
benchmark datasets, discussions, and paves the way for future
work. The dataset is available online for non-commercial research
at https://uit-together.github.io/datasets/UIT-ADrone/.
Index Terms—Traffic Anomaly Detection, Benchmark, Object
Detection, Drone-based Surveillance, Convolutional Neural Net-
works.
I. INTRODUCTION
Unusual event detection is an active research topic in
the fields of image processing and computer vision, which
has attracted considerable attention from both academia and
industry due to its many applications in real life. It is note-
worthy that the detection of abnormal events such as traffic
collisions, violations, traffic accidents, fights, and crimes is one
of the most crucial research topics of smart city transportation
management systems in recent years.
An anomaly/outlier can be identified as activities or events
that differ from what is expected, common, or normal [1]-[2].
That means it deviates significantly or has a low probability
of occurring from some concept of normal such as animals
Tung Minh Tran, Tu N.Vu, Khang Nguyen (*corresponding author)
are
with
the
University
of
Information
Technology,
Ho
Chi
Minh
City, Vietnam and Vietnam National University, Ho Chi Minh City,
Vietnam,
Quarter
6,
Linh
Trung
Ward,
Thu
Duc
District,
Ho
Chi
Minh City (e-mail: tungtm.ncs@grad.uit.edu.vn; 18520184@gm.uit.edu.vn;
khangnttm@uit.edu.vn).
Tam V.Nguyen is with the Department of Computer Science, University
of Dayton, 300 College Park, Dayton, OH 45469, United States (e-mail:
tamnguyen@udayton.edu).
running onto the roadway, truck accidents, stalled vehicles in
transportation systems, defective products in the manufactur-
ing industry, and the presence of a tumor in medicine. Thus,
there is no fixed definition of anomalous actions or events in all
domains because the abnormality definition changes according
to various application contexts, i.e., time, place, and scenarios.
For instance, a person running at a park is usually a normal
behavior but an abnormal event in other locations such as a
mall. Likewise, vehicles stopped near traffic lights are normal
events when the traffic signal is red; however, they may be
considered anomalous if the traffic light is green.
In recent years, unusual event detection has been a cru-
cial component of the intelligent city transportation manage-
ment system, primarily focusing on solving minority, unpre-
dictable/uncertain, and rare events. It should be noted that
detecting traffic anomalies involves multiple kinds of viola-
tions of regulations, such as driving in the wrong direction,
illegal parking, car/motorcycle accidents, cyclist running on
a pedestrian sidewalk, walking, fighting, robbing, and acts
of vandalism. This is still a challenging problem due to
the complex traffic environment, lightning conditions, dy-
namic weather conditions, lack of high-quality data, and the
complexity of the traffic scene. Due to recent considerable
technological advancements, there is rapid growth in video
surveillance networks that provide safety and security in
public and private places such as airports, streets, subway
stations, hospitals, colleges, shopping malls, banks, compa-
nies, government buildings, and private homes. Moreover,
drones are increasingly employed in various domains related
to agriculture, the construction industry, border security, traffic
monitoring system, and disaster area investigation.
When it comes to traffic surveillance systems, developing
a the large dataset has become a challenge because abnormal
objects are usually small, inter-object occlusions, and their vi-
sual features are not easily distinguishable, especially anomaly
datasets from drone-based video surveillance to enhance public
safety under real-world conditions. The main reason is that
anomalous events occur infrequently and rarely due to the
dependence on the changing visual context and the difficulty,
unexpected cost, and laboriousness of sample collection in
real-life situations. As a result, real-world anomaly datasets
are severely imbalanced since the number of anomalies is
much smaller than that of normal data. This problem leads
to insufficiently labeled anomalous data, including suspicious
human activities via training.
Motivated by the aforementioned challenges and the in-
creasing demand for public safety and security, we particularly
introduce a novel benchmark dataset captured by an aerial
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 2

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
2
drone focusing on anomaly detection that is relevant to road
traffic situations. Moreover, a comparative study with existing
state-of-the-art methods is also conducted in order to provide
a challenging benchmark for real-time object detection and
anomaly detection in aerial videos. Furthermore, to overcome
the shortage of labeled anomaly data and to design a method
that can extract meaningful features to effectively represent
information from surveillance videos in a reasonable time
frame, we propose a combination of deep transfer learning
with unsupervised fine-tuning for anomaly detection from
drone-based surveillance sequences. Transfer learning is based
on a model trained with large-scale datasets from action
recognition; that is, the convolutional neural networks trained
on a particular dataset may be fine-tuned for a new dataset
even if the scope is different without the need for relearning
or providing new datasets. For example, a model that learned
to identify trucks in a video stream can detect unseen cars
without relearning the process.
The remainder of the paper is organized as follows. We first
deliver related work on anomaly detection and review previous
anomaly datasets captured by an aerial drone in Section II.
We then detail the novel outlier detection relationships of our
dataset in Section III. After that, experimental settings and
several analytical experiments, including quality comparisons,
are reported in Section IV. We then discuss the quantitative
results and address the challenges associated with drone-view
images in Section V. Finally, the paper is concluded in Section
VI.
II. RELATED WORK
Detecting anomalous traffic events is a challenging prob-
lem in computer vision as it involves object detection, ob-
ject tracking, and motion detection. To address the problem
where anomalies only occupy a small amount of collected
data, contrasting to normal data patterns that account for an
overwhelming proportion of the data in various real-world
applications. In this aspect, we review some methodologies
that are closely related to deep learning drone-based video
surveillance as well as existing drone-based datasets for object
detection and anomaly detection tasks.
A. Methodologies for Anomaly Detection in Traffic Surveil-
lance Videos
Concerning anomaly analysis in the traffic monitoring sys-
tem, the main approach to anomaly problems using deep mod-
els consists of unsupervised and weakly supervised learning
methods due to the limitations in the availability of anno-
tated anomalous instances. Note that unsupervised learning
techniques are used to detect abnormal events in surveillance
videos, in which only normal data are available in the train-
ing step because anomalous events are diverse and difficult
to capture. As a result, the number of anomalous samples
collected for these methods needs to be increased compared
with the normal objects. On the contrary, weakly supervised
video anomaly detection methods that concentrate on train-
ing with numerous normal samples and a small number of
category labels of unusual data patterns significantly improve
learning accuracy compared to full, unsupervised approaches.
In particular, a comprehensive review of [3] focused solely
on traffic anomalies. This survey presented different types of
modern deep learning techniques applied in video clips to
understand traffic violations and abnormalities in road traffic
scenarios involving vehicles, pedestrians, and their interactions
with the environment. Furthermore, this study reviewed com-
puter vision-based methods, frameworks, their applicability,
implementation details, and limitations, discussed challenges,
compared various benchmark datasets, identified gaps, and
suggested future research directions. Next, in the work of [4],
U-Net used a generator to predict the next frame to detect
anomalies in surveillance videos. After that, an optical flow
constraint was proposed for the objective function constraining
in terms of appearance and motion to ensure motion consis-
tency for regular events in the training set to boost anomaly
detection performance.
Moreover, it also used adversarial training to discriminate
whether the prediction was actual or fake. In another one,
[5] proposed a framework that dissociated spatial information
and motion information using a two-stream architecture for
video anomaly detection. In addition, the model utilized both
reconstruction and prediction as auxiliary tasks for spatial
and motion streams. This framework contained three key
components. Firstly, the first frame of the input video clips was
fed into the spatial autoencoder network to detect anomalous
objects with spatial features (e.g., scene and appearance). The
given individual frame was encoded to a mid-level appearance
representation by using the spatial encoder. Secondly, a motion
autoencoder generated an RGB difference by inputting consec-
utive video frames, which could learn the temporal regularity.
Moreover, its captured feature representation contained essen-
tial motion information. Thirdly, variance-based attention in
temporal autoencoder automatically assigned the importance
weight to the moving part of video clips.
Concerning anomaly detection in aerial traffic surveillance,
not much work has been done previously on unusual event
detection for drone-based surveillance sequences. To be more
detailed, A hybrid approach of [11] proposed to integrate
space–time trajectories and semantic information of objects to
build high-level knowledge for extracting complicated critical
activities and events from drone-based video surveillance. In
another work, [12] first classified safety-related abnormalities
into three groups: (1) Vehicles commit dangerous or illegal
lane-changing behaviors; (2) Vehicles slow down or stop un-
expectedly or abruptly, and (3) Vehicles blocked by vehicles in
the crossing directions. Then, a functional approach was pro-
posed to model temporal relations of time-to-collision safety
indicators to detect safety-related anomalies from drone video
surveillance. Next, an approach was made in [13] and proposed
an architecture based on deep learning for contextual anomaly
detection called CADNet. This method worked based on a
variational autoencoder (VAE) with a context subnetwork by
exploiting contextual information related to the environment
from aerial video surveillance to find point anomalies and
contextual anomalies. Then, [18] proposed an unsupervised
learning method based on deep end-to-end architecture for
the detection of anomalies from drone-based surveillance. This
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 3

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
3
method used only normal samples for the training phase, and
the optical flow representations of abnormal samples were
generated from consecutive original images in the testing
phase. Most recently, [14] introduced a method of anomaly
detection in aerial videos using transformers by an encoder-
decoder architecture called ANDT. This framework aimed
to treat adjacent frames as a sequence of triplets and then
implemented a Transformer encoder to learn a spatio-temporal
feature from the video sequence. Afterward, a decoder was
applied to combine with the encoder to predict the next frame.
Furthermore, ANDT focused solely on normal data in the
training phase and identified an unknown or unpredictable
event as an anomaly in the test phase.
B. Object Detection Models
We conduct a review of the literature related to real-
time object detectors. As we can observe, real-time object
detection plays an essential role in the field of computer vision
to detect people, cars, bicycles, boats, and other objects in
various contexts, such as traffic surveillance, robotics, and
medical image analysis. In recent years, the top deep learning
based object detection frameworks were divided into two main
categories, including one-stage architectures (e.g., YOLO [6],
YOLOF [21], YOLOR [22], YOLOX [23], and YOLOv7 [25])
and two-stage architectures (e.g., Faster-RCNN [7]).
With regard to the one-stage-based methods, the YOLO
[6] series is a representative one-stage network to enhance
high accuracy and real-time speed. After that, this method
continued to inspire further researches by making subsequent
versions, and the detection performance improved steadily.
Notably, the YOLO series has attracted considerable attention
in the field of computer vision and various researchers in
recent years. In particular, the architecture of YOLOF [21]
consists of three main components: Backbone, Encoder, and
Decoder. YOLOF extracts only feature C5 level features from
the backbone, without using extra features at other levels.
Moreover, YOLOF replaces the RPN with a Dilated Encoder
instead of using the Feature Pyramid Network (FPN) to extract
features. In this architecture, the Dilated Encoder is designed
to enlarge the receptive field. Additionally, YOLOF solved
this imbalance problem on Single-in-Single-out encoders by
applying a Uniform Matching strategy, marking the indexes of
k nearest anchor points and k prediction boxes closest is posi-
tive for each ground-truth box. In addition, Uniform Matching
ensures that all ground-truth boxes can be matched to the same
number of positive anchors uniformly, regardless of their sizes.
Next, YOLOR [22] is a useful unified model for multitasking
purposes, especially real-time object detection. This network
encoded implicit knowledge and explicit knowledge together
and enabled the learned model to generate a unified representa-
tion to serve multiple tasks. Moreover, the kernel space in this
framework was applied, which could be translated, rotated, and
scaled to align each output kernel space of neural networks,
prediction refinement, and multitask learning into the implicit
knowledge learning process, and verified their effectiveness.
Then, YOLOX [23] adopts the architecture of YOLOv3 [24]
with DarkNet53 backbone by replacing the YOLO detect
head with decoupled one to improve the convergence speed
greatly. Moreover, the anchor-free and advanced labels were
also assigned to this framework to improve object detector
performance. In another one, TPH-YOLOv5 [30], another
variant of YOLOv5 [26], aims to detect multi-scale objects
by incorporating an additional prediction head. The model
leverages Transformer Prediction Heads and Convolutional
Block Attention Model to locate attention regions in dense
object scenarios. Furthermore, various strategies such as data
augmentation, multiscale testing, multi-model integration, and
leveraging extra classifiers are employed in this framework to
enhance the model’s performance. Recently, YOLOv7 [25] is
the trainable bag-of-freebies method to enhance the accuracy
of real-time object detection. This method modified a more
efficient ELAN module based on the YOLOv5 [26] algorithm
and proposed a framework for auxiliary head training to
enhance feature extraction, which improved accuracy and high
performance.
Regarding the two-stage-based methods, Faster R-CNN
[7] is a CNN-based method improved from the R-CNN
architecture. The significant contribution of this model is the
inference time at an approximate real-time speed. Faster R-
CNN uses a pre-trained CNN model to generate a feature
map and bypasses the traditional region proposal algorithm
of selective search. This feature map is then fed to the region
proposal network (RPN) to identify the area recommendations
and create pre-defined boxes called anchor boxes. RPN is an
alternative recommendation network to the selective search
method. The anchor boxes are further classified and regressed.
In addition, the non-maximum suppression (NMS) algorithm
selects the overlapping anchors to ensure that the proposals do
not contain overlapping boxes.
Concerning extensive experiments for object detection tasks,
[32] conducted to investigate the impact of different deep
learning object detection methods, including Faster R-CNN
[7], RFCN [33], SNIPER [34], SSD [35], YOLOv3 [24],
RetinaNet [36], and CenterNet [37] for object detection tasks
in aerial images from drones. It has been demonstrated that
the YOLO method is both feasible and effective based on
experimental results, and the YOLO series is considered the
optimal choice for real-time object detection applications.
Next, [38] proposed an efficient approach (YALA) for learning
to detect unseen (missing) objects. In this framework, a dual-
level of deep networks was designed to efficiently detect
difficult objects in images by adopting Faster RCNN [7] to
train in the detection model, then training another Faster
RCNN model to tackle the unseen and challenging objects.
Moreover, this pipeline leverages deep learning-based multi-
scale detection for better performance. Further improvement
of YALA was proposed in the study [39], named YADA to
improve object detection performance in images. This frame-
work consisted of two stages, namely, (1) data preparation
during pre-training, and (2) data residual post-training. More
specifically, lucid data synthesizing was applied in the data
preparation to generate data by exploiting hard examples and
embedding them in the same contextual locations. Further, a
dual-level deep network leveraged with these generated data
was used by modifying Faster-RCNN [7] to train in a detection
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 4

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
4
model. After that, another Faster-RCNN model was trained to
detect hard objects in images.
C. Related Benchmark Drone-based Datasets
This section introduces the public benchmark anomaly
datasets developed by researchers in drone-based video
surveillance, dealing with the complex traffic environment, as
seen in Table I. Some of the mentioned datasets from aerial
images focusing primarily on road traffic surveillance have
been studied and published in recent years [15], [16]. However,
in anomaly event detection, there are some drone datasets that
exist [14], [17], [18], [19], [20]. To better understand different
drone datasets, we briefly summarize them as well as are
publicly available for research and useful for the comparison
of different methods as follows.
1) Drone-based datasets for vehicle detection:
VisDrone dataset [29] consists of 10,209 images taken
from drones in various locations at different heights for object
detection task. There are ten predefined categories of interest,
including pedestrian, people, bicycle, car, van, truck, tricycle,
awning-tricycle, bus, and motor. Moreover, some rare special
vehicles are classified as “ignored regions” and “others,” but
they are not used in the evaluation. Out of 10,209 images,
6,471 images are divided into training, 548 for validation,
1,610 images for test-dev set, and 1,580 images for testing.
Furthermore, more than 540k bounding boxes of targets are
annotated with ten predefined classes.
MONET dataset [31] contains 53K images with 162K an-
notated bounding boxes captured by drones both day and night
in a rural area near the city of Nicosia, Cyprus. Furthermore,
There are three types of targets, including vehicle, person, and
ignore. Moreover, the dataset has many annotations that can
also be used for multiple object-tracking problems.
UAVDT dataset [9] contains 100 videos with a total
duration of more than 10 hours using drone cameras for object
detection, single object tracking, and multiple object tracking
problems. The video sequences were recorded at 30 frames per
second (fps), with 1080 × 540 pixels resolution. Moreover, it
was recorded at various locations in urban areas, including
squares, arterial streets, toll stations, highways, crossings, and
T-junctions. Additionally, the videos cover different lighting
conditions due to the time of the day and the weather condi-
tions. In addition, approximately 80,000 frames in this dataset
are labeled for more than 2,700 vehicles with 0.84 million
bounding boxes.
Stanford Drone dataset [15] comprises about 10,000 tra-
jectories with 929,499 samples in total. It was recorded from
a drone’s perspective with a length of 9 hours at eight unique
locations on the Stanford Campus. This dataset analyzes
human trajectories in crowded scenes such as pedestrians,
bicycles, cars, skateboards, carts, and buses. Moreover, it has
a high percentage rate of labeled pedestrians and cyclists, and
their trajectory in time and space is also identified. At the same
time, only approximately 7% of the labeled targets are cars.
DroneSURF dataset [16] consists of 200 videos of 58
subjects captured by a drone camera for the problem of face
recognition. The dataset includes a total of 411,451 samples.
Additionally, video footage has some challenges, such as
motion, variations in pose, illumination change, background,
altitude, and resolution. In addition, more than 786,000 face
annotations are also provided for performance evaluation.
2) Drone-based datasets for anomaly detection:
Mini-Drone Dataset [17] consists of 38 videos recorded
by a Phantom 2 drone flying at low altitude in a parking
lot for privacy protection. These videos are high resolution,
with a duration ranging from 16 to 24 seconds each. The
videos in this dataset are divided into three situation categories:
normal, suspicious, and abnormal. Noticeably, these types are
almost all identified by the actions of the persons involved in
videos. More specifically, the normal actions in these videos
relate to several events, such as people walking, getting in
their cars, or parking correctly. The unusual activities include
people fighting, a person falling down, and stealing. The
suspicious cases represent situations where people behave
suspiciously, which could distract the surveillance staff. For
example, a person loitering in a parking lot can be considered
as looking for a car/motorcycle to steal. Furthermore, the
dataset comprises 15 training video sequences (9,497 frames)
and 23 testing video sequences (13,798 frames). The data set is
challenging because of changes in illumination, environmental
variations, and different altitudes between videos. In addition,
the ground truth annotations are provided for each video in
the form of bounding boxes for each person and vehicle in
each frame, which helps evaluate the performance.
UTT Drone dataset [18] was captured by Mavic air two
from the DJI series with a total of 14,021 video frames (8,933
for training and 5,088 for testing). It contains seven folders for
the training and 12 folders for the test. Particularly, the train
folders contain only normal events, such as people walking on
the lawn, whereas the test folders consist of both normal and
abnormal events. Unusual activities include running, fighting,
and falling. However, the number of videos and the full video
duration were not mentioned in detail in the original paper.
Brutal Running dataset [19] consists of 1,000 samples
in total captured by a Phantom 4 pro drone. There are 340
training samples and 660 samples for testing. The normal
event consists of a girl walking outside, whereas the anoma-
lous event occurs while running. Nevertheless, the number
of videos, situations, and video length were not specifically
mentioned in the original article.
AU-AIR-Anomaly dataset [20] contains eight aerial videos
for more than 2 hours for traffic surveillance. Moreover, these
videos were primarily captured at Skejby Nordlandsvej and
P.O Pedersensvej roads (Aarhus, Denmark). Noticeably, this
dataset was originally created for object detection tasks. Based
on the dataset, [13] annotated various abnormal events to
detect anomalies in aerial videos. In addition, there are a
total of 32,823 video frames covering four anomalous events,
namely a car on a bike road, a parked van in front of a
building, a person on the road, and a bicycle on the road.
Furthermore, frame-level ground truth is provided to evaluate
the performance of state-of-the-art anomaly detection methods.
Drone-Anomaly dataset [14] has a total of 59 untrimmed
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 5

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
5
TABLE I: Comparison of publicly available drone-based datasets for anomaly detection
Dataset attribute
Mini Drone [17]
UTT Drone [18]
Brutal Running [19]
AU-AIR [20]
Drone-Anomaly [14]
UIT-ADrone (Ours)
Dataset Size
No. of videos
38
–
–
1
59
51
No. of frames
23,295
14,021
1,000
32,823
87,488
206,194 frames
Length
16s - 24s per video
–
–
2 hours
–
6.48 hours
Situations
parking lot
campus
–
roads
highways, roundabouts, etc.
roundabouts
Categories
People
✓
✓
✓
✗
✗
✓
Vehicles
✗
✗
✗
✓
✓
✓
Animals
✗
✗
✗
✗
✓
✗
No. of anomalous events
3
3
1
4
–
10
Resolution
224 × 224
227 × 227
227 × 227
1920 × 1080
640 × 640
1920 × 1080
Altitude
low altitude
low altitude
–
10m - 30m
–
50m - 70m
Year
2015
2021
2021
2021
2022
2023
videos that are captured at seven different scenes in real-world
environments, including highways, crossroads, bike round-
abouts, vehicle roundabouts, railway inspection, solar panel
inspection, and farmland inspection. Notably, aerial videos in
this dataset were collected from YouTube and Pexels. Addi-
tionally, the dataset comprises 37 training video sequences
and 22 testing sequences with various real-world anomalous
events. In addition, there are 87,488 video frames (51,635 for
training and 35,853 for testing) in total, with each frame of
640×640 resolution and a frame rate of 30 frames per second.
Moreover, the ground truth annotations are provided for each
testing video in the form of each anomalous event in each
frame, which helps evaluate the performance. Nonetheless,
the number of anomalies and the length of videos were not
detailed in the original paper.
III. DATASET DESCRIPTION
To tackle the limited availability of drone-based datasets
with real anomalies for traffic anomaly detection, we construct
a drone-view anomaly detection dataset named UIT-ADrone.
The drone took the video clips we chose to capture at
realistic roundabouts, which are the most common place to
capture all road users present in a scene. Furthermore, the
interaction between traffic participants is particularly high at
these intersections, especially motorcycles. Our dataset has a
wide range of challenges. In more detail, the object scale in
aerial images varies dramatically due to the substantial change
in flight altitude and distance between the drone and objects of
interest. Additionally, drone-based video surveillance objects
(e.g., cars, bicycles, motorcycles) have illumination changes,
occlusion of independently moving objects, and complex back-
grounds. In addition, anomalies mostly occur for a short span
of time in video drones.
A. Data Acquisition
We have conducted videos captured by the aerial perspective
with a camera to collect practical traffic data for detecting
traffic abnormalities in Hochiminh city, Vietnam. The used
drone is a DJI MAVIC MINI 2, recording at 30 frames per
second (fps), with a resolution of 1920 × 1080 pixels ranging
from 50 to 70 meters in height at different times of the
TABLE II: Statistics of the UIT-ADrone (Ours) dataset.
Types of abnormal events
Number of actions
Crossing the road at the wrong line
80
Walking under the street
344
Driving in the wrong roundabout
686
Driving on the sidewalk
145
Illegal left turn/ turn right
28
Illegal parking in the street
225
Carrying bulky goods
144
Parking on the sidewalk
68
Driving in the opposite directions
214
Falling off motorcycles
1
day. More specifically, the videos of the drone are recorded
at two roundabouts on the campus of the Vietnam National
University, Ho Chi Minh City, and at one public roundabout
in Ho Chi Minh City. Note that the public roundabout has an
especially high traffic volume, with a variety of motorbikes on
the streets. Moreover, Figure 1 shows a scene at the roundabout
in our dataset.
B. Dataset Statistics
The UIT-ADrone dataset consists of 51 videos with a total
of 206,194 extracted video frames covering various anomalous
events. The entire video is approximately 6.50 hours long,
recorded in complex real-world scenarios, and they pose
significant new challenges, such as complex scenes, high
density, occlusion of moving objects, lighting conditions, small
objects, and large camera motion. Furthermore, it contains
ten abnormal events related to various types of violations of
regulations, including crossing the road at the wrong lane,
walking under the street, driving in the wrong roundabout,
illegally driving on the sidewalk, illegal left turn/ turn right,
illegally parking in the street, carrying bulky goods, parking
on the sidewalk, driving in the opposite directions, and falling
off motorcycles.
In Table I, we compare the UIT-ADrone dataset with current
public datasets for anomaly detection problems, which are
similar to the UIT-ADrone dataset: Mini-Drone [15], and
UTT Drone [18]. It is essential to notice that the datasets
in this table only provide three types of abnormal events,
involving some pedestrians and cars. Therefore, there is not
much interaction between road users and vehicles (e.g., cars,
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 6

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
6
Fig. 1: Visualization of traffic scenes included in the UIT-ADrone (Ours) dataset.
buses, trucks, bikes), as well as interactions between objects
of interest, especially motorcycles. In contrast to the existing
datasets, the UIT-ADrone dataset consists of 10 different types
of anomalous events and a more representative distribution of
the types of road users in public urban interchanges. Moreover,
the videos captured by a drone have a duration of nearly 6.50
hours of data. Furthermore, detailed descriptions of anomalous
event types in our dataset are given in Table II. Notably, a
frame can have more than one outlier event because of the
huge diversity of situations that are encountered on real-world
roundabouts, especially motorbikes. Thus, our dataset is much
more suitable for detecting abnormal events from drone-based
traffic videos.
C. Annotation
To generate ground-truth data for the purpose of evaluat-
ing different models to detect traffic anomalies, we use a
tool called Supervisely assign frame-level labels. This tool
is browser-based and supports advanced functions, such as
drawing a bounding box or tracking the objects of interest
in a video drone. Since the frames we label are sequential
at a frame rate of 30 fps, and the position of objects of
interest changes little from frame to frame, Supervisely is an
easy-to-use tool for annotating challenge data. Furthermore,
some screenshots of the Supervisely tool are illustrated in
Figure 2 and Figure 3, respectively. This tool is available
at https://supervise.ly/. In addition, the UIT-ADrone dataset
comprises bounding boxes for the training and testing set
for object detection, following the format of the MS COCO
dataset [27], which is standard for object detection. Therefore,
our dataset contains train.json and test.json for the training and
testing set, respectively. For anomaly detection, testing labels
are organized as arrays (.npy). It means the video is equal to
the array. The indexes for frames start at 0 and end at a total
of frames subtraction of 1. Each element in the array is set to
0 as normal or 1 as abnormal. Notably, only normal data are
available in the training step for these unsupervised tasks in our
study. Additionally, we also carry out cross-checking between
annotators to check for error labels based on the consensus of
annotators.
IV. PROTOCOLS AND BASELINE RESULTS
In this section, we demonstrate experimental results to
verify the challenges and effectiveness of our dataset based
on a set of state-of-the-art algorithms. Concretely, protocols
and baseline results have been provided for the task of object
detection and traffic anomaly detection on our dataset and two
public datasets. The performance of the methods on standard
datasets for both of these tasks is illustrated in Table III,
and Table IV, respectively. Furthermore, we also conduct
extensive cross-dataset experiments to investigate the cross-
dataset adaptability of our dataset. The experimental outcomes
are presented in Table V and Table VI, respectively.
A. Protocols
The proposed UIT-ADrone dataset is downsampled and
divided into the number of abnormal and normal snippets
for training and test sets. In particular, the training set only
includes normal snippets, whereas the test set consists of
normal and abnormal snippets. The resulting dataset has a total
of 1,497 snippets (592 for training and 905 for testing), or the
equivalent of 206,194 video frames. In more detail, there are
59,186 frames for the training set and 147,005 frames for the
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 7

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
7
Normal
Scene 1
Scene 2
Abnormal
Fig. 2: Example images from two traffic scenes of the UIT-ADrone dataset by using Supervisely. The left column shows normal
frames, and the right column demonstrates abnormal frames. Note that, red boxes denote anomalies in abnormal frames. Please
zoom by 400% in the electronic version.
Scene 1
Scene 2
Fig. 3: Image samples for object detection from two traffic scenes of the UIT-ADrone dataset by using Supervisely annotation
tool. Please zoom by 400% in the electronic version.
test set. Moreover, there are 63,485 ground truth annotations
provided for testing snippets in the form of bounding boxes
around each abnormal event in each extracted video frame.
Noticeably, each anomalous event (object) is also labeled with
a tracking number. Furthermore, a single frame can have more
than one labeled anomaly.
B. Experimental Results
In this section, we discuss the experimental results of our
UIT-ADrone dataset with two common tasks: Object detection
and Anomaly Detection. Based on related works, thoroughly
empirical studies with five object detectors consisting of Faster
R-CNN [7], YOLOF [21], YOLOR [22], YOLOX [23], and
YOLOv7 [24] are performed on the UAVDT dataset [9]
and our dataset for the object detection task. Moreover, we
also conduct an evaluation of three current state-of-the-art
anomaly detection algorithms based on deep architectures,
namely Future Frame Prediction [4], Anomaly Detection with
Transformers (ANDT) [14], and Spatio-Temporal Dissociation
[5] on two anomaly datasets including the Drone-Anomaly
[14] dataset and our dataset, which follow the same setup as
other similar unsupervised video anomaly detection studies.
Metrics. We use a frame-based receiver operating charac-
teristic (ROC) curve, and the corresponding area under the
curve (AUC) [8] to evaluate the performance of experimental
methods for anomaly detection problems. Additionally, mAP
[10] is a very important metric used to measure object de-
tection performance in our benchmark. mAP metric will be
calculated by using official MS-COCO api. It should be noted
that the higher the value of AUC, as well as the value of mAP,
is, the better the model’s performances will have. Furthermore,
Figure 4 presents the results of our experiments on the Drone-
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 8

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
8
TABLE III: Comparison of experimental methods in terms of average precision values on the UIT-ADrone (Ours) and the
UAVDT dataset (%). The results of state-of-the-art methods on the UAVDT dataset are denoted by gray cells.
Method
APbus
APtruck
APcar
APtricycle
APvan
APbike
APped
APmotorbike
AP50
AP75
mAP
30.90
26.30
23.00
16.00
6.80
1.40
5.00
6.40
31.90
11.30
14.50
Faster R-CNN [7]
7.80
1.90
27.90
–
–
–
–
–
22.30
12.90
12.50 1
31.80
26.00
24.30
18.30
9.80
1.20
2.80
5.30
32.80
11.60
14.90
YOLOF [21]
1.70
1.20
26.50
–
–
–
–
–
20.90
7.80
9.80
32.60
28.80
26.90
21.20
11.20
1.19
5.40
8.31
35.50
13.70
16.90
YOLOR [22]
11.30
2.65
42.90
–
–
–
–
–
31.00
21.10
19.00
30.00
21.00
19.30
13.60
3.50
1.30
2.60
5.30
26.50
9.40
12.10
YOLOX [23]
5.30
0.00
21.30
–
–
–
–
–
20.00
6.10
8.90
28.30
29.20
26.20
17.80
8.28
0.27
3.50
6.14
34.40
11.50
15.00
YOLOv7 [24]
23.00
3.14
34.40
–
–
–
–
–
37.00
20.02
20.10
1 The result was cited from [28].
Anomaly [14] and our datasets in terms of the ROC-AUC
metric at the frame level. Moreover, we provide snapshots of
some correct cases and failure cases on our dataset from our
experiments, as seen in Figure 5.
Object detection. Table III uses mAP metric to show a
performance comparison of various algorithms, including the
Faster R-CNN [7], the YOLOF [21], YOLOR [22], YOLOX
[23], and YOLOv7 [24] models for object detection task on the
UIT-ADrone (Ours), and the UAVDT [9] datasets. In general,
out of five well-known methods, the mAP of the YOLOR
[22] on our dataset, and that of the YOLOv7 [24] method
on the UAVDT dataset [9] is the highest at nearly 17.00
% and at just over 20.00 %, respectively. In contrast, the
figure of the YOLOX [23] method is the lowest on the UIT-
ADrone and the UAVDT datasets at nearly 9.00 % and at
roundly 12.00 %, respectively. Moreover, the experiments also
show that one-stage YOLO family detectors perform well in
contexts of aerial images rather than two-stage detectors such
as Faster R-CNN [7]. As regards the UIT-ADrone dataset, the
figures of the YOLOR [22] model surpass the other state-
of-the-art methods in most of the classes on the UIT-ADrone
dataset, ranging from about 1.00 % to nearly 4.00%. However,
this method achieves the lowest result on APbike class at
nearly 2.00 %. Furthermore, the mAP of the YOLOv7 [24]
method is slightly higher than the Faster R-CNN [7] model
at nearly 15.00 % and 14.50 %, respectively. Regarding the
UAVDT dataset [9], it is clear that the largest percentage of the
YOLOv7 [24] method accounts for 20.10 %, and this figure
is slightly higher than that of the YOLOX [23] method at
19.00 %. Moreover, compared with the rest of the models,
the performance result of the YOLOR [22] method is better
across all classes, ranging from about 2.60 % to over 20.00
%. On the other hand, the percentage of the YOLOX [23],
and the YOLOF [21] methods are the lowest at approximately
9.00 % and at roundly 10.00 %, respectively. Notably, the
object detection result of the YOLOX [23] method on APtruck
class is 0.00 %. From the results presented in this table, it
can be seen that the YOLOR [23] and the YOLOv7 [24]
models obtain the best object detection performance for both
single and multiple object detection compared to the existing
methods on two benchmarks. Interestingly, the performance
of the YOLOv7 [24] method on the UAVDT dataset [9] is
higher than that of the YOLOR [23] method; however, its
performance is less than the YOLOR method on our UIT-
TABLE IV: Performance comparison of anomaly detection
methods in terms of average AUC metric at frame level on
the Drone-Anomaly [14] and our datasets (%).
Method
AUC
UIT-ADrone (Ours)
Drone-Anomaly [14]
Future Frame Prediction [4]
53.56
64.00
ANDT [14]
60.50
82.201
Spatio-Temporal Dissociation [5]
57.05
79.50
1 The result was quoted from [14] for the roundabout scene.
ADrone dataset. Theoretically, YOLOR [23] is the model that
is proposed to train multi-tasks for gaining implicit knowledge
to serve other tasks. In the case of the UAVDT dataset [9],
having images captured at an angle of under 90 degrees with
the horizontal, and the objects are much smaller than our UIT-
ADrone dataset, implicit knowledge from pre-trained models
may not work well, leading to a worse performance than
YOLOv7 [24] model. The images’ context of our UIT-ADrone
dataset seems to be similar to knowledge trained on the
YOLOR [23] method; therefore, the implicit knowledge works
well. Conversely, the YOLOv7 [24] model aims to generalize
on different contexts of datasets without prior knowledge; thus,
its performance may be worse than YOLOR [23] method.
Additionally, experimental results obtained on two benchmark
datasets demonstrate the effectiveness of the YOLOv7 [24]
method in the case of less training data and faster computation.
In contrast, the YOLOR [23] algorithm requires large data
to train. Therefore, this method significantly improves the
result of common classes on two datasets. As regards the UIT-
ADrone dataset, besides the common classes, there are some
classes with small objects along with complicated calculations,
then the YOLOR [23] model gives better results. Notably, the
number of object classes detected in our dataset is almost
three times more numerous than that of object classes in the
UAVDT dataset [9] (8 classes compared to 3 classes). Still,
the YOLOv7 [24] model on the UAVDT dataset [9] has a
much higher mAP value (about 5.00 %) than the achieved
result of this method on the UIT-ADrone dataset at 20.10 %
and at 15.00 %, respectively. The detailed figures’ analysis
demonstrates that our anomaly dataset is challenging for the
current state-of-the-art algorithms for object detection tasks in
drone-based video surveillance systems.
Anomaly Detection. Table IV shows performances of
three prominent methods, namely Future Frame Prediction
[4], ANDT [14], and Spatio-Temporal Dissociation [5] on
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 9

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
9
0.0
0.2
0.4
0.6
0.8
1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0
True Positive Rate
ROC curves on the Drone-Anomaly dataset (Bike roundabout)
Spatio-Temporal Dissociation ( 
 =  0.83)
Future Frame Prediction (
 =  0.64)
AUC
AUC
(a) The visualization plot of ROC-AUC score on the Drone-
Anomaly dataset [14].
0.0
0.2
0.4
0.6
0.8
1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0
True Positive Rate
ROC curves on the UIT-ADrone (Ours) dataset
ANDT (AUC = 0.60)
Spatio-Temporal Dissociation (AUC = 0.57)
Future Frame Prediction (AUC = 0.54)
(b) The visualization plot of ROC-AUC score on the UIT-
ADrone (Ours) dataset.
Fig. 4: Experimental results of Future Frame Prediction [4], ANDT [14] and Spatio-Temporal Dissociation [5] methods based
on ROC-AUC metric at frame level of the Drone-Anomaly [14] and the UIT-ADrone (Ours) datasets.
Ground-truth: 1 (Abnormal)
Prediction: 1 (Abnormal)
Ground-truth: 1 (Abnormal)
Prediction: 1 (Abnormal)
(a) Correct cases for frame prediction on the UIT-ADrone dataset.
Ground-truth: 1 (Abnormal)
Prediction: 0 (Normal)
Ground-truth: 1 (Abnormal)
Prediction: 0 (Normal)
(b) Failure cases for frame prediction on the UIT-ADrone dataset.
Fig. 5: Correct and failure cases for anomaly prediction on the UIT-ADrone (Ours) datasets.
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 10

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
10
TABLE V: Results of cross-dataset adaptation experiments in
terms of average AUC metric at frame level on the Drone-
Anomaly and the UIT-ADrone (Ours) datasets with fine-tuning
and without fine-tuning (%).
Source →target
AUC
w/ Fine-tuning
UIT-ADrone →Drone-Anomaly [14]
83.40
Drone-Anomaly [14] →UIT-ADrone
55.30
w/o Fine-tuning
UIT-ADrone →Drone-Anomaly [14]
76.86
Drone-Anomaly [14] →UIT-ADrone
52.84
two abnormal drone datasets, namely Drone-Anomaly [14]
and UIT-ADrone based on AUC metric at the frame level.
Overall, there are considerable differences in results between
the state-of-the-art methods on these datasets. The ANDT
method’s result is the highest figure of the three prominent
methods on two datasets at over 82.00 % for the Drone-
Anomaly dataset and at 60.50 % for the UIT-ADrone dataset,
respectively. Furthermore, the ANDT method is higher than
that of the other ones ranging from about 3.00 % to over
10.00 % on two anomalous datasets. Similar to the ANDT
method, the next most substantial percentage of the Spatio-
Temporal Dissociation method is at 79.50 % for the Drone-
Anomaly dataset and at 64.00 % for the UIT-ADrone dataset.
By contrast, the figure of the Future Frame Prediction method
is the lowest on these datasets at 64.00 % for the Drone-
Anomaly dataset and 53.00 % for the UIT-ADrone dataset.
Based on the analysis of these experimental results, the results
of these well-known methods on the UIT-ADrone dataset are
much lower than the results of the Drone-Anomaly dataset.
It is clear that our dataset is very challenging due to the
complex traffic environment and diversity of anomalous data.
Obviously, the issue of anomalous event detection in drone-
based video surveillance is still challenging, depending on the
realistic conditions and environment.
Transfer Learning. Our extensive experiments aim to fine-
tune as well as without fine-tuning for detecting anomalies in
frames on cross-dataset adaptation. Detailed analysis of the
performance and its comparison in terms of AUC metric at
frame level with the state-of-the-art method, namely Spatio-
Temporal Dissociation [5] on two sources, and destination
datasets, including the Drone-Anomaly [14], and the UIT-
ADrone datasets are also reported. To be more detailed, we
first train the model on training images from the source dataset
and then perform a transfer learning setting by loading the pre-
trained weights learned from the training image in the source
dataset to continue to learn the training image patterns from the
target dataset. After that, the final weights will be evaluated
on the test set of the target dataset. By refining the learned
representations for anomaly detection, the Drone-Anomaly and
the UIT-ADrone datasets serve as source and target datasets,
respectively. Similarly, we also experiment without fine-tuning
(inference dataset B directly from the model trained on dataset
A, and vice versa) for detecting anomalies in frames on these
datasets.
Table V shows the performance evaluation of the Spatio-
Temporal Dissociation [5] method for anomaly detection in
the two sources and destination datasets, namely the Drone-
Anomaly [14] and the UIT-ADrone datasets. It is notewor-
thy that the experimental method with fine-tuning has su-
perior results to those without fine-tuning on cross-dataset
adaptation. Specifically, the performance of the setting UIT-
ADrone→Drone-Anomaly [14] with the Spatio-Temporal Dis-
sociation [5] method on the Drone-Anomaly’s test set with
fine-tuning surpasses the performance of the setting without
fine-tuning by over 6.50 %, at 83.40 % compared to at
76.86 %. Likewise, the performance of the setting Drone-
Anomaly [14]→UIT-ADrone is witnessed the same conclusion
with transfer learning experiments: the setting of fine-tuning
achieve the higher AUC score (about 2.50 %) than that of
without fine-tuning, at 55.30 % and 52.84 %, respectively.
Moreover, from the results presented in this table, we see that
the performance of the setting UIT-ADrone→Drone-Anomaly
[14] with the Spatio-Temporal Dissociation [5] method on
the Drone-Anomaly’s test set outperforms the performance
of the setting without loading the learned weights increased
by nearly 4.00 %, at 83.40 % compared to at 79.50 % of
the previous experimental result from Table IV. The learned
models can explain this outcome through the load weights
learned from the UIT-ADrone dataset, which provides signif-
icant prior knowledge because our dataset includes numerous
images captured from roundabout scenes. Although humble
AUC scores obtained from the setting without fine-tuning
compared to those with fine-tuning, the results are also pretty
good and even acceptable in the context of no training. This,
therefore, leads to better performance in small-scale datasets
like Drone-Anomaly (captured at the roundabout scene similar
to our dataset context). On the contrary, the performance of the
setting Drone-Anomaly [14]→UIT-ADrone with the Spatio-
Temporal Dissociation [5] baseline does not improve on the
test set of our dataset at 55.30 %, nearly 2.00 % lower than
the previous experimental result from Table IV of 57.00 %.
We assume the Drone-Anomaly dataset has a much smaller
number of samples than our dataset (26,377 samples compared
to 206,194 samples, according to Table VI) as well as the lack
of variety of unusual event types in the same context, resulting
in poor generalization of the trained model due to the rapid
growth of video surveillance data, especially data captured by
drone in the complex traffic environment. It is essential to note
that loading learned weights from the Drone-Anomaly dataset
generates some noise due to insufficient training data. Thus,
the trained model has difficulty continuing to learn patterns
from large-scale datasets, such as the UIT-ADrone dataset.
V. DISCUSSION
In this paper, we create an annotated aerial video dataset
consisting of 51 video sequences involving three realistic
traffic scenes. Our UIT-ADrone dataset expands the scope
of anomaly detection research in real-world applications by
covering a large variety of anomalous events with char-
acteristics in Vietnam. In addition, we extensively validate
existing methods in order to provide a benchmark for this
task. Additionally, owing to the complexity and diversity of
real-world scenarios, the most significant challenge in traffic
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 11

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
11
TABLE VI: Comparison of the number of samples between
the Drone-Anomaly [14] and the UIT-ADrone (Our) dataset.
Dataset
No. of samples
Drone-Anomaly (the roundabout scene) [14]
26,377
UIT-ADrone (Ours)
206,194
anomaly detection problems is that available data is highly
imbalanced towards normality (i.e., non-anomalous), leading
to the availability of anomalous cases may be limited and
may evolve over time due to external factors. Within such
scenarios, it is impossible to take into account all unseen
abnormal examples, so our dataset is very challenging for
well-established the-state-of-the-art methods to detect unusual
events.
According to the above experimental findings, we find that
compared with natural images, new challenges appear in aerial
images based on real scenes, including dense distribution,
miniature objects with only a few pixels, large aspect ratios,
arbitrary orientations, and camera motion. These character-
istics make deep learning models such as CNN-based and
transformer-based face challenges for aerial object detection
as well as detecting anomalous events in drone-based video
surveillance, especially the recorded surveillance footage of
dense populations in urban environments. Furthermore, small
objects are easily fooled by complex background noise in-
terference, thus, in turn, increasing the difficulty of accurate
object detection and detection of unusual events. Additionally,
anomalies in surveillance footage are difficult to anticipate, as
the prior knowledge about these anomalies is usually limited or
even unavailable. In addition, when new categories of anoma-
lies emerge, the data acquisition environments are extremely
diverse, and the labeling of training data for novel categories is
complex and prohibitively expensive. Furthermore, abnormal
event detection is more than just dependent on circumstances
and context; but also depends on the appearance of the objects
and their movements in real scenes. Moreover, challenges
in anomaly detection with massive volumes of aerial videos
include inconsistent behavior of different types of anomalies,
camera movements, variable spatial resolution due to changes
in flight altitude, and handling imbalanced distribution of
normal and abnormal data, in which normal events often
account for an overwhelming proportion. Therefore, state-of-
the-art methods are typically trained only on normal data while
being tested on both normal and abnormal data, which are
difficult to adapt to various monitoring scenarios. Furthermore,
the analysis of the extensive experiments shows the superiority
of the proposal for cross-domain adaptivity on our dataset,
in which many anomalous events with temporal dynamics
exist. It is clear that these experimental outcomes demonstrate
our dataset can apply deep learning-based transfer learning
for drone-based anomaly detection. Moreover, since the main
focus of this paper is to introduce a novel dataset for anomaly
detection in drone images, we have not yet evaluated the
accuracy of various kinds of anomalous events.
VI. CONCLUSION AND FUTURE WORK
In this work, we have presented our efforts to build a
novel dataset for real-time detection of anomalous events in
aerial traffic surveillance at three various locations in which
the primary context is roundabout. We have contributed the
large-scale dataset of aerial videos, named UIT-ADrone, with
specific applicability to detect anomalous events in the com-
plicated background and various object sizes. The proposed
dataset contains 51 original videos of 10 abnormal events
recorded on various roundabouts and at different times of the
day. Video frames are captured across over 206, 000 frames,
with 63, 485 anomalous frames annotated. Furthermore, exten-
sive empirical results performed on various publicly available
benchmarks demonstrate that it is challenging to track small
objects. The experiments show that it is feasible to detect
anomaly frames in real-life applications.
Future work will consider raising the number of envi-
ronmental contexts to increase the diversity of anomalous
event types and more experiments that can be performed by
evaluating the accuracy of different abnormal events, as well
as tracking anomalous events from the UIT-ADrone dataset.
Finally, by sharing our dataset, we hope that researchers will
push the limitations of existing methods for object detection
as well as outlier event detection in aerial videos.
ACKNOWLEDGMENT
This research is funded by Vietnam National University Ho
Chi Minh City (VNU-HCM) under grant number B2023-26-
01.
REFERENCES
[1] Chandola, Varun and Banerjee, Arindam and Kumar, Vipin,“Anomaly
detection: A survey”, ACM computing surveys (CSUR), vol. 41, pp. 1–
58, 2009.
[2] Tran, Tung Minh and Vu, Tu N and Vo, Nguyen D and Nguyen,
Tam V and Nguyen, Khang,“Anomaly Analysis in Images and Videos:
A Comprehensive Review”, ACM Computing Surveys (CSUR), vol.55,
2022.
[3] Santhosh, Kelathodi Kumaran and Dogra, Debi Prosad and Roy, Partha
Pratim,“Anomaly detection in road traffic using visual surveillance: A
survey”, ACM Computing Surveys (CSUR), vol. 53, pp. 1–26, 2020.
[4] Liu, Wen and Luo, Weixin and Lian, Dongze and Gao, Shenghua,“Future
frame prediction for anomaly detection–a new baseline”, Proceedings
of the IEEE conference on computer vision and pattern recognition, pp.
6536–6545, 2018.
[5] Chang, Yunpeng and Tu, Zhigang and Xie, Wei and Luo, Bin and Zhang,
Shifu and Sui, Haigang and Yuan, Junsong, “Video anomaly detection
with spatio-temporal dissociation” Pattern Recognition, Elsevier, vol.
122, pp. 108213, 2022.
[6] Redmon, Joseph and Divvala, Santosh and Girshick, Ross and Farhadi,
Ali,“You only look once: Unified, real-time object detection”, Proceed-
ings of the IEEE conference on computer vision and pattern recognition,
pp. 779–788, 2016.
[7] Girshick, Ross, “Fast r-cnn”, Proceedings of the IEEE international
conference on computer vision, pp. 1440–1448, 2015.
[8] Li, Weixin and Mahadevan, Vijay and Vasconcelos, Nuno, “Anomaly
detection and localization in crowded scenes” IEEE transactions on
pattern analysis and machine intelligence, IEEE, vol.1, pp. 18–32, 2013.
[9] Du, Dawei and Qi, Yuankai and Yu, Hongyang and Yang, Yifan and
Duan, Kaiwen and Li, Guorong and Zhang, Weigang and Huang,
Qingming and Tian, Qi, “The unmanned aerial vehicle benchmark:
Object detection and tracking”, Proceedings of the European conference
on computer vision (ECCV), pp. 370–386, 2018.
[10] Everingham, Mark and Eslami, SM and Van Gool, Luc and Williams,
Christopher KI and Winn, John and Zisserman, Andrew, “The pascal
visual object classes challenge: A retrospective”, International journal
of computer vision, Springer, vol.111, pp. 98–136, 2015.
[11] Cavaliere, Danilo and Loia, Vincenzo and Saggese, Alessia and Sen-
atore, Sabrina and Vento, Mario,“A human-like description of scene
events for a proper UAV-based video content analysis”, Knowledge-
Based Systems, vol. 178, pp. 163–175, 2019.
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

## Page 12

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
12
[12] Yang, Di and Ozbay, Kaan and Xie, Kun and Yang, Hong and Zuo,
Fan and Sha, Di,“Proactive safety monitoring: A functional approach
to detect safety-related anomalies using unmanned aerial vehicle video
data”, Transportation research part C: emerging technologies, vol. 127,
pp. 103130, 2021.
[13] Bozcan, Ilker and Kayacan, Erdal,“Context-dependent anomaly detec-
tion for low altitude traffic surveillance”, 2021 IEEE International
Conference on Robotics and Automation (ICRA), pp. 224–230, 2021.
[14] Jin, Pu and Mou, Lichao and Xia, Gui-Song and Zhu, Xiao Xi-
ang,“Anomaly Detection in Aerial Videos with Transformers”, IEEE
Transactions on Geoscience and Remote Sensing, 2022.
[15] Robicquet, Alexandre and Sadeghian, Amir and Alahi, Alexandre and
Savarese, Silvio, “Learning social etiquette: Human trajectory under-
standing in crowded scenes”, European conference on computer vision,
pp. 549–565, 2016.
[16] Kalra, Isha and Singh, Maneet and Nagpal, Shruti and Singh, Richa and
Vatsa, Mayank and Sujit, PB, “Dronesurf: Benchmark dataset for drone-
based face recognition”, 2019 14th IEEE International Conference on
Automatic Face and Gesture Recognition (FG 2019), pp. 1–7, 2019.
[17] Bonetto, Margherita and Korshunov, Pavel and Ramponi, Giovanni and
Ebrahimi, Touradj, “Privacy in mini-drone based video surveillance”,
2015 11th IEEE international conference and workshops on automatic
face and gesture recognition (FG), vol. 4, pp. 1–6, 2015.
[18] Hamdi, Slim,“Deep Learning Anomaly Detection for Drone-based
Surveillance”, Troyes, 2021.
[19] Hamdi, Slim and Bouindour, Samir and Snoussi, Hichem and Wang,
Tian and Abid, Mohamed,“End-to-end deep one-class learning for
anomaly detection in uav video stream”, Journal of Imaging, vol. 7,
pp. 90, 2021.
[20] Bozcan, Ilker and Kayacan, Erdal,“Au-air: A multi-modal unmanned
aerial vehicle dataset for low altitude traffic surveillance”, 2020 IEEE
International Conference on Robotics and Automation (ICRA), pp.
8504–8510, 2020.
[21] Chen, Qiang and Wang, Yingming and Yang, Tong and Zhang, Xiangyu
and Cheng, Jian and Sun, Jian, “You only look one-level feature”,
Proceedings of the IEEE/CVF conference on computer vision and
pattern recognition, pp. 13039–13048, 2021.
[22] Wang, Chien-Yao and Yeh, I-Hau and Liao, Hong-Yuan Mark,“You only
learn one representation: Unified network for multiple tasks”, arXiv
preprint arXiv:2105.04206, 2021.
[23] Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun,
Jian,“Yolox: Exceeding yolo series in 2021”, Workshop on Autonomous
Driving at CVPR 2021, 2021.
[24] Redmon, Joseph and Farhadi, Ali,“Yolov3: An incremental improve-
ment”, arXiv preprint arXiv:1804.02767, 2018.
[25] Wang, Chien-Yao and Bochkovskiy, Alexey and Liao, Hong-Yuan
Mark,“YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for
real-time object detectors”, arXiv preprint arXiv:2207.02696, 2022.
[26] Yao, Jia and Qi, Jiaming and Zhang, Jie and Shao, Hongmin and Yang,
Jia and Li, Xin,“A real-time detection algorithm for Kiwifruit defects
based on YOLOv5”, Electronics, MDPI, vol.10, pp.1711, 2021.
[27] He, Kaiming and Gkioxari, Georgia and Doll´ar, Piotr and Girshick,
Ross,“Mask r-cnn”, Proceedings of the IEEE international conference
on computer vision, pp.2961–2969, 2017.
[28] Yu, Weiping and Yang, Taojiannan and Chen, Chen,“Towards resolving
the challenge of long-tail distribution in UAV images for object detec-
tion”, Proceedings of the IEEE/CVF winter conference on applications
of computer vision, pp.3258–3267, 2021.
[29] Du, Dawei and Zhu, Pengfei and Wen, Longyin and Bian, Xiao and Lin,
Haibin and Hu, Qinghua and Peng, Tao and Zheng, Jiayu and Wang,
Xinyao and Zhang, Yue and others,“VisDrone-DET2019: The vision
meets drone object detection in image challenge results”, Proceedings of
the IEEE/CVF international conference on computer vision workshops,
pp.0-0, 2019.
[30] Zhu, Xingkui and Lyu, Shuchang and Wang, Xu and Zhao, Qi,
“Improved YOLOv5 based on transformer prediction head for object
detection on drone-captured scenarios”, Proceedings of the IEEE/CVF
international conference on computer vision, pp. 2778–2788, 2021.
[31] Riz, Luigi and Caraffa, Andrea and Bortolon, Matteo and Mekhalfi,
Mohamed Lamine and Boscani, Davide and Moura, Andr´e and Antunes,
Jos´e and Dias, Andr´e and Silva, Hugo and Leonidou, Andreas and oth-
ers,“The MONET dataset: Multimodal drone thermal dataset recorded
in rural scenarios”, arXiv preprint arXiv:2304.05417, 2023.
[32] Nguyen, Khang and Huynh, Nhut T and Nguyen, Phat C and Nguyen,
Khanh-Duy and Vo, Nguyen D and Nguyen, Tam V,“Detecting objects
from space: An evaluation of deep-learning modern approaches”, Elec-
tronics, MDPI, vol.9, pp.583, 2020.
[33] Dai, Jifeng and Li, Yi and He, Kaiming and Sun, Jian,“R-fcn: Object
detection via region-based fully convolutional networks”, Advances in
neural information processing systems, vol.29, 2016.
[34] Singh, Bharat and Najibi, Mahyar and Davis, Larry S,“Sniper: Efficient
multi-scale training”, Advances in neural information processing sys-
tems, vol.31, 2018.
[35] Liu, Wei and Anguelov, Dragomir and Erhan, Dumitru and Szegedy,
Christian and Reed, Scott and Fu, Cheng-Yang and Berg, Alexander
C,“Ssd: Single shot multibox detector”, Computer Vision–ECCV 2016:
14th European Conference, Amsterdam, The Netherlands, October 11–
14, 2016, Proceedings, Part I 14, Springer, pp. 21–37, 2016.
[36] Lin, Tsung-Yi and Goyal, Priya and Girshick, Ross and He, Kaiming
and Doll´ar, Piotr,“Focal loss for dense object detection”, Proceedings of
the IEEE international conference on computer vision, pp. 2980–2988,
2017.
[37] Zhou, Xingyi and Wang, Dequan and Kr¨ahenb¨uhl, Philipp,“Objects as
points”, arXiv preprint arXiv:1904.07850, 2019.
[38] Nguyen, Khanh-Duy and Nguyen, Khang and Le, Duy-Dinh and Duong,
Duc Anh and Nguyen, Tam V,“You always look again: Learning to
detect the unseen objects”, Journal of Visual Communication and Image
Representation, Elsevier, vol.60, pp. 206–216, 2019.
[39] Nguyen, Khanh-Duy and Nguyen, Khang and Le, Duy-Dinh and Duong,
Duc Anh and Nguyen, Tam V,“YADA: you always dream again for better
object detection”, Multimedia Tools and Applications, Elsevier, vol.78,
pp. 28189–28208, 2019.
This article has been accepted for publication in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. This is the author's version which has not been fully e
content may change prior to final publication. Citation information: DOI 10.1109/JSTARS.2023.3285905
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/
