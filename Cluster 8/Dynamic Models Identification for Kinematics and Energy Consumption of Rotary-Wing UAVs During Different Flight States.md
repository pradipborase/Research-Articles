# Dynamic Models Identification for Kinematics and Energy Consumption of Rotary-Wing UAVs During Different Flight States.pdf

## Page 1

Citation: Falkowski, K.; Duda, M.
Dynamic Models Identiﬁcation for
Kinematics and Energy Consumption
of Rotary-Wing UAVs during
Different Flight States. Sensors 2023,
23, 9378. https://doi.org/
10.3390/s23239378
Academic Editor: Biswajeet
Pradhan
Received: 31 August 2023
Revised: 16 November 2023
Accepted: 20 November 2023
Published: 24 November 2023
Copyright:
© 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
sensors
Communication
Dynamic Models Identiﬁcation for Kinematics and Energy
Consumption of Rotary-Wing UAVs during Different
Flight States
Krzysztof Falkowski 1,* and Michał Duda 2
1
Avionics Department, Institute of Aviation Technology, Faculty of Mechatronics, Armament and Aerospace,
Military University of Technology, 00-908 Warsaw, Poland
2
Doctoral School, Military University of Technology, 00-908 Warsaw, Poland; michal.duda@wat.edu.pl
*
Correspondence: krzysztof.falkowski@wat.edu.pl
Abstract: This article presents the method of identifying dynamic models for different ﬂight states
of a rotary-wing UAV for simulations. Experimental ﬂights with real-life UAVs were conducted to
obtain data necessary for identiﬁcation. Dynamic models were identiﬁed with time series methods
performed using Matlab R2022b software. Such models can later be implemented in simulations to
represent the behavior of real-life objects. Simulation is the ﬁrst stage of developing a real-life UAV
system, where prototyping with physical models is problematic. Therefore, obtaining accurate models
is crucial for the simulation process to be reliable. Presented methods do not require knowledge of
UAV construction, and complex mathematical equations do not need to be derived. Also, veriﬁcation
of obtained models was performed to make sure that they were identiﬁed correctly. In particular, the
presented method was proven effective and successfully used in some applications.
Keywords: dynamic models; identiﬁcation; UAV; simulation
1. Introduction
Interest in applications of quadrotor drones is rising rapidly due to the development
of robotic technologies. Scientists worldwide propose and research new control algorithms
that can be implemented to execute speciﬁc tasks or improve existing solutions. Many of
them are theoretical dissertations not transferred to practical applications. The research
provided in this paper focuses on an attempt to simulate a real-life UAV with all its
physical parameters.
Deployment of a real-life UAV system requires many robots to be built, programmed,
and launched. The time and cost of those processes can grow signiﬁcantly, especially for
testing and prototyping [1]. This makes simulations the ﬁrst complex system preparation
stage [2]. Implementing a virtual system allows for conducting a series of tests with different
conditions using only a PC. Such tests are not dependent on the weather, do not require
robot maintenance, and can be terminated if any malfunction appears [3]. Prototyping an
algorithm for maneuvering real-life UAVs can be dangerous for the surroundings and the
robot [4].
Most of the research focuses on control algorithms, a set of rules that deﬁnes how
robotic agents propagate throughout the area. Tests using virtual simulations provide the
mathematical output of the robot’s behavior, and often, their physical parameters are either
not addressed or simpliﬁed. The more precise the data implemented in the simulation,
the more realistic its output is. In the case of simulating a UAV’s behavior, not only the
commanding algorithm matters but also the dynamics of its movement. Simulation of a
UAV requires knowledge of its physical parameters and dynamics. Every neglection or
simpliﬁcation at such an early research stage can lead to incorrect conclusions, affecting
further real-life applications [5,6].
Sensors 2023, 23, 9378. https://doi.org/10.3390/s23239378
https://www.mdpi.com/journal/sensors

## Page 2

Sensors 2023, 23, 9378
2 of 11
In the case of practical applications, energy consumption is a crucial factor in the usage
of autonomous robots, especially UAVs [7]. The energy used to perform the task should be
addressed in the research, as UAVs depend highly on their battery life. A power source
deﬁnes their performance, such as velocities, altitude, capacity, etc. [8,9].
A speciﬁc ﬁeld that is signiﬁcantly based on simulations and modeling is formation
ﬂights and swarms of UAVs. Due to the numerous agents required to perform, it is much
easier to model and simulate them virtually rather than prepare the same number of
physical objects. The literature provides a signiﬁcant amount of research regarding multi-
agent systems, where such systems are modeled. As shown by Huang, a second-order
consensus algorithm can resolve collision avoidance in formations [10]. UAV formation
obstacle avoidance can be performed using an artiﬁcial potential ﬁeld and a consensus
algorithm [11]. The trajectory of ﬂight for every agent in the formation can be planned
before starting the mission [12]. Even a mission of tracking a moving target with a formation
of UAVs can be modeled and simulated, as proven in [13]. Although such research proved
correct in all these cases, it is based on mathematical equations and analytical contemplation.
Such an approach is time-consuming. Also, it requires precise knowledge of UAV internal
parameters, or simpliﬁcations are assumed that ignore the physical aspect of the agents.
The next step of every theoretical research should be implementation in real-life systems,
which is often not addressed. Our study presents a method for obtaining models for
UAV ﬂights based on experimental data that can later be implemented into simulations of
single-object or multi-agent systems. Such an approach ensures the model’s compatibility
with a physical object and is more applicable in practical solutions. The conﬂict in Ukraine
showed that UAV systems can be prototyped from available UAVs that are not necessarily
made for military purposes. An ability to rapidly identify models of such objects might
come in handy in many military applications, especially when time is essential.
Similar studies regarding preparing dynamic models for UAVs have already been
performed and described in the literature. As shown in [14], dynamic models of UAVs
can be derived mathematically, including speciﬁc factors such as weather conditions,
ﬂying speed, and payload. This approach requires complex mathematical methods and
knowledge of the modeled object [15]. The other approach assumes that it is possible to
collect experimental data using real-life objects and subsequently identify models with it.
As presented in [16], creating energy consumption models for UAVs for their different ﬂight
states is possible. Such research can also be extended to ﬁnd and impact factors such as
climb rate or desired altitude [17]. All such methods prove their efﬁciency. Our study used
similar identiﬁcation methods, extending them with different ﬂight stages, particularly
models for horizontal acceleration and deceleration, which could be used in modeling
collision avoidance—a critical feature of every aerial vehicle system.
This paper presents a practical approach to identifying dynamic models for rotary-
wing UAVs. Experimental ﬂights were performed, which allowed the collection of ﬂight
data for the UAVs and thus helped to improve the precision of data used in simulations.
Such an approach permitted performing simulations close to the actual behavior of UAVs
without solving complex mathematical formulas regarding quadrotors. This was especially
useful when the consumption of energy was calculated. Also, the method proved to be
quicker and relatively simple and focused on physical systems over theoretical contempla-
tions that often cannot be transferred straight into real-life applications.
2. Materials and Methods
The main goal of the presented research was to build a control system for a UAV. The
study was divided into four stages as follows:
1.
Prepare a simulation program executing a desired algorithm.
2.
Conduct experimental ﬂights with real-life UAVs to collect ﬂight data for the identiﬁ-
cation of dynamic models.
3.
Identify dynamic models of UAVs in examined ﬂight stages.

## Page 3

Sensors 2023, 23, 9378
3 of 11
4.
Implement obtained dynamic models into the simulation. Conduct tests and gather
and analyze results.
All study stages were described in more detail in the other parts of this paper.
2.1. Physical Parameters in Simulations of UAVs
Before launching a real-life system, the ﬁrst step was to test it in virtual simulations.
This stage required models of the objects to be implemented into the simulation as a
representation of real-life objects. The more accurate those models were, the more realistic
the simulation output was.
Knowing the drones’ dynamic models was vital in conducting the simulations for two
reasons. Firstly, it allowed us to correctly measure the time and energy consumed by the
UAVs while performing the mission. Those two factors were signiﬁcant for the optimization
of the performance. Drones operated in different ﬂight stages during the simulation, as
presented in Figure 1. During all of them, they consumed energy at different rates, and
knowing those rates enabled the calculation of total energy consumption. UAV systems are
known for their relatively low battery capacities, and optimizing the performance of drone
systems according to energy consumption is one of the main factors to include in research.
Secondly, the time required to complete transition states (accelerating, climbing, etc.) and
maximal velocities enabled us to derive the total time needed to ﬁnish the task.
Figure 1. Diagram of ﬂight states.
The second reason for identifying dynamic models of the drones was the safety and
ﬂuency of their movement. Due to the implementation of the collision avoidance feature,
knowing the distance required to accelerate or decelerate was necessary because it was
vital for the path planning of the drones. The distance covered during stopping was crucial
as the algorithm needed to compute when the drones had to start decelerating to avoid a
collision if such a situation appeared.
2.2. Experimental Flights and Data Collection
The mathematical models can be estimated by the identiﬁcation method. This method
uses time series models such as ARX, AR, and ARMAX. The transfer function can be
estimated from the ARX model:
Y(z) = G(z)U(z) + H(z)E(z),
(1)
where Y(z)—the Z transform of an output signal, U(z)—the Z transform of an input signal,
E(z)—the Z transform of the white noise, G(z) = B(z)
A(z)—a transfer function in terms of z
operator, and H(z) =
1
A(z)—a color ﬁlter in terms of z operator. A(z), B(z)—polynomials
in terms of z operator.

## Page 4

Sensors 2023, 23, 9378
4 of 11
The transfer function of an identiﬁed model can be converted from a digital model to
an analog model. The continuous transfer function is equal:
G(s) ∼= G(z)| f orTs,
(2)
where Ts—the sampling period.
The authors of the stochastic recovery path simulation need a model of take-off,
landing and cruise ﬂight, acceleration, and deacceleration of the UAV. We assume that the
UAVs will not change altitude at the operational zone. The UAV quadrotor was used to
conduct the identiﬁcation experiment. The quadrotor is presented in Figure 2.
 
Figure 2. The UAV used for identiﬁcation tests.
The experiments were divided into the vertical and horizontal movement of the UAV.
The vertical move study included take-off to an altitude of 100 m. Next, the altitude
increased to 200 m, 300 m, and 400 m and decreased to 300 m, 200 m, and 100 m. The last
point of the study was landing. The UAV hovered at each point of the study. It took the
same position (latitude and longitude), and the ﬂight controller stabilized and corrected
the angular orientation of the UAV. The altitude ﬂight is presented in Figure 3.
Figure 3. The proﬁle of altitude recorded during the experiment.
The next experiment applied to horizontal movement. The UAV took off to an altitude
of 200 m and moved to the waypoint. There, the UAV changed the heading and returned
to the point of take-off, and the UAV landed. The UAV had a deﬁned latitude, longitude,
and altitude of the take-off and waypoint. The maximum airspeed was 10 m/s, as deﬁned
in the ﬂight plan. The airspeed proﬁle is presented in Figure 4.

## Page 5

Sensors 2023, 23, 9378
5 of 11
 
Figure 4. The proﬁle of airspeed recorded during the experiment.
The mechanical and electrical parameters were recorded during identiﬁcation exper-
iments. The voltage, current, airspeed, vertical speed, altitude, latitude, longitude, and
reference airspeed and altitude were recorded. The experiment enabled us to obtain the
transfer function between the reference value and energy. The transfer functions were
estimated for the take-off, climbing, descending, cruise, and landing of the UAV.
3. Results
3.1. Identifying Dynamic Models
When experimental data were collected, it was possible to identify dynamic models
for every ﬂight state. The models were identiﬁed according to a section of gathered data
corresponding to the same state in actual ﬂight. Then, to verify it, dynamic models were
compared to a suitable part of data from other ﬂights. Finally, the entire ﬂight was simulated
using identiﬁed models mimicking the real-life test, and it allowed us to compare the total
energy consumption and scale of errors.
Identiﬁcation was performed in Matlab R2022b. Input data were control signals
from the ﬂight controller, and output data were registered ﬂight parameters. Identiﬁed
parameters were a change of power over time, vertical displacements, and horizontal
velocities over time during every considered ﬂight state. The dynamic models were
presented as a continuous time transfer function.
The only difference was hover, which was considered a static state; hence, dynamic
model identiﬁcation could not be performed for it. Knowing that it depended on height [9],
the power was calculated as the average power required to hover at a given altitude. Then,
knowing the result for a few different altitudes, the dependence of power on time was
approximated with function. According to Rotratu [18], the power required to hover is
given by:
P =
T
2
3
p
2ρA
(3)
where T—total thrust force, A—total area swept by rotors, and ρ—air density.
Assuming that during hover, T and A are constant, power depends on air density,
which in International Standard Atmosphere [19] can be approximated as a reversed
exponential proportional to ﬂight altitude H. In this case, the power required to hover can
be written as:
P = K ·Hz
(4)
where K =
T
2
3
√
2A = const, z—proportion exponent, and H—ﬂight altitude.
Using collected data, the equation describing power required to hover on ﬂight altitude
H was approximated with:
P(H) = 119.49H0.02 [W]
(5)

## Page 6

Sensors 2023, 23, 9378
6 of 11
3.1.1. Vertical Movement Models
The ﬁrst dynamic models to be identiﬁed were vertical movements: ascending and
descending. The data for the process were four subsequent climbs by 100 m from 0 to
400 m for ascending. Analogically, there were four subsequent decreases by 100 m from
400 m to 0 for the descent. Models for the altitude changes were identiﬁed together for
both states, and models of power were created separately. A comparison of experimental
data and identiﬁed models for altitude change is shown in Figure 5.
 
Figure 5. The control signal and characteristic comparison of experimental data and simulation
for altitude.
As seen in Figure 5, the simulated characteristic matches the experimental data; hence,
the simulation can be assumed to mimic the vertical movement of the drone with sufﬁcient
precision. The following transfer function describes the identiﬁed model:
G1(s) = e−2.9s
0.03071
s2 + 0.2923s + 0.03071
(6)
The second part of the identiﬁcation was made for the power required to climb and
descend to a 100 m difference in altitude. As the system was assumed to be linear, offsets
were brought to 0, so as not to break homogeneity and superposition principles. Then, it
was added to the stable state power required for hovering. The power characteristics for
climb and descent are shown in Figures 6 and 7.
Figure 6. The control signal and characteristic comparison of experimental data and simulation for
power change during climbing.

## Page 7

Sensors 2023, 23, 9378
7 of 11
 
Figure 7. The control signal and characteristic comparison of experimental data and simulation for
power change during descending.
As can be seen, at the beginning of the climb, the power rapidly increased as the drone
had to accelerate upwards. At some point, the UAV reached sufﬁcient speed to reach the
desired altitude, requiring less and less thrust. Hence, the power started to decrease. At the
climb’s ﬁnal stage, the drone had to lose gathered speed using the force of gravity. At that
point, the power dropped below a stable state shortly after stabilizing to the value required
to hover. The identiﬁed model for power during the climb is presented below:
G2(s) = e−0.2s
0.07023s + 0.02383
s2 + 0.006887s + 0.06957
(7)
When the drone needed to descend, power ﬁrst dropped, and the reduced thrust
became lower than the force of gravity, making the drone accelerate downwards. At
some point, the power rose to slow the rate of descent. Subsequently, the thrust had to
grow over the force of gravity for some time to lose downward velocity and stabilize the
ﬂight to hover at the desired altitude. The transfer function for power during descent is
presented below:
G3(s) = e−0.5s 0.09489s −0.00001339
s2 + 0.228s + 0.05344
(8)
In both cases, the experimental data was distorted by noise that could not be seen in
the simulated response. Optical evaluation allowed us to conclude that the signal trends
were similar in both cases, yet further validation of the models had to be conducted.
3.1.2. Horizontal Movement Identiﬁcation
Analogical identiﬁcation was performed for horizontal movement. The ﬂight states
were accelerating, moving with constant velocity, and decelerating (stopping) as presented
in Figure 8. The energy consumption had linear dependence on acceleration and ﬂy-
ing with constant velocity. While accelerating, the temporal power grew proportionally
to velocity, and during the constant speed movement, the energy consumption settled
around a constant value. This value was calculated as an average taken from the segment
where the drone ﬂew with constant velocity. The identiﬁed model for horizontal ﬂight is
presented below:
G4(s) = e−0.6s
0.03569
s2 + 0.935s + 0.3588
(9)

## Page 8

Sensors 2023, 23, 9378
8 of 11
Figure 8. The control signal and characteristic comparison of experimental data and simulation for
airspeed during horizontal ﬂight.
When the drone was commanded to stop, the desired velocity was instantly changed
to 0, so the UAV not only aborted the ﬂying forward but also tried to stop in the shortest
time. Hence, it rotated backward and created counter thrust to its movement direction,
creating backward force. The power change for deceleration is shown in Figure 9.
Figure 9. The control signal and characteristic comparison of experimental data and simulation for
power during deceleration.
As can be seen, after being commanded to stop, the power consumption rapidly
increased as the drone started the backward rotation and increased the thrust. Then, it
rotated forward, decreasing the power to settle in a hover. Below, the identiﬁed transfer
function for power change during deacceleration is presented:
G5(s) = e−0.6s
0.02583s −0.3294
s2 + 1.905·10−10 s + 0.2492
(10)
Knowledge of dynamic changes in airspeed (9) provided the information required to
simulate the collision avoidance feature in the systems. For example, the distance needed
to stop the UAV can be derived from the model. Also, the movement dynamics allowed
us to forecast further positions of the drones and predict conﬂicting conﬁgurations. Also,
whenever a UAV is obligated to stop, it consumes additional energy that can be calculated
using the identiﬁed model (10).
3.2. Model Veriﬁcation
After identifying the dynamic models, the next step is their veriﬁcation. This is
required to prove that identiﬁed models represent different cases. The other experimental

## Page 9

Sensors 2023, 23, 9378
9 of 11
ﬂight was considered, and its ﬂight plan was recreated in simulation. Next, the experimental
and simulated data were compared.
As seen in Figure 10, the nature of both characteristics was the same. Flat segments
and peaks were synchronized and had a similar magnitude. Yet, the charts could have been
more perfectly aligned as their height was mainly deﬁned by the constant power required
to remain at altitude. This value depends on many factors such as atmospheric conditions,
winds, etc., so if they were different in compared attempts, the average power required to
hover also differed.
Figure 10. Characteristic comparison of experimental data and simulation for power change during
the entire ﬂight for veriﬁcation.
Nevertheless, such comparisons proved that most of the identiﬁcation was performed
correctly. It also showed how vital the power required to hover is for UAVs and how
volatile that variable is.
4. Discussion
This article describes a method for identifying dynamic models of UAV ﬂight. As
shown in this paper, obtaining dynamic models of certain maneuvers of quadrotor robots
is possible without deriving a complete mathematical model, which is complex for such
objects. Properly conducted experimental ﬂights with data recording are required to
perform identiﬁcation.
This method is useful, especially regarding energy consumption and temporal power
during ﬂight stages. Battery capacity is one of the most signiﬁcant challenges of present
UAVs, and energy characteristics are integral to mission planning. The presented method
allows us to identify the power characteristics of ﬂying UAVs quickly.
In the case of rotary-wing UAVs, the most critical ﬂight state is remaining at a constant
altitude. During a hover or while performing maneuvers, a signiﬁcant part of the generated
thrust has to be directed down to counteract the force of gravity. The presented results
show that the gross amount of temporal energy had to be consumed so the robot would not
fall. Therefore, correctly identifying this power is crucial in preparing a UAV ﬂight model.
Identiﬁed models for certain ﬂight states can be implemented in virtual simulations
of the UAV. This way, simulations become more realistic while remaining in the virtual
process. Kinematic models allowed us to mimic the movement of the UAVs, which helped
us reproduce the acceleration and stopping distances, which are crucial in path planning
and collision avoidance. Power parameter models allow us to derive energy consumption
for the entire ﬂight.
Simulating and deriving the power characteristics throughout the entire ﬂight of the
UAV allows for calculating the total energy that must be consumed to fulﬁll the planned
mission. Such a study improves the path-planning process with another factor, which is
especially signiﬁcant for rotary-wing UAVs. Thanks to that, it is possible to optimize the
total energy consumption of the system.

## Page 10

Sensors 2023, 23, 9378
10 of 11
5. Conclusions
The identiﬁcation method can be useful for studies on UAVs when researchers want to
avoid deeply investigating UAV construction and the relations between power consumption
and component structure. This method allows us to bypass complex mathematical methods,
but it requires a real object to be available for experimental data collection.
Power consumption is a crucial parameter for every system based on UAVs, especially
rotary-wing robots. Methods that allow us to estimate energy consumed in a mission
beforehand help to better prepare for it. It is especially visible in swarm systems, where
estimated performance and errors are multiplied by the number of actors in the swarm.
Presented validation data showed a misalignment of experimental and simulated
data, which was a difference of a constant value over the entire chart. The validation data
could have been gathered in different atmospheric conditions, or other unidentiﬁed factors
inﬂuenced the results. This shows how rotary-wing UAVs are susceptible to various factors
and noise. On the one hand, it shows how important it is to collect experimental data in
ideal conditions; on the other hand, in real-life applications, conditions will probably not
be perfect, and this should also be included in simulations.
In further studies, models will be implemented in simulations of swarms performing
the Stochastic Coverage Task. Using acquired models should allow us to estimate the total
energy and time required to complete the mission, and information on acceleration and
deceleration (braking) will be useful for motion planning and collision avoidance.
Author Contributions: Conceptualization, K.F. and M.D.; methodology, K.F. and M.D.; software,
M.D.; validation, K.F.; formal analysis, K.F.; investigation, K.F. and M.D.; resources, K.F.; data curation,
M.D.; writing—original draft preparation, K.F. and M.D.; writing—review and editing, K.F. and
M.D.; visualization, M.D.; supervision, K.F.; project administration, K.F.; funding acquisition, K.F. All
authors have read and agreed to the published version of the manuscript.
Funding: The article contains partial results of research work ﬁnanced by the National Center for
Research and Development as part of competition 4/SZAFIR/2021 and contract DOB-SZAFIR/
01/B/023/04/2021.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data are contained within the article.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Sanchez-Lopez, J.L.; Pestana, J.; De La Puente, P.; Campoy, P. A reliable open-source system architecture for the fast designing
and prototyping of autonomous multi-uav systems: Simulation and experimentation. J. Intell. Robot. Syst. 2016, 84, 779–797.
[CrossRef]
2.
Soria, E.; Schiano, F.; Floreano, D. SwarmLab: A MATLAB drone swarm simulator. In Proceedings of the 2020 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), Las Vegas, NV, USA, 24 October–24 January 2020.
3.
de Winter, J.C.F.; van Leeuwen, P.M.; Happee, R. Advantages and Disadvantages of Driving Simulators: A Discussion. In
Proceedings of the Measuring Behavior 2012 8th International Conference on Methods and Techniques in Behavioral Research,
Utrecht, The Netherlands, 28–31 August 2012; pp. 47–49.
4.
Higgins, F.; Tomlinson, A.; Martin, K.M. Threats to the swarm: Security considerations for swarm robotics. Int. J. Adv. Secur. 2009,
2, 288–297.
5.
Popov, L.N. Drone Swarm Simulation. Ph.D. Thesis, University of Houston, Houston, TX, USA, 2020; p. 8.
6.
Gu, W.; Valavanis, K.P.; Rutherford, M.J.; Rizzo, A. UAV Model-based Flight Control with Artiﬁcial Neural Networks: A Survey.
J. Intell. Robot. Syst. 2020, 100, 1469–1491. [CrossRef]
7.
Li, J.; Xiong, Y.; She, J.; Wu, M. A path planning method for sweep coverage with multiple UAVs. IEEE Internet Things J. 2020, 7,
8967–8978. [CrossRef]
8.
Dudek, M.; Tomczyk, P.; Wygonik, P.; Korkosz, M.; Bogusz, P.; Lis, B. Hybrid fuel cell–battery system as a main power unit for
small unmanned aerial vehicles (UAV). Int. J. Electrochem. Sci. 2013, 8, 8442–8463. [CrossRef]
9.
Cesare, K.; Skeele, R.; Yoo, S.H.; Zhang, Y.; Hollinger, G. Multi-UAV exploration with limited communication and battery. In
Proceedings of the 2015 IEEE International Conference on Robotics and Automation (ICRA), Seattle, WA, USA, 26–30 May 2015.

## Page 11

Sensors 2023, 23, 9378
11 of 11
10.
Huang, Y.; Tang, J.; Lao, S. UAV group formation collision avoidance method based on second-order consensus algorithm and
improved artiﬁcial potential ﬁeld. Symmetry 2019, 11, 1162. [CrossRef]
11.
Wang, N.; Dai, J.; Ying, J. UAV formation obstacle avoidance control algorithm based on improved artiﬁcial potential ﬁeld and
consensus. Int. J. Aeronaut. Space Sci. 2021, 22, 1413–1427. [CrossRef]
12.
Wang, Y.; Wang, D.; Zhu, S. Cooperative moving path following for multiple ﬁxed-wing unmanned aerial vehicles with speed
constraints. Automatica 2019, 100, 82–89. [CrossRef]
13.
Doostmohammadian, M.; Taghieh, A.; Zarrabi, H. Distributed estimation approach for tracking a mobile target via formation of
UAVs. IEEE Trans. Autom. Sci. Eng. 2021, 19, 3765–3776. [CrossRef]
14.
Thibbotuwawa, A.; Nielsen, P.; Zbigniew, B.; Bocewicz, G. Energy consumption in unmanned aerial vehicles: A review of energy
consumption models and their relation to the UAV routing. In Information Systems Architecture and Technology: Proceedings of 39th
International Conference on Information Systems Architecture and Technology–ISAT 2018: Part II; Springer International Publishing:
Berlin/Heidelberg, Germany, 2019; pp. 173–184.
15.
Chen, C.; Shen, L.; Zhang, D.; Zhang, J. Mathematical modeling and control of a tiltrotor UAV. In Proceedings of the 2016 IEEE
International Conference on Information and Automation (ICIA), Ningbo, China, 1–3 August 2016.
16.
Góra, K.; Smyczy´nski, P.; Kujawi´nski, M.; Granosik, G. Machine Learning in Creating Energy Consumption Model for UAV.
Energies 2022, 15, 6810. [CrossRef]
17.
Abeywickrama, H.V.; Jayawickrama, B.A.; He, Y.; Dutkiewicz, E. Comprehensive energy consumption model for unmanned
aerial vehicles, based on empirical studies of battery performance. IEEE Access 2018, 6, 58383–58394. [CrossRef]
18.
Rotaru, C.; Todorov, M. Helicopter Flight Physics. In Flight Physics Models, Techniques and Technologies; Volkov, K., Ed.; IntechOpen:
London, UK, 2018; ISBN 978-953-51-3807-5.
19.
Cavcar, M. The International Standard Atmosphere (ISA). 2000. Available online: https://scholar.google.com/citations?user=
WpEp_wcAAAAJ&hl=en (accessed on 30 August 2023).
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
