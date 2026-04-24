# AU AIR A Multi-Modal Unmanned Aerial Vehicle Dataset for Low Altitude Traffic Surveillance.pdf

## Page 1

AU-AIR: A Multi-modal Unmanned Aerial Vehicle Dataset for Low
Altitude Trafﬁc Surveillance
Ilker Bozcan, Erdal Kayacan
Abstract— Unmanned aerial vehicles (UAVs) with mounted
cameras have the advantage of capturing aerial (bird-view)
images. The availability of aerial visual data and the recent
advances in object detection algorithms led the computer vision
community to focus on object detection tasks on aerial images.
As a result of this, several aerial datasets have been introduced,
including visual data with object annotations. UAVs are used
solely as ﬂying-cameras in these datasets, discarding different
data types regarding the ﬂight (e.g., time, location, internal
sensors). In this work, we propose a multi-purpose aerial
dataset (AU-AIR) that has multi-modal sensor data (i.e., visual,
time, location, altitude, IMU, velocity) collected in real-world
outdoor environments. The AU-AIR dataset includes meta-data
for extracted frames (i.e., bounding box annotations for trafﬁc-
related object category) from recorded RGB videos. Moreover,
we emphasize the differences between natural and aerial images
in the context of object detection task. For this end, we
train and test mobile object detectors (including YOLOv3-
Tiny and MobileNetv2-SSDLite) on the AU-AIR dataset, which
are applicable for real-time object detection using on-board
computers with UAVs. Since our dataset has diversity in
recorded data types, it contributes to ﬁlling the gap between
computer vision and robotics. The dataset is available at
https://bozcani.github.io/auairdataset.
I. INTRODUCTION
Unmanned aerial vehicles (UAVs) are extensively used as
ﬂying platforms of sensors for different domains such as
trafﬁc surveillance [1], managing the urban environment [2],
package delivery [3] or aerial cinematography [4]. For these
applications, UAVs are equipped with mounted cameras and
mainly gather visual data of the environment. Then, computer
vision algorithms are applied to aerial visual data to extract
high-level information regarding the environment.
Object detection is one of the most studied problems
in computer vision. The recent advances in deep learning
(variants of convolutional neural networks (CNNs) mainly)
have led to breakthrough object detection performances with
the availability of large datasets and computing power. Since
these methods require a large number of training samples,
several datasets (e.g., COCO [5], Pascal VOC [6]) have been
introduced for benchmarking for the object detection task.
The samples in these datasets consist of natural images that
are mainly captured by handheld cameras. The signiﬁcant
differences between natural and aerial images (such as object
layouts and sizes) cause these object detectors to have trouble
to ﬁnd objects in aerial images. Therefore, several datasets
(e.g., [7]–[13]) have been introduced in recent years as a
benchmark for object detection in aerial images.
I. Bozcan and E. Kayacan are with the Department of Engineering,
Aarhus University, 8000 Aarhus C, Denmark {ilker, erdal} at
eng.au.dk
 
 
Time:                   15:30:12+40 ms
Date:        03.08.2019 
Location:             56.206821°, 10.188645°
Altitude:  22 meters 
     
Roll, pitch, yaw: 0.011 rad, 0 rad, 1.26 rad
        
Vx, Vy, Vz:            0.05 m/s, 0.03 m/s, -0.23 m/s 
Fig. 1.
In the AU-AIR dataset, extracted frames are labeled with object
annotations, time stamp, current location, altitude, and velocity of the UAV,
and the rotation data read from the IMU sensor. [Best viewed in color]
Besides visual data gathered by a camera, the data from
other sensors might give crucial information about the envi-
ronment. The use of UAVs as only ﬂying cameras cut off the
potential advance in multi-modal object detection algorithms
for aerial applications. For instance, the recent advances
in perception for autonomous driving have brought new
datasets such as [14]–[16] including multi-modal data (e.g.,
RGB images, Global Positioning System (GPS) coordinates,
inertial measurement unit (IMU) data). Although the data
fusion for object detection is still open research topic [17],
these multi-modal datasets allow a benchmark for further
research. However, to the best of our knowledge, there is no
such multi-modal dataset collected in a real-world outdoor
environment for UAVs.
In this work, we present a multi-modal UAV dataset (The
AU-AIR dataset) in order to push forward the development
of computer vision and robotic algorithms targeted at au-
tonomous aerial surveillance. The AU-AIR dataset meets
vision and robotics for UAVs having the multi-modal data
from different on-board sensors. The dataset consists of 8
video streams (over 2 hours in total) for trafﬁc surveillance.
The videos mainly are recorded at Skejby Nordlandsvej
and P.O Pedersensvej roads (Aarhus, Denmark). The dataset
includes aerial videos, time, GPS coordinates and the altitude
of the UAV, IMU data, and the velocity. The videos are
recorded at different ﬂight altitudes from 5 meters to 30
meters and in different camera angles from 45 degrees to 90
arXiv:2001.11737v2  [cs.CV]  3 Feb 2020

## Page 2

degrees (i.e., complete bird-view images that the camera is
perpendicular to the Earth). Instances belonging to different
object categories related to the trafﬁc surveillance context are
annotated with bounding boxes in video frames. Moreover,
each extracted video frame is labeled with the ﬂight data
(See Fig. 1).
The whole dataset includes 32,823 labeled video frames
with object annotations and the corresponding ﬂight data.
Eight object categories are annotated including person, car,
van, truck, motorbike, bike, bus, trailer. The total number
of annotated instances is 132,034. The dataset is split into
30,000 training-validation samples and 2,823 test samples.
In this work, we emphasize differences between aerial and
natural images in the context of object detection tasks. To
this end, we compare image samples and object instances
between the AU-AIR dataset and the COCO dataset [5]. In
our experiments, we train and evaluate two mobile object
detectors (including YOLOv3-tiny [18] and MobileNetv2-
SSD Lite [19] on the AU-AIR dataset. We form a baseline,
including mobile object detectors since we focus on real-
time performance and the applicability of object detection
task onboard computers mounted on UAV.
A. Related Work
In recent years, several drone datasets have been intro-
duced for object detection tasks ([7]–[13]). Zhu et al. [7]
propose a UAV dataset (VisDrone) consisting of visual data
and object annotations in images and frames. In the VisDrone
dataset, object instances belonging the certain categories are
annotated by bounding boxes and category labels. Besides
object annotations, VisDrone includes some vision-related
attributes such as the visibility of a scene, occlusion status.
Du et al. [8] propose a benchmark dataset for object detection
and tracking in aerial images. The dataset also includes meta
information regarding the ﬂight altitude. Hsieh et al. [9]
propose a UAV-based counting dataset (CARPK) including
object instances that belong to the car category. Robicquet
et al. [10] introduce a UAV dataset (Stanford) that collects
images and videos of six types of objects in the Stanford
campus area. In this dataset, some of the object categories
dominate the dataset having a high number of samples,
whereas the remaining object categories have signiﬁcantly
less number of instances. Mueller et al. [11] propose syn-
thetic dataset created by a simulator for target tracking with
a UAV. Collins et al. [12] introduce a benchmarking website
(VIVID) with an evaluation dataset collected under the
DARPA VIVID program. Krajewski et al. propose an aerial
dataset collected from highways, including object bounding
boxes and labels of vehicles.
These datasets are annotated by common objects in an
environment such as humans and different types of vehicles
(e.g., car, bike, van). However, they only include visual data
and bounding box annotations for objects and discard other
sensory data. Among these studies, only UAVDT [8] includes
an attribute that gives limited information about the ﬂight
altitude (i.e., labels such as ”low-level”, ”mid-level” and
”high-level”).
Fonder et al. [20] propose a synthetic dataset (Mid-Air) for
low altitude drone ﬂights in unstructured environments (e.g.,
forest, country). It includes multi-modal data regarding the
ﬂight (e.g., visual, GPS, IMU data) without any annotations
for visual data.
There are also multi-modal drone datasets in the literature
([20]–[24]). However, the visual data are not collected for
object detection since the main focus of these studies is the
UAV navigation. Therefore, these datasets do not have object
annotations. The comparison of existing datasets is given in
Table I.
B. Contribution
Looking also at the summary of the existing studies in
Table I, the followings are the main contributions of this
work:
• To the best of our knowledge, the AU-AIR dataset is
the ﬁrst multi-modal UAV dataset for object detection.
The dataset includes ﬂight data (i.e., time, GPS, alti-
tude, IMU data) in addition to visual data and objects
annotations.
• Considering the real-time applicability, we form a base-
line training and testing mobile object detectors with the
AU-AIR dataset. We emphasize the differences between
object detection in aerial images and natural images.
II. OBJECT DETECTION IN NATURAL IMAGES VS
AERIAL IMAGES
The availability of large amounts of data and processing
power enables deep neural networks to achieve state-of-the-
art results for object detection. Currently, deep learning-
based object detectors are separated into two groups. The
ﬁrst group consists of region-based CNNs that ascend on
image classiﬁers. Region-based CNNs propose image regions
that are likely to contain an object and classify the region
into a predeﬁned object category. The second group has only
one stage converting to the object detection problem into the
bounding box prediction for objects, without re-purposing
image classiﬁers. Faster-R-CNN [25] is one of the well-
known models belonging to the ﬁrst group, YOLO [26] and
SSD [27] are the popular object detectors that belong to the
second group.
Deep learning-based object detectors have trained and
performed on large datasets such as COCO [5] and PASCAL
[6]. These datasets include natural images that contain a
single object or multi objects in their natural environments.
Most of the images in these datasets are captured by humans
using a handheld camera so that the vast majority of images
have side-view. There are challenges of the object detection
in natural images such as occlusion, illumination changes,
rotation, low resolution, crowd existence of instances.
Aerial images have different characteristics from natural
images due to having a bird’s-eye view. First of all, objects
in natural images are much larger than their counterparts
in aerial images. For example, an object category such as
humans may occupy a large number of pixels in natural
images. However, it may have a few numbers of pixels

## Page 3

TABLE I
COMPARISON WITH EXISTING UAV DATASETS.
Dataset
Environment
Data type
Visual data
Object annotations
Time
GPS
Altitude
Velocity
IMU data
VisDrone [7]
outdoor
real
yes
yes
no
no
no
no
no
UAVDT [8]
outdoor
real
yes
yes
no
no
partial
no
no
CARPK [9]
outdoor
real
yes
yes
no
no
no
no
no
Stanford [10]
outdoor
real
yes
yes
no
no
no
no
no
UAV123 [11]
outdoor
synthetic
yes
yes
no
no
no
no
no
VIVID [12]
outdoor
real
yes
yes
no
no
no
no
no
highD [13]
outdoor
real
yes
yes
no
no
no
no
no
Mid-Air [20]
outdoor
synthetic
yes
no
yes
yes
yes
yes
yes
Blackbird [21]
indoor
real
yes
no
yes
yes
yes
yes
yes
EuRoC MAV [22]
indoor
real
yes
no
yes
yes
yes
yes
yes
Zurich Urban MAV [23]
outdoor
real
yes
no
yes
yes
yes
yes
yes
UPenn Fast Flight [24]
outdoor
real
yes
no
yes
yes
yes
yes
yes
AU-AIR
outdoor
real
yes
yes
yes
yes
yes
yes
yes
 
 
(a)
(b)
Fig. 2.
Sample images, including human category from COCO (a) and
AU-AIR (b) datasets. Human instances occupy a signiﬁcantly larger area in
the natural image (a) than in the aerial image (b). Figure (b) is captured at
an altitude of 12 meters that is close to the lowest value of ﬂight altitude
range (5 meters). Objects tend to occupy a much smaller area when the
altitude increases. [Best viewed in color]
 
 
person
person
person
person
(a)
(b)
Fig. 3.
Sample images, including car category from COCO (a) and AU-
AIR (b) datasets. Car instances are occluded by other cars in a natural image
(a) that is captured by the handheld camera, but they are less likely to occur
due to other instances in an aerial image (b). [Best viewed in color]
in an aerial image that is quite challenging to detect for
object detectors (See Fig. 2). Moreover, aerial images can
be fed to a network with higher dimensions that increases
computational cost in order to prevent the diminishing of
pixels belonging to small objects.
Secondly, an occlusion is observed in different conditions
for natural and aerial images. In natural images, an object
instance may be occluded by another foreground object
instance (e.g., a human in front of a car). However, objects
in aerial images are less likely to be occluded by other
foreground objects (especially, bird-view images captured by
a camera that is perpendicular to the Earth). (See Fig. 3.
Thirdly, the perspective in aerial images makes appear-
ances of objects short and squat. This fact diminishes the
 
 
(a)
(b)
Fig. 4.
Sample images from the AU-AIR dataset. The object height
information is lost in images captured with a complete bird-view angle
(a), whereas it can be inferred in images with a side-view angle (b). The
heights of the bounding box in (b) give a clue about objects’ height (green
arrows). [Best viewed in color]
information regarding an object height (See Fig. 4). More-
over, although aerial images can supply more contextual
information about an environment by a broader view angle,
the object instances may be amid cluttered.
Lastly, having a drone to capture aerial images, the altitude
changes during the ﬂight can cause varieties in object size
and appearance in aerial images. Therefore, a recording of
aerial videos at different altitudes may change the levels of
challenges mentioned above.
III. AU-AIR – THE MULTI-MODAL UAV DATASET
To address the challenges mentioned in Section II, we
propose a multi-modal drone dataset (AU-AIR) including
videos, object annotations in the extracted frames and sensor
data for the corresponding frames. The data are captured by
low-level ﬂight (max. 30 meters) and for the scenario of a
trafﬁc surveillance. The AU-AIR dataset consists of video
clips, sensor data, and object bounding box annotations for
video frames.
A. UAV Platform
We have used a quadrotor (Parrot Bebop 2) to capture the
videos and record the ﬂight data. An on-board camera has
recorded the videos with a resolution of 1920 × 1080 pixels
at 30 frames per second (fps). The sensor data have been
recorded for every 20 milliseconds.

## Page 4

B. Dataset Collection
The AU-AIR dataset consists of 8 video clips (approxi-
mately in 2 hours of a total length) with 32,823 extracted
frames. All videos are recorded for a scenario of aerial
trafﬁc surveillance at the intersection of Skejby Nordlandsvej
and P.O Pedersensvej (Aarhus, Denmark) on windless days.
Moreover, the videos cover various lighting conditions due to
the time of the day and the weather conditions (e.g., sunny,
partly sunny, cloudy).
Capturing an aerial video with a UAV brings different
challenges for visual surveillance that are signiﬁcantly dif-
ferent from natural images. To add these challenges in our
dataset, we have captured the videos in different ﬂight alti-
tudes and camera angles. The ﬂight altitude changes between
10 meters to 30 meters in the videos and the camera angle
is adjusted from 45 degrees to 90 degrees (perpendicular to
the Earth). An increase in the camera angle makes object
detection task more challenging since images get differ from
natural images.
Although the videos have been recorded with 30 fps,
we have extracted ﬁve frames for every second in order to
prevent the redundant occurrence of frames. Both of raw
videos and extracted frames have a resolution of 1920×1080
pixels.
C. Visual Data and Annotation
Considering a trafﬁc surveillance scenario, we have man-
ually annotated speciﬁc object categories in the frames. For
annotation, we used a bounding box and object category
index for each instance. The annotated object categories
include eight types of objects which highly occur during
the trafﬁc surveillance: person, car, bus, van, truck, bike,
motorbike, and trailer.
For annotation, we employed workers on Amazons Me-
chanical Turk (AMT) [28]. In order to increase the labeling
quality, three workers annotated the same frame separately.
Then, we combined annotations if they have the same object
labels, and whose bounding boxes overlap more than a
certain threshold. We chose a threshold as a value of 0.75
experimentally. In case this condition is not satisﬁed, we
manually ﬁne-tuned the bounding boxes and class labels. The
category distribution over the dataset can be seen in Fig. 5. In
the context of trafﬁc surveillance, cars appear signiﬁcantly
more than other classes, and three vehicle types (car, van,
truck) have a major portion of annotated bounding boxes.
The AU-AIR dataset includes frames that are captured in
different ﬂight altitudes (See Fig. 6). We recorded the data
mainly for 10 meters, 20 meters, and 30 meters with different
camera angles from 45 degrees to 90 degrees.
D. Sensor Data
In addition to visual data and object annotations, the AU-
AIR dataset includes sensor data that are logged during
the video recording. In the dataset, we have the following
attributes for each extracted frame:
• d: current date of a frame
• t: current time stamp of the frame
car
van
truck
human
trailer
bicycle
bus
motorbike
object classes
0
50000
100000
num. of annotations
102622
9995
9545
5158
2538
1128
729
319
Fig. 5.
Distribution of annotations across object classes.
5
10
15
20
25
30
altitude (meters)
0
5000
10000
num. of samples
589
7023
2110
11657
2094
9352
Fig. 6.
Distribution of samples across ﬂight altitudes.
• la: latitude of the UAV (read from GPS sensor)
• lo: longitude of the UAV (read from GPS sensor)
• a: altitude of the UAV (read from altimeter)
• φ: UAV roll angle (rotation around the x axis) (read
from IMU sensor)
• θ: UAV pitch angle (rotation around the y axis) (read
from IMU sensor)
• ψ: UAV yaw angle (rotation around the z axis) (read
from IMU sensor)
• Vx: speed on the x axis
• Vy: speed on the y axis
• Vz: speed on the z axis
Table II shows unit values and ranges for each attribute
except the date. The date (d) has a format of MMDDYYYY-
HHMMSS where MM, DD, YYYY, HH, MM, SS indicates
the month, day, year, hour, minutes, and second, respectively.
TABLE II
SENSOR DATA TYPES IN THE DATASET.
Data
Unit
Min. value
Max. value
t
milliseconds
0
inf
la
degrees
−90
+90
lo
degrees
−180
+180
a
millimeters
0
inf
φ
radians
−π
+π
θ
radians
−π
+π
ψ
radians
−π
+π
Vx
m/s
0
inf
Vy
m/s
0
inf
Vz
m/s
0
inf
The velocities (Vx, Vy, Vz) and rotation angles (φ, θ, ψ) are
calculated according to the UAV body-frame given in Fig. 7.

## Page 5

X-axis
Y-axis
Z-axis
Vx
Vy
Vz
θ
Ψ
Φ
camera
(front side)
Fig. 7.
The body-frame of Parrot Bebop 2. [Best viewed in color]
IV. EVALUATION AND ANALYSIS
We train and evaluate mobile object detectors with our
dataset. During the evaluation, we consider real-time perfor-
mance rather than achieving a state-of-the-art accuracy for
the sake of the applicability. Therefore, we choose two mo-
bile object detectors (YOLOv3-Tiny [18] and MobileNetv2-
SSDLite [19]), which have a reasonable trade-off between
the detection accuracy and the inference time.
A. Baseline networks
We conﬁgure YOLOv3-Tiny [18] and MobileNetv2-
SSDLite [19] for the bench-marking using the default pa-
rameters (e.g., learning rate, input size) as suggested in the
original papers. We use the models that are trained on the
COCO dataset as backbones.
We split the AU-AIR dataset into %60 training, %10
validation and %30 testing samples. The object detectors are
adapted to the total number of classes in the AU-AIR dataset
(8 classes in total) by changing their last layers.
B. Comparison Metrics
To compare detection performances, we use mean average
precision (mAP) that is a prominent metric in object detec-
tion [5], [6]. It is the mean of the average precision (AP)
values which compute the precision score for an object cate-
gory at discretized recall values over 0 to 1 [6]. We consider
11 different recall values as in [6] and the intersection over
union (IoU) threshold as 0.5.
C. Results
For
benchmarking,
we
train
YOLOv3-Tiny
and
MobileNetv2-SSDLite
with
the
AU-AIR
Dataset.
We
use the batch size of 32 and Adam optimizer with the
default parameters (alpha= 0.001, beta1=0.9, beta2=0.999).
The training is stopped when the validation error starts
to increase. Both networks are pre-trained on the COCO
dataset. In order to see the effect of the training with an
aerial dataset and a natural image dataset, we also use
YOLOv3-Tiny and MobileNetv2-SSDLite trained on the
COCO dataset without further training with the AU-AIR
dataset. The results are given in Table III.
 
 
(a)
(b)
(c)
(d)
Fig. 8.
Sample results of YOLOv3-Tiny networks. The network trained on
only the COCO dataset has poor detection performance (a). The network
trained on the AU-AIR dataset with the COCO pre-training has better
results for the same input (b). It can also detect objects in complete bird-
view images, which appears signiﬁcantly different from natural images. The
network trained on AU-AIR dataset can also ﬁnd objects which suffer from
the perspective (d). [Best viewed in color]
As shown in Table III, the networks only trained on the
COCO dataset have poor results. This is expected since the
characteristics of natural images are signiﬁcantly different
from natural images.
We observe that the AP values of motorbike and bicycle
categories are signiﬁcantly lower than the AP values of other
categories. This fact might happen due to the class imbalance
problem and the small object sizes of these categories.
However, the bus category has the highest AP value, although
there are fewer bus instances. This might result from the large
size of bus instances in the frames. Furthermore, although the
size of human instances is usually as small as the sizes of
motorbike and bicycles, the AP values of the human category
are relatively higher than these classes. This fact might be a
consequence of the high number of human instances. There
is no available AP values for the van and trailer categories
in Table III since they do not exist in the COCO dataset.
The baselines trained on the AU-AIR dataset are good at
ﬁnding objects in aerial images that are captured at different
altitudes and view angles. Qualitative results can be seen in
Fig. 8.
Among the baselines, YOLOv3-Tiny has higher AP values
and mAP value compared to MobileNetv2-SSDLite. There is
no signiﬁcant difference between inference times (17.5 FPS
and 17 FPS for YOLOv3-Tiny and MobileNetv2-SSDLite on
TX2, respectively).
V. DISCUSSION
Since the number of instances of each object category
is imbalanced in the AU-AIR dataset (Fig. 5), we consider
several methods to solve the imbalanced class problem in
the next version of the dataset. As a ﬁrst step, we will try

## Page 6

TABLE III
CATEGORY-WISE AVERAGE PRECISION VALUES OF THE BASELINE NETWORKS.
Training
Model
Dataset
Human
Car
Truck
Van
Motorbike
Bicycle
Bus
Trailer
mAP
YOLOV3-Tiny
AU-AIR
34.05
36.30
47.13
41.47
4.80
12.34
51.78
13.95
30.22
MobileNetV2-SSDLite
AU-AIR
22.86
19.65
34.74
25.73
0.01
0.01
39.63
13.38
19.50
YOLOV3-Tiny
COCO
0.01
0
0
n/a
0
0
0
n/a
n/a
MobileNetV2-SSDLite
COCO
0
0
0
n/a
0
0
0
n/a
n/a
to collect more data to balance the number of instances. Be-
sides, we may consider adding synthetic data (i.e., changing
the brightness of images, translation, rotation) to increase
the number of object categories which has a low number of
samples in the current version.
We use AMT to annotate objects in images. Although
three different people annotate one image and the annotations
are manually checked by ourselves, there might be still
overlooked samples that have weak annotations (e.g., unla-
belled instances, loose bounding box drawings). Therefore,
we consider using a three-step workﬂow proposed by Su et
al. [29]. In this workﬂow, the ﬁrst worker draws a bounding
box around an instance, the second worker veriﬁes whether
the bounding box is correctly drawn, and the third worker
checks whether all object instances are annotated.
Unlike other UAV object detection datasets, ours includes
sensor data corresponding to each frame. In this work, we
give a baseline only for object annotations and visual data.
As future work, more baselines may be added to encourage
research using sensor data (e.g., navigation and control of a
UAV, object detection using multi-modal data). Also, we can
add more visual sensors, such as multi-spectral cameras.
We have used a ready-to-ﬂy quadrotor (i.e., Parrot Bebop
2) to collect the whole dataset. We also consider collecting
more samples from other platforms (e.g., different types of
UAVs) using cameras that have different resolutions and
frame rates.
In this dataset, trafﬁc surveillance is the primary context.
In future work, we consider increasing the number of envi-
ronment contexts to increase diversity in the dataset.
VI. CONCLUSIONS
In this work, we propose the AU-AIR dataset that is a
multi-modal UAV dataset collected in an outdoor environ-
ment. Our aim is to ﬁll the gap between computer vision
and robotics having a diverse range of recorded data types for
UAVs. Including visual data, object annotations, and ﬂight
data, it can be used for different research ﬁelds focused on
data fusion.
We have emphasized the differences between natural im-
ages and aerial images affecting the object detection task.
Moreover, since we consider real-time performance and
applicability in real-world scenarios, we have created a base-
line, including two mobile object detectors in the literature
(i.e., YOLOv3-Tiny [18] and MobileNetv2-SSDLite [19]).
In our experiments, we showed that mobile networks trained
on natural images have trouble in detecting objects in aerial
images.
REFERENCES
[1] A. Puri, “A survey of unmanned aerial vehicles (uav) for trafﬁc surveil-
lance,” Department of computer science and engineering, University
of South Florida, pp. 1–29, 2005.
[2] D. Gallacher, “Drones to manage the urban environment: Risks,
rewards, alternatives,” Journal of Unmanned Vehicle Systems, vol. 4,
no. 2, pp. 115–124, 2016.
[3] M. Mehndiratta and E. Kayacan, “A constrained instantaneous learning
approach for aerial package delivery robots: onboard implementation
and experimental results,” Autonomous Robots, vol. 43, no. 8, pp.
2209–2228, 2019.
[4] R. Bonatti, W. Wang, C. Ho, A. Ahuja, M. Gschwindt, E. Camci,
E. Kayacan, S. Choudhury, and S. Scherer, “Autonomous aerial
cinematography in unstructured environments with learned artistic
decision-making,” Journal of Field Robotics, vol. n/a, no. n/a. [Online].
Available: https://onlinelibrary.wiley.com/doi/abs/10.1002/rob.21931
[5] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan,
P. Doll´ar, and C. L. Zitnick, “Microsoft coco: Common objects in
context,” in European conference on computer vision. Springer, 2014,
pp. 740–755.
[6] M. Everingham, L. Van Gool, C. K. Williams, J. Winn, and A. Zisser-
man, “The pascal visual object classes (voc) challenge,” International
journal of computer vision, vol. 88, no. 2, pp. 303–338, 2010.
[7] P. Zhu, L. Wen, X. Bian, L. Haibin, and Q. Hu, “Vision meets drones:
A challenge,” arXiv preprint arXiv:1804.07437, 2018.
[8] D. Du, Y. Qi, H. Yu, Y. Yang, K. Duan, G. Li, W. Zhang, Q. Huang,
and Q. Tian, “The unmanned aerial vehicle benchmark: Object de-
tection and tracking,” in Proceedings of the European Conference on
Computer Vision (ECCV), 2018, pp. 370–386.
[9] M.-R. Hsieh, Y.-L. Lin, and W. H. Hsu, “Drone-based object counting
by spatially regularized regional proposal network,” in Proceedings
of the IEEE International Conference on Computer Vision, 2017, pp.
4145–4153.
[10] A. Robicquet, A. Sadeghian, A. Alahi, and S. Savarese, “Learning
social etiquette: Human trajectory understanding in crowded scenes,”
in European conference on computer vision.
Springer, 2016, pp.
549–565.
[11] M. Mueller, N. Smith, and B. Ghanem, “A benchmark and simula-
tor for uav tracking,” in European conference on computer vision.
Springer, 2016, pp. 445–461.
[12] R. Collins, X. Zhou, and S. K. Teh, “An open source tracking
testbed and evaluation web site,” in IEEE International Workshop on
Performance Evaluation of Tracking and Surveillance, vol. 2, no. 6,
2005, p. 35.
[13] R. Krajewski, J. Bock, L. Kloeker, and L. Eckstein, “The highd dataset:
A drone dataset of naturalistic vehicle trajectories on german highways
for validation of highly automated driving systems,” in 2018 IEEE
21st International Conference on Intelligent Transportation Systems
(ITSC), 2018.
[14] A. Geiger, P. Lenz, C. Stiller, and R. Urtasun, “Vision meets robotics:
The kitti dataset,” The International Journal of Robotics Research,
vol. 32, no. 11, pp. 1231–1237, 2013.
[15] H. Caesar, V. Bankiti, A. H. Lang, S. Vora, V. E. Liong, Q. Xu, A. Kr-
ishnan, Y. Pan, G. Baldan, and O. Beijbom, “nuscenes: A multimodal
dataset for autonomous driving,” arXiv preprint arXiv:1903.11027,
2019.
[16] Y. Choi, N. Kim, S. Hwang, K. Park, J. S. Yoon, K. An, and I. S.
Kweon, “Kaist multi-spectral day/night data set for autonomous and
assisted driving,” IEEE Transactions on Intelligent Transportation
Systems, vol. 19, no. 3, pp. 934–948, 2018.

## Page 7

[17] D. Feng, C. Haase-Schuetz, L. Rosenbaum, H. Hertlein, F. Duffhauss,
C. Glaeser, W. Wiesbeck, and K. Dietmayer, “Deep multi-modal
object detection and semantic segmentation for autonomous driving:
Datasets, methods, and challenges,” arXiv preprint arXiv:1902.07830,
2019.
[18] J. Redmon and A. Farhadi, “Yolov3: An incremental improvement,”
arXiv preprint arXiv:1804.02767, 2018.
[19] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen, “Mo-
bilenetv2: Inverted residuals and linear bottlenecks,” in Proceedings
of the IEEE Conference on Computer Vision and Pattern Recognition,
2018, pp. 4510–4520.
[20] M. Fonder and M. Van Droogenbroeck, “Mid-air: A multi-modal
dataset for extremely low altitude drone ﬂights,” in Proceedings of
the IEEE Conference on Computer Vision and Pattern Recognition
Workshops, 2019, pp. 0–0.
[21] A. Antonini, W. Guerra, V. Murali, T. Sayre-McCord, and S. Karaman,
“The blackbird dataset: A large-scale dataset for uav perception in
aggressive ﬂight,” arXiv preprint arXiv:1810.01987, 2018.
[22] M. Burri, J. Nikolic, P. Gohl, T. Schneider, J. Rehder, S. Omari, M. W.
Achtelik, and R. Siegwart, “The euroc micro aerial vehicle datasets,”
The International Journal of Robotics Research, vol. 35, no. 10, pp.
1157–1163, 2016.
[23] A. L. Majdik, C. Till, and D. Scaramuzza, “The zurich urban micro
aerial vehicle dataset,” The International Journal of Robotics Research,
vol. 36, no. 3, pp. 269–273, 2017.
[24] K. Sun, K. Mohta, B. Pfrommer, M. Watterson, S. Liu, Y. Mulgaonkar,
C. J. Taylor, and V. Kumar, “Robust stereo visual inertial odometry
for fast autonomous ﬂight,” IEEE Robotics and Automation Letters,
vol. 3, no. 2, pp. 965–972, 2018.
[25] S. Ren, K. He, R. Girshick, and J. Sun, “Faster r-cnn: Towards real-
time object detection with region proposal networks,” in Advances in
neural information processing systems, 2015, pp. 91–99.
[26] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, “You only look
once: Uniﬁed, real-time object detection,” in Proceedings of the IEEE
conference on computer vision and pattern recognition, 2016, pp. 779–
788.
[27] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed, C.-Y. Fu,
and A. C. Berg, “Ssd: Single shot multibox detector,” in European
conference on computer vision.
Springer, 2016, pp. 21–37.
[28] A. M. Turk, “Amazon mechanical turk,” Retrieved August, vol. 17, p.
2012, 2012.
[29] H. Su, J. Deng, and L. Fei-Fei, “Crowdsourcing annotations for visual
object detection,” in Workshops at the Twenty-Sixth AAAI Conference
on Artiﬁcial Intelligence, 2012.
