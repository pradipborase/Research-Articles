# Attitude_Estimation_of_Quadrotor_UAV_based_on_QUKF.pdf

## Page 1

VOLUME XX, 2017
1
Date of publication xxxx 00, 0000, date of current version xxxx 00, 0000.
Digital Object Identifier 10.1109/ACCESS.2022.Doi Number
Attitude Estimation of Quadrotor UAV based on
QUKF
TAO LIANG1, KAILAI YANG3, QIANG HAN1, CHENJIE LI1, JUNLIN LI1, QINGWEN DENG1,
SHIDONG CHEN1,2, XIANGUO TUO1,2.
1.School of Automation and Information Engineering, Sichuan University of Science and Engineering, Yibin 644000, China
2.Artificial Intelligence Key Laboratory of Sichuan Province, Yibin 644000, China
3.School of Mechanical Engineering, Sichuan University of Science and Engineering, Yibin 644000, China
Corresponding author: Qiang Han (e-mail: hanqiang1117@163.com).
This work was supported in part by the China University Innovation Fund "New Generation Information Technology Innovation Project" (2021ITA10002),
the Sichuan Province science and technology Department key research and development project(2021YFG0056), Sanjiang New District of Yibin City,
Sichuan
Province
unveiled
the
"AM-OLED
LCD
device
Assembly
Bonding
Technology
Research
and
Development"(2022JBGS001),
and in part by the Postgraduate Innovation Fund Project of Sichuan University of Science and Engineering under grant (Y2022110).
ABSTRACT Toward the quadcopter unmanned aerial vehicle (UAV) attitude measurement problem, to
improve the accuracy of acquisition of vehicle attitude parameters, and ensure accuracy of subsequent
attitude control, the Quaternion-based Unscented Kalman filter (QUKF) data fusion method is presented.
This attitude measurement system uses STM32F103 as the central controller, MPU6050 with integrated
accelerometer and gyroscope, and magnetometer HMC5883l as the measurement sensor. Coordinate
Rotation Relationships for the Attitude Heading Reference System (AHRS) in Quaternions, combining
Unscented Kalman Filter (UKF) to Fuse Low-Cost Attitude Measurement Systems, tracking estimation of
the genuine attitude of the vehicle. High-precision sensor measurements as real values, by comparing with
Extended Kalman Filter (EKF), Complementary Filter (CF), and genuine values to validate and analyze the
effectiveness of the algorithm applied to the low-cost attitude measurement system. Experimental results
show that the low-cost attitude measurement system using quaternions as state variables combined with
UKF can accurately estimate attitude information, providing precise attitude information for subsequent
attitude control of UAVs.
INDEX TERMS Unscented Kalman filter, quaternion, quadrotor UAV, attitude estimation, data fusion.
I. INTRODUCTION
For the past few years, UAVs have a bright future ahead
of them, widely used in both military and civilian
applications.
Quadcopter
UAVs
are
simple
and
inexpensive, and they can replace human labor for
particular tasks, so a large number of researchers and
companies have conducted extensive research in related
areas. In quadrotor attitude control, it is crucial to obtain
highly accurate and stable attitude information [1], it
determines the accuracy of the subsequent attitude control.
High-precision
attitude
sensors
can
acquire
vehicle
attitude information. However, high-precision attitude
sensors are generally characterized by high cost, bulky
and heavy. Currently, quadcopter drones on the market
generally consider the cost, load capacity, and other
reasons, choosing low-cost, low-precision sensors. And
this kind of sensor is susceptible to geomagnetic fields,
noise, vibration, and other environmental disturbances; in
this case, the accuracy of attitude information acquired by
low-precision sensors decreases; it affects the vehicle's
stability. Therefore, it is essential to have a stable and
highly
accurate
attitude
estimation
for
the
attitude
measurement system.
The low-cost MEMS inertial sensors currently available
on
the
market
generally
include
gyroscopes,
accelerometers, magnetometers. Gyroscopes in inertial
sensors are used for three-axis directional angular velocity
measurements, with better dynamic correspondence and
accuracy.
Still,
it
exists
integral
error,
long
time
cumulative error will be enlarged, the stability is relatively
poor,
and
the
angle
information
integrated
by
the
gyroscope is relative to the relative position of the starting
point,
so
it
does
not
provide
absolute
angle
[2].
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3320707
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

## Page 2

Author Name: Preparation of Papers for IEEE Access (February 2017)
2
VOLUME XX, 2017
Accelerometers for measuring acceleration in three axes,
with good static performance, but is susceptible to motion
acceleration
and
has
lower
dynamic
accuracy
[3].
Magnetometers are used to measure the strength of the
magnetic field in the triaxial direction, and external
magnetic interference is more sensitive to the magnetic
field, easily affected by magnetic fields[4]. Single inertial
sensors all have their drawbacks, so they can't be totally
trusted, need a fusion algorithm to fuse data from different
sensors and estimate valid attitude information.
Noise encountered in UAV attitude measurements is
generally filtered using a filtering method to remove the
interference caused by the noise [5]. Traditional filtering
methods can only be realized when the valid signal and
the noise have different frequency bands. In the early
1960s, Kalman [6] and Buse proposed a new linear
filtering and prediction theory. This method can process
the input and observed signals from noise in a linear state
space representation of the equations to find the state of
the system or the proper signal, and it was first applied to
the design of NASA's Apollo manned lunar landing
spacecraft and its navigation system [7]. The typical
attitude estimation algorithms are CF [8], Gradient-
Descent (GD) method [9], and Kalman filter (KF) [10].
[11] has compared these algorithms, CF and GD are
relatively simple and suitable for handling aircraft with
limited hardware performance; in the case of hardware
satisfaction, KF is the best choice. The KF fusion effect is
better than the above two and widely used, but KF can
only be applied to some linear systems. For nonlinear
systems like UAVs, KF has some limitations [12], but
extended some algorithms based on KF have also been
derived for nonlinear systems, for example, EKF [13],
Particle Filter (PF) [14], and UKF [15]. These filtering
methods have higher estimation accuracy compared to CF
and GD. PF relies heavily on the estimation of the initial
state and has the particle degeneracy problem; UKF is
more
accurate
than
EKF
and
avoids
the
complex
operations of Jacobi matrices for complex nonlinear
functions in EKF. [16] has proposed a CF for estimating
UAV attitude with small computational effort, however,
CF requires high sensor accuracy, and the filtering
performance decreases with increasing gyroscope drift
error. [17] has proposed KF fusion of gyroscope and
accelerometer data to calculate the optimal estimate to
correct the output error recursively, but this method does
not provide an accurate estimation of the yaw angle and
does not apply to nonlinear systems such as UAVs. [18]
has applied EKF to multi-axis vehicle attitude estimation,
EKF is an expansion of the nonlinear equations into a
first-order approximation using Taylor's formula, however,
when the linearization assumption does not hold, it leads
to a degradation of the filter performance. [19] has
utilized an EKF based on the direction cosine matrix for
UAV attitude estimation, but nine values in the direction
cosine matrix need to be computed, and the amount of
computation is more significant compared to the Euler
angles and quaternions, which will increase the processor
computational load and cannot be tracked in real-time. [20]
has proposed an Euler angle-based attitude estimation for
UKF multi-rotor UAVs, which improves the accuracy but
suffers from gimbal deadlocking.
In this paper, we propose a quaternion-based UKF data
fusion method for estimating the flight attitude of a
quadrotor
under
nonlinear
state
modeling.
We
use
STM32F103 as the core microcontroller, 3-axis gyroscope
and 3-axis accelerometer, and 3-axis magnetometer to
form a low-cost 9-axis attitude measurement system.
Sensor MPU6050 acquires gyroscope/accelerometer raw
data
information,
and
sensor
HMC5883l
obtains
magnetometer raw data information. The first step is to
calibrate the raw error of each sensor, which is the fixed
error of the sensor itself, to improve the accuracy of the
input information of the UKF. Updating the state variables
of the model using angular velocity information and
correction
of
observations
using
accelerometer
information and magnetometer information. Figure 1
illustrates the attitude measurement system, 
denotes
that the gyroscope correction outputs three-axis angular
velocity information, a indicates that the accelerometer
calibration outputs triaxial acceleration information, m
indicates
that
the
magnetometer
calibration
outputs
triaxial magnetic field strength information.
FIGURE 1. The QUKF-based attitude measurement system
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3320707
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

## Page 3

Author Name: Preparation of Papers for IEEE Access (February 2017)
VOLUME XX, 2017
4
II. MATHEMATICAL MODEL
A.
VISION SENSOR
Vehicles generally provide attitude information with a
heading attitude reference system (AHRS), this attitude
information includes roll angle, pitch angle, and yaw angle.
AHRS provides both a navigational coordinate system and an
airframe coordinate system, the navigation coordinate system
is the reference coordinate system used to solve the attitude
information of the aircraft, and in this article, we have chosen
the northeastern part of the earth as the navigational
coordinate system. The airframe coordinate system is fixed to
the vehicle and changes with the movement of the airframe;
the x-axis is aligned with the head direction, the y-axis is in
the same plane as the body, and in the same direction as the
right chord of the body, the z-axis is kept perpendicular to the
x-axis and y-axis respectively and pointing down the
airframe. As shown in Figure 2.
FIGURE 2. Navigation coordinate system and airframe coordinate
system
Expression of the navigation coordinate system in terms of
the direction cosine matrix to the airframe coordinate system
and the relational formula is built with attitude information,
as in:
cos cos  cos sin sin
sin cos  cos sin cos
sin sin
sin cos  sin sin sin
cos cos  sin sin cos
sin sin
sin                       cos sin                              cos cos
b
nR













































(1)
As in (1), n represents the navigation coordinate system,
b represents the airframe coordinate system,
b
n
R
represents a
rotation from the navigation coordinate system to the
airframe coordinate system, 
represents rotation of the
vehicle around x-axis, the angle of rotation is the roll angle,
represents the rotation of the vehicle around the y-axis, the
angle of rotation is the pitch angle. represents the rotation
of the vehicle around the z-axis, and the angle of rotation is
the yaw angle. (1) is the rotation matrix expressed in terms of
Euler angles, which satisfies
(
)
n
b
T
b
n
R
R

.
The rotation matrix expressed in terms of Euler angles is
straightforward, so the attitude information can be described
by the angle of rotation around the three directions. However,
it is easy to encounter gimbal lock, so it is easy to produce
singular values.
This can be avoided by describing the attitude information
in terms of quaternions (
0
1
2
3
[
 
 
 
]T
Q
q q q q

), so in this paper,
we use quaternions to represent the rotation relation, and the
quaternion satisfies the following relation:
(2)
2
2
2
2
0
1
2
3
1 2
0 3
1 3
0 2
2
2
2
2
1 2
0 3
0
1
2
3
2 3
0 1
2
2
2
2
1 3
0 2
2 3
0 1
0
3
1
2
  2(
)       2(
)
2(
)       
  2(
)
2(
)           2(
)   
n
b
q
q
q
q
qq
q q
qq
q q
R
qq
q q
q
q
q
q
q q
q q
qq
q q
q q
q q
q
q
q
q


























(3)
As in (3),
n
b
R
denotes the relational equation for the
rotation of the airframe coordinate system to the navigation
coordinate system and
describes the airframe attitude
information in quaternions, again there is the relation
(
)
b
n
T
n
b
R
R

.
B.
Calibration Of Sensor Raw Error
Manufacturers
in
the
production
of
MPU6050
and
HMC5883l such devices, due to process, technology, and
other reasons, result in certain defects in the sensor, so in the
actual application of the sensor output signal there are
specific
errors.
Therefore,
the
raw
data
output
from
gyroscopes, accelerometers, and magnetometers all have
errors, and such errors are deterministic errors, modeling the
error calibration:
(
)
(
)
(
)
e
a
e
m
e
R
c
a
a
R
a
b
m
R
m
m




















(4)
As in (4), , a , m are the data after calibration of
gyroscope, accelerometer and magnetometer respectively;
, a, mare gyroscope, accelerometer and magnetometer
raw data respectively;
e
,
ea ,
e
m are the zero bias error of
each sensor;
e
c



,
e
a
a
b

,
e
m
m

compensate for
the zero bias error of each sensor, respectively; R,
a
R ,
m
R
are the ratios of the maximum and minimum output
differences of the sensor in each axial direction, respectively,
used to compensate for scale factor errors and axle
misalignment of individual sensors;
16.4
c 
is the ratio of
the output range of the MPU6050 data register to the output
range of the gyroscope,
1638.35
b 
is the ratio of the output
range of the MPU6050 data register to the output range of the
accelerometer.
The gyroscope is placed on a horizontal plane at rest, and
by collecting multiple sets of data in each axis, the zero bias
2
2
2
2
0
1
2
3
1
q
q
q
q




This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3320707
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

## Page 4

Author Name: Preparation of Papers for IEEE Access (February 2017)
VOLUME XX, 2017
4
in each axis is equal to the average value of the data in that
axis; the accelerometer is calibrated using the six-plane
calibration method, in which the accelerometer's
X

,
Y

,
and
Z

axes are pointed toward the ground, and the same
data are collected in both directions for each axis, and the
average value of the data for each axis is calculated; the
magnetometer adopts the three-axis rotary table method, in
which the magnetometer is fixed on a high-precision three-
axis rotary table, and the rotary table is rotated around the X ,
Y , and Z
axes respectively by uniform rotation, and the
zero deviation of each axis is equal to the average value of
the data in that axis. The calibration parameters for each
sensor measured in this paper are as follows:
[1.567 
0.498 
0.787]
[0.975 
1.427 
1.977]
[0.035 0.065 0.075]
(1.005, 0.999, 1.013)
1.020 
0.005 0.010
0.067 0.966 
0.016
0.008 
0.014 1.080
(1.005 0.989 1.012)
T
e
T
e
T
e
a
m
a
m
R
diag
R
R
diag






































(5)
C.
Gyroscope-based State Update
The relationship between quaternions and the angle speed, as
in:
1
( )
2
dQ
Q
Q
dt





(6)
0 
 
 
   0     
  
( )
 
  0     
  
  
  0
x
y
z
x
z
y
y
z
x
z
y
x


































(7)
As in (7),
[
 
 
]
x
y
z



is the raw data of the gyroscope
measurement output after calibration,
x
、
y
、
z

are the
angular velocities of rotation about the
X , Y , and
Z coordinate axes, respectively;
( )


denotes the 4*4
opposite matrix. In the discrete equation, the state update
belongs to the next moment to the previous moment state
value. In each clock cycle T , it is known that the quaternion
1
tq and the angular velocity
1
t

at time
1
t 
, predictive
estimation of the quaternion
tq at time t using
1
tq 

, as in:
1
1
t
t
t
q
q
Tq




(8)
Obtain the state update equation with respect to the
quaternion, as in:
1
1
1
(
)
2
t
t
t
t
T
q
q
q







(9)
D.
Accelerometer Attitude Solving
Accelerometer as an inertial sensor to measure acceleration,
the measured output value is the acceleration of three axes in
the airframe coordinate system, denoted by
[
 
 
]
b
b
b
b T
x
y
z
a
a a a

.
According
to
the
measurement
principle,
when
the
accelerometer is at rest, it is only subjected to the
acceleration
of
gravity,
denoted
by
[0 0 ]
[0 0 1]
a
g
g


, g
(
2
9.8
/
g
m s

) denotes the
acceleration of gravity. When the vehicle is in motion, the
gravity acceleration information is assigned to three axes
according to the attitude angle of the airframe, referring to
the (3) we can get:
1
3
0
2
2
3
0
1
2
2
2
2
0
3
1
2
   2(
)
0
0
   2(
)
b
x
b
n
y
b
b
z
a
q q
q q
a
R
g
q q
q q
g
q
q
q
q
a
































(10)
From the three-axis components of the accelerometer output,
we can calculate roll angle and pitch angle, as in:
arcsin(
)
arctan(
)
x
y
z
a
g
a
a







(11)
E.
Magnetometer Attitude Solving
The magnetometer is used as an inertial sensor to measure
the magnetic field strength, and the measured output is the
magnetic induction in the three axes of the airframe
coordinate system. The magnetometer measurements in the
airframe
coordinate
system
are
expressed
as
[
 
 
]
b
b
b
b T
x
y
z
m
m m m

. In the navigational coordinate system,
the geomagnetic field always points north along the direction
of magnetic induction, has northward and perpendicular
components, and no eastward component, so the magnetic
field
strength
is
expressed
as
[
 
 
] (
0)
n
n
n
n T
n
x
y
z
y
m
m m m
m


.
When
the
airframe
coordinate system coincides with the geomagnetic field in
the navigation coordinate system,
[
 0 
]
b
n
n T
x
z
M
m
m

is the
output of the magnetometer. Since
b
n
M
m

, it satisfies
b
b
n
n
m
R M

, and by rotating it, we realize the conversion
between the airframe coordinate system and the navigation
coordinate system, and the relationship between the magnetic
field strengths of the two coordinate systems is expressed as:
                 
cos cos
sin
sin cos
(sin cos cos
cos sin
)
cos cos
(cos cos cos
sin sin
)
b
n
n
x
x
z
b
n
n
y
z
x
n
n
b
z
x
z
m
m
m
m
m
m
m
m
m











































(12)
Therefore, the component of the magnetic field strength in
the horizontal direction is:
sin
sin
cos
cos
cos
sin sin
sin cos
n
b
b
x
z
y
n
b
b
b
x
x
y
z
m
m
m
m
m
m
m

















(13)
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3320707
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

## Page 5

Author Name: Preparation of Papers for IEEE Access (February 2017)
VOLUME XX, 2017
4
Define the positive yaw angle when the head of the
airframe is turned clockwise, the yaw angle can be obtained
from (13), as in:
cos
sin
arctan
cos
sin sin
sin cos
b
b
y
z
b
b
b
x
y
z
m
m
m
m
m












(14)
F.
Quaternions And Euler Angle Conversions
A quaternion matrix can be constructed by rotating an axis
and the angle of rotation around that axis, as in:
0
cos
cos
cos
sin
sin
sin
2
2
2
2
2
2
1
cos
cos
sin
sin
sin
cos
2
2
2
2
2
2
2
sin
cos
sin
cos
sin
cos
2
2
2
2
2
2
3
sin
cos
cos
cos
sin
sin
2
2
2
2
2
2
q
q
q
q















































(15)
As in (15), can be launched
[ 0 1 2 3]T
Q
q
q q
q




.
G.
System Equation of State Design
Equation of state and measurement equations for quadrotors:
( , )
( , )
t
t
t
x
f x t
w
z
h x t
v






(16)
Due to the nonlinear characteristics of the aircraft system,
it can be assumed as a discrete nonlinear system with
Gaussian noise, as in:
1
1
(
, )
( )
t
t
t
t
X
F X t
W
Z
HX t
V









(17)
As in (16) and (17), X
represents the state vector of the
system, Z
is denoted as the measured output value of the
sensor at time t , The nonlinear functions F and H denote the
state transfer
matrix, the sensor measurement
matrix,
respectively;
t
W denotes the system noise of the equation of
state,
tV
denotes the system noise of the measurement
equation, and all obey the Gaussian distribution of the noise,
(0, )
t
W
N
S

,
(0, )
tV
N
R

, S and R denote the covariance
matrix of
t
W and
tV respectively.
In this paper, we use quaternions as system state variables,
that is
[ 0 1 2 3]T
X
q q q q

. Acceleration and magnetometer
solved
attitude
information
as
observations
in
the
measurement equation, that is
[ 0 1 2 3]T
Z
q q q q



. Included
among these:
1
0
0
0
0
1
0
0
( )
( )
0
0
1
0
2
0
0
0
1
T
F
X t






























(18)
1
0
0
0
0
1
0
0
0
0
1
0
0
0
0
1
H












(19)
III. Attitude Information Fusion Algorithm Design
Due to the nonlinear characteristics of the discretized
equations of state and measurement equations of quadrotors.
This paper processes nonlinear equations using UKF,
enabling status updates for precise attitude information. The
following equations can express the algorithm, as in:
Determine 2
1
n 
Sigma points at time
1
t , the sampling
points:
1
1
1
1
1
1
1
1
ˆ
,
0
ˆ
(
)
,
1
ˆ
(
)
,
1
2
i
t
t
i
t
t
t
i
t
t
t
X
i
X
n
P
i
n
X
n
P
i
n
n































(20)
Calculate the weights corresponding to the sampling points:
0
0
2
(1
)
,
1
2
2(
)
m
c
i
i
m
c
n
n
i
n
n

































(21)
As in (20) and (21),
1
i
t
is the sampling points in the
original state distribution selected by rule such that the mean
and covariance of these sampling points are equal to the
standard and covariance of the initial state distribution，n is
the number of state variables,
1
ˆ
t
X is the state variable at
moment
1
t 
, is a scaling parameter used to reduce
prediction error.
1
tP
is the error covariance matrix at time
1
t 
, 
is a parameter controlling the state of the
distribution of sampling points.
Substituting the points Sigma calculated in (20) into the
nonlinear equation of state (17):
|
1
1
(
), 
0
2
i
i
t t
t
F
i
n







(22)
Calculating one-step prediction and covariance matrices
for system state quantities:
2
|
1
|
1
0
ˆ
n
i
i
t t
t t
i
X





(23)
2
|
1
|
1
|
1
|
1
|
1
0
ˆ
ˆ
(
)(
)
n
i
i
i
T
t t
t t
t t
t t
t t
i
P
X
X
Q













(24)
Based
on
the
one-step
prediction
values,
the
UT
transformation is used again to produce new set of
Sigma points:
|
1
|
1
1
|
1
|
1
1
|
1
|
1
ˆ
,
0
ˆ
(
)
,
1
ˆ
(
)
,
1
2
i
t t
t t
i
t
t t
t t
i
t
t t
t t
X
X
i
X
X
n
P
i
n
X
X
n
P
i
n
n































(25)
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3320707
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

## Page 6

Author Name: Preparation of Papers for IEEE Access (February 2017)
VOLUME XX, 2017
4
The predicted Sigma points set are brought into the
measurement equation to obtain the predicted observations:
|
1,
0
2
i
i
t
t t
Z
HX
i
n





(26)
The mean of the system prediction and its covariance are
obtained by weighted summation:
2
0
ˆ
, 
0
2
n
i
i
i
t
t
i
Z
Z
i
n






(27)
2
0
ˆ
ˆ
(
)(
)
n
i
i
t
i
t
T
ztzt
t
i
t
i
i
P
Z
Z
Z
Z
R







(28)
2
|
1
0
ˆ
ˆ
(
)(
)
n
i
i
t
i
t
T
xtzt
t t
i
t
i
i
P
X
Z
Z
Z








(29)
Obtain the kalman gain matrix:
xtzt
t
ztzt
P
K
P

(30)
Finally update the state and covariance matrix:
|
1
ˆ
ˆ
ˆ
(
)
i
i
t
t t
t
t
t
X
X
K Z
Z




(31)
|
1
(
)T
t
t t
t
zkzk
t
P
P
K P
K



(32)
IV. Experimental Verification
In order to verify the effectiveness of the algorithm, we
choose a low-cost flight controller for our experiments,
STM32F103 as a microcontroller, inertial sensor MPU6050
as a 3-axis gyroscope and 3-axis accelerometer, HMC5883l
as a 3-axis magnetometer. We built a Pixhawk-based flight
experiment platform and conducted UAV dynamic flight
experiments outdoors, as shown in Figure 3. The data
collected by the High Precision Sensor MTI-300 is used as
the real data, and the data measured by the low-cost sensor is
used as the data required for attitude fusion, storing the
synchronized collected flight data on the SD card of the flight
control board, and set the sampling frequency to 20 HZ, and
we select continuous 30s attitude measurement data, finally,
data fusion of nine-axis data using Matlab. Comparison and
analysis of the data measured by the QUKF proposed in this
paper with EKF, CF, and high-precision attitude sensors. In
the experiment, according to the stability and accuracy of the
algorithm as the dominant conditions, after simulation and
debugging to selection the parameters
1
,
1

,
2

,
(0.001, 0.001, 0.001, 0.001)
S diag

,
(0.05, 0.05, 0.05, 0.05)
R diag

,
in order to ensure the feasibility of the algorithms, different
algorithms all use the same noise covariance matrix S and
R , and the initial values of the state variables are all set to
[1 0 0 0]T
X 
.
FIGURE 3. Quadrotor
Figure 4 represents the calibrated data of the gyroscope,
accelerometer, and magnetometer in the hovering condition.
Figures 5-7 indicate that the roll angle, pitch angle, and yaw
angle estimates of the low-accuracy sensors are compared
with the true values by applying different algorithms in the
hovering condition. As can be seen from Figure 5, the roll
angles estimated by QUKF, EKF, and CF are basically kept
around 0.7

and almost straight, and by zooming in, it can
be observed that the roll angles fused by the QUKF
algorithm are closer to the real values, so the stability of
QUKF is more excellent. As can be seen from Figure 6, the
pitch angles estimated by the three algorithms are basically
kept around
0.2

, and by zooming in, it can be observed
that both QUKF and EKF are closer to the real value. As can
be seen from Figure 7, the yaw angles estimated by the three
algorithms are basically kept at 66.7, by zooming in, it is
observed that the QUKF estimates are closer to the real
values and have excellent stability. Overall, the estimated
attitude angles of the three algorithms are basically consistent
with the real values in the hovering condition, and the
estimated attitude angles of QUKF are closer to the real
values than those of EKF and CF, tolerance is basically
within 0.2，and the stability is also more excellent.
FIGURE 4. Gyroscope, accelerometer, and magnetometer calibrated in
hovering state
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3320707
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

## Page 7

Author Name: Preparation of Papers for IEEE Access (February 2017)
VOLUME XX, 2017
4
FIGURE 5. Comparison of roll angle in hovering state
FIGURE 6. Comparison of pitch angle in hovering state
FIGURE 7. Comparison of yaw angle in hovering state
Figure
8
represents
the
data
of
the
gyroscope,
accelerometer, and magnetometer after calibration in an
outdoor dynamic flight environment. Figures 9-11 represent
the comparison of roll angle, pitch angle, yaw angle
estimation of the low accuracy sensor with the real values
using different algorithms in a motion environment. Based on
the comparison, it can be observed that all the three
algorithms perform well in attitude estimation and basically
track the real attitude angle. By observing 10s and 29s in
Figure 9, it can be observed that the QUKF estimates are
much closer to the true values, and the stability of both
QUKF and EKF is excellent, while the CF shows a large
amount of jitter. By observing 6s and 27s in Figure 10, It
can be observed that the QUKF estimates are closer to the
true values compared to EKF and CF, and the QUKF and
EKF curves are smoother and have better stability compared
to CF. By observing 11s and 28s in Figure 11, it can be
observed that the QUKF estimates are closer to the true
values, and both QUKF and EKF curves are smoother, while
CF is more volatile and less stable. Overall, all three
algorithms can basically track the real attitude angle in the
motion state, and the estimated attitude angle of QUKF is
more accurate compared to EKF and CF, and the curves of
QUKF and EKF are smoother, and the stability is more
excellent compared to CF.
FIGURE 8. Gyroscopes, accelerometers, magnetometers calibrated in
motion
FIGURE 9. Comparison of roll angle under motion
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3320707
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

## Page 8

Author Name: Preparation of Papers for IEEE Access (February 2017)
VOLUME XX, 2017
4
FIGURE 10.
Comparison of pitch angle under motion
FIGURE 11.
Comparison of yaw angle under motion
Comparison of the accuracy of attitude angle estimation
using two error analysis metrics, Root Mean Square Error
(RMSE) and Mean Absolute Error (MAE), respectively. As
shown in table 1:
TABLE 1. COMPARISON OF RMSE AND MAE
RMSE
MAE
roll
pitch
yaw
roll
pitch
yaw
QUKF
0.5288
0.6891
0.5821
0.3582
0.4224
0.4163
EKF
0.8122
0.8934
0.7526
0.7564
0.6827
0.6135
CF
1.1548
1.0438
1.0745
1.0652
0.8307
0.8677
From the data in the table, the attitude angle errors
estimated based on the QUKF are smaller than the latter two,
and based on the RMSE, it can be seen that the QUKF has an
average decrease of 0.2compared to the EKF estimation
error, and an average decrease of 0.5compared to the CF
estimation error. Overall, the attitude estimation accuracy of
QUKF for quadrotor UAVs is higher than that of EKF, CF
algorithm.
Conclude
In this paper, STM32F103 is used as the controller in
hardware, MPU6050 and HMC5883l are used as low-cost
sensors. Aiming at the nonlinear characteristics of the flight
environment of the aircraft, the QUKF algorithm with higher
estimation accuracy is proposed, filtering out Gaussian noise
encountered by sensors during vehicle flight by fusing the
corrected
data
from
gyroscopes,
accelerometers,
and
magnetometers, determining the attitude angle of the vehicle
by attitude solving. Finally, by analyzing and comparing with
EKF and CF algorithms, it is concluded that the accuracy of
QUKF estimation is higher than that of EKF and CF
algorithms, and the robustness is also better, which can
effectively improve the accuracy of attitude measurement.
Therefore, the attitude angle estimated by the low-precision
sensor designed in this paper through the fusion algorithm
can be similar to that of the high-precision sensor, which
meets the practical requirements of UAV attitude solving.
REFERENCES
[1]
Jiang F, Pourpanah F, Hao Q. Design, implementation, and
evaluation of a neural-network-based quadcopter UAV system[J].
IEEE Transactions on Industrial Electronics, 2019, 67(3): 2076-2085.
DOI: 10.1109/TIE.2019.2905808.
[2]
Passaro V M N, Cuccovillo A, Vaiani L, et al. Gyroscope technology
and applications: A review in the industrial perspective[J]. Sensors,
2017, 17(10): 2284. DOI: 10.3390/s17102284.
[3]
Gao L, Bourke A K, Nelson J. Evaluation of accelerometer based
multi-sensor versus single-sensor activity recognition systems[J].
Medical engineering & physics, 2014, 36(6): 779-785. DOI:
10.1016/j.medengphy.2014.02.012
[4]
Hashim H A, Brown L J, Mcisaac K. Nonlinear Stochastic Attitude
Filters on the Special Orthogonal Group 3: Ito and Stratonovich[J].
IEEE Transactions on Systems Man & Cybernetics Systems, 2018:1-
13. DOI: 10.1109/tsmc.2018.2870290.
[5]
Markley F L, Crassidis J, Cheng Y. Nonlinear attitude filtering
methods[C]//AIAA guidance, navigation, and control conference and
exhibit. 2005: 5927. DOI: 10.2514/6.2005-5927.
[6]
Welch G F. Kalman filter[J]. Computer Vision: A Reference Guide,
2020: 1-3. DOI: 10.1007/978-3-030-03243-2_716-1.
[7]
Garrett-Bakelman F E, Darshi M, Green S J, et al. The NASA Twins
Study:
A
multidimensional
analysis
of
a
year-long
human
spaceflight[J].
Science,
2019,
364(6436):
eaau8650.
DOI:
10.1126/science.aau8650
[8]
Kubelka V, Reinstein M. Complementary filtering approach to
orientation estimation using inertial sensors only[C]//2012 IEEE
international conference on robotics and automation. IEEE, 2012:
599-605. DOI: 10.1109/ICRA.2012.6224564.
[9]
Petrović M, Rakočević V, Kontrec N, et al. Hybridization of
accelerated gradient descent method[J]. Numerical Algorithms, 2018,
79: 769-786. DOI: 10.1007/s11075-017-0460-4.
[10] Li Q, Li R, Ji K, et al. Kalman filter and its application[C]//2015 8th
International Conference on Intelligent Networks and Intelligent
Systems
(ICINIS).
IEEE,
2015:
74-77.
DOI:
10.1109/ICINIS.2015.35.
[11] Koksal N, Jalalmaab M, Fidan B. Adaptive linear quadratic attitude
tracking control of a quadrotor UAV based on IMU sensor data
fusion[J]. Sensors, 2018, 19(1): 46. DOI: 10.3390/s19010046.
[12] Zhu Y, Liu J, Yu R, et al. Attitude solving algorithm and FPGA
implementation of four-rotor UAV based on improved mahony
complementary
filter[J].
Sensors,
2022,
22(17):
6411.
DOI:
10.3390/s22176411.
[13] Yang S, Baum M. Extended Kalman filter for extended object
tracking[C]//2017
IEEE
international
conference
on
acoustics,
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3320707
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

## Page 9

Author Name: Preparation of Papers for IEEE Access (February 2017)
VOLUME XX, 2017
4
speech and signal processing (ICASSP). IEEE, 2017: 4386-4390.
DOI: 10.1109/ICASSP.2017.7952985.
[14] Askari I, Haile M A, Tu X, et al. Implicit Particle Filtering via a
Bank of Nonlinear Kalman Filters[J].
2022, 145: 110469. DOI:
10.1016/j.automatica.2022.110469.
[15] Antonov S, Fehn A, Kugi A. Unscented Kalman filter for vehicle
state estimation[J]. Vehicle System Dynamics, 2011, 49(9): 1497-
1520. DOI: 10.1080/00423114.2010.527994.
[16] Noordin A, Basri M A M, Mohamed Z. Sensor fusion algorithm by
complementary filter for attitude estimation of quadrotor with low-
cost
IMU[J].
TELKOMNIKA
(Telecommunication
Computing
Electronics
and
Control),
2018,
16(2):
868-875.
DOI:
10.12928/telkomnika.v16i2.9020.
[17] Kaba A, Ermeydan A, Kiyak E. Model derivation, attitude control
and
Kalman
filter
estimation
of
a
quadcopter[C]//2017
4th
International Conference on Electrical and Electronic Engineering
(ICEEE).
IEEE,
2017:
210-214.
DOI:
10.1109/ICEEE2.2017.7935821.
[18] Ludwig S A, Burnham K D. Comparison of Euler estimate using
extended Kalman filter, Madgwick and Mahony on quadcopter flight
data[C]//2018 International Conference on
Unmanned Aircraft
Systems
(ICUAS).
IEEE,
2018:
1236-1241.
DOI:
10.1109/ICUAS.2018.8453465.
[19] Somasiri J, Chandima D P, Jayasekara A G B P. Extended kalman
filter based autonomous flying system for quadcopters[C]//2018 2nd
International Conference On Electrical Engineering (EECon). IEEE,
2018: 130-137. DOI: 10.1109/EECon.2018.8541019.
[20] Kada B, Munawar K, Shaikh M S, et al. UAV attitude estimation
using nonlinear filtering and low-cost mems sensors[J]. IFAC-
PapersOnLine,
2016,
49(21):
521-528.
DOI:
10.1016/j.ifacol.2016.10.655.
TAO
LIANG
received
the
B.S.
degree
in
Measurement
and
Control
Technology
and
Instrumentation from the Sichuan University of
Science and Engineering, Yibin, China, in 2020,
he is currently pursuing the M.S. degree in the
Sichuan University of Science and Engineering,
Yibin, China. His main research interest includes
UAV Attitude Estimation and Control.
KAILAI YANG received the B.S. degree in
Process Equipment and Control Engineering from
the
Sichuan
University
of
Science
and
Engineering, Yibin, China, in 2020, and the M.S.
degree
in
Mechanical
Engineering
from
the
Sichuan University of Science and Engineering,
Yibin, China, in 2023. His main research interests
are the digitalization of intelligent equipment and
manufacturing process.
CHENJIE
LI
received
the
B.S.
degree
in
Measurement
and
Control
Technology
and
Instrumentation from the Sichuan University of
Science and Engineering, Yibin, China, in 2021,
he is currently pursuing the M.S. degree in the
Sichuan University of Science and Engineering,
Yibin, China. His main research interest includes
data processing.
QINGWEN DENG received the B.S. degree in
Electrical engineering and automation from the
Sichuan University of Science and Engineering,
Yibin, China, in 2022, he is currently pursuing
the M.S. degree in the Sichuan University of
Science and Engineering, Yibin, China. His
main research interest includes data processing.
JUNLIN LI received the B.S. degrees in
Internet of Things Engineering from the
Sichuan University of Arts and Science,
Dazhou, China, in 2020, he is currently
pursuing the M.S. degree in the Sichuan
University of Science and Engineering,
Yibin, China. His main research interest
includes uav path planning and obstacle
avoidance.
XIANGUO TUO was born in Hunan,
China, in 1965. He received the Ph.D.
degree from the Chengdu University of
Technology,
Chengdu,
China.
He
is
currently a Professor with the Sichuan
University of Science and Engineering. His
research
interests
include
nuclear
technology
theory,
nuclear
geophysical
exploration
methods,
development
of
nuclear electronic instruments, radiation
environment assessment, nuclide migration,
and environmental monitoring and disaster warning methods.
QIANG HAN was born in ShanDong,
China, in 1987. He received the Ph.D.
degree from the Southwest university of
science and technology, Mianyang, China.
He
is currently a lecture with the Sichuan
University of Science and Engineering. His
research
interests
include
nonlinear system control, complex networks,
cooperative control of UAV formation.
SHIDONG
CHEN
received
the
B.S.
degree in Building electrical and intelligent
from
the
Yangtze
Normal
University,
Chongqing, China, in 2021, he is currently
pursuing the M.S. degree in the Sichuan
University of Science and Engineering,
Yibin, China. His main research interest
includes Nonlinear system control.
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3320707
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4
