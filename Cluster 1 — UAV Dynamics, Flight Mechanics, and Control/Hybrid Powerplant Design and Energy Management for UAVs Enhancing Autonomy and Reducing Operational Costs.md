# Hybrid Powerplant Design and Energy Management for UAVs Enhancing Autonomy and Reducing Operational Costs.pdf

## Page 1

Academic Editor: Tek Tjing Lie
Received: 2 May 2025
Revised: 2 June 2025
Accepted: 6 June 2025
Published: 12 June 2025
Citation: Quintana, J.A.; Bordons, C.;
Esteban, S.; Delgado, J. Hybrid
Powerplant Design and Energy
Management for UAVs: Enhancing
Autonomy and Reducing Operational
Costs. Energies 2025, 18, 3101. https://
doi.org/10.3390/en18123101
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
Article
Hybrid Powerplant Design and Energy Management for UAVs:
Enhancing Autonomy and Reducing Operational Costs
Javier A. Quintana 1
, Carlos Bordons 1,2,*
, Sergio Esteban 3,*
and Julian Delgado 4
1
ENGREEN—Laboratory of Engineering for Energy and Enviromental Sustainability, Universidad de Sevilla,
41092 Seville, Spain; jquintana3@us.es
2
Department of Systems Engineering and Automation, Universidad de Sevilla, 41092 Seville, Spain
3
Department of Aerospace Engineering, Universidad de Sevilla, 41092 Seville, Spain
4
Zelenza S.L., 28053 Madrid, Spain; jdelgado@zelenza.com
*
Correspondence: bordons@us.es (C.B.); sesteban@us.es (S.E.)
Abstract: This study presents the design of a hybrid powerplant for unmanned aerial
vehicles (UAVs), improving its autonomy compared to power systems based solely on
batteries. The powerplant is designed for the Mugin EV-350 aircraft. Using experimental
data from electric motors in a wind tunnel and fuel cells, a comparative analysis of different
energy management strategies, such as fuzzy logic and passive, is conducted to reduce the
operational and maintenance costs. A Python-based software program is developed and
utilized for the real-time implementation and simulation of energy management strategies,
with data collected in databases. This study integrates experimental data (wind tunnel
and fuel cells) with real-time EMS strategies, and simulation-based predictions indicate
practical improvements in endurance and cost reduction, as well as an increase in flight
autonomy of 50%.
Keywords: energy management; system integration; electric propulsion systems
1. Introduction
The global drone market is projected to experience robust growth, with Grand View Re-
search estimating the market size at USD 73.06 billion in 2024 and forecasting a compound
annual growth rate (CAGR) of 14.3% from 2025 to 2030, reaching approximately USD
163.6 billion by 2030 [1]. These figures are based on revenue and are reported in nominal
(not inflation-adjusted) terms. The methodology involves forecasting revenue growth at
global, regional, and national levels; analyzing trends across major sectors (e.g., agriculture,
logistics); and considering technological advancements and regulatory developments as
key growth drivers [1]. The geographic scope of these projections is global, with detailed
breakdowns available for regions including North America, Europe, Asia Pacific, Latin
America, and the Middle East and Africa, as well as key countries within these regions.
Despite this rapid growth, the widespread adoption of drones is hindered by a critical
limitation: energy endurance. Traditional battery-powered drones, which rely primarily on
lithium-ion batteries, are constrained by their relatively low energy density, typically offer-
ing flight times of 20 to 40 min depending on the payload and operating conditions [2]. This
limitation not only restricts the operational ranges of drones but also increases the down-
time for recharging, reducing the overall efficiency and increasing the costs. For instance,
in commercial delivery services, frequent battery swaps or recharging can significantly
delay operations, undermining the economic viability of drone-based logistics [3].
Energies 2025, 18, 3101
https://doi.org/10.3390/en18123101

## Page 2

Energies 2025, 18, 3101
2 of 25
To address these challenges, researchers and industry stakeholders have turned to hy-
brid powerplants that combine batteries with alternative energy sources, such as hydrogen
fuel cells. Fuel cells offer energy densities up to five times greater than lithium-ion batteries,
enabling significantly longer flight times [4]. However, fuel cells alone cannot meet the
dynamic power demands of drones during takeoff, maneuvering, or sudden load changes
due to their slower response times. This has led to the development of hybrid systems that
integrate batteries for high-power bursts and fuel cells for sustained energy supply. Such
systems have demonstrated the potential to extend flight times compared to battery-only
configurations [5]. Despite these advancements, the integration of batteries and fuel cells
into a cohesive energy system remains a complex challenge, requiring sophisticated energy
management strategies to optimize the performance, efficiency, and longevity.
Energy management systems (EMS) face inherent design tradeoffs when optimizing
hybrid UAV powerplants, as each strategy struggles to balance adaptability, computational
efficiency, and operational reliability. Rule-based methods [6] prioritize simplicity through
deterministic thresholds (e.g., “activate fuel cell at 40% battery”), but their static decision
boundaries fundamentally limit adaptation to variable flight profiles—a 2023 field study
showed that these systems achieve only 72–84% of the theoretically optimal energy uti-
lization during wind gust recovery maneuvers [7]. In contrast, model predictive control
(MPC) [8] introduces dynamic optimization through receding horizon calculations, yet
it carries a steep computational cost: real-world implementations require 15–30× more
processing power than rule-based systems, often forcing UAVs to accept 200–500 ms control
latencies that degrade trajectory tracking by 12–18% [8]. Machine learning approaches [9]
theoretically transcend these limitations through neural network-based policy optimization,
but their “black box” nature creates critical reliability gaps—a recent comparative analysis
found that deep reinforcement learning controllers exhibit 23% performance variance when
encountering battery degradation patterns that are absent from the training data [9]. This
trilemma underscores a fundamental EMS design challenge: no current strategy simulta-
neously achieves real-time responsiveness, environmental adaptability, and operational
robustness in airborne hybrid systems.
Furthermore, existing studies often overlook the long-term degradation of power
sources, which can significantly impact the performance and lifespans of hybrid UAV sys-
tems. For example, research on proton-exchange membrane fuel cells (PEMFCs) in hybrid
UAVs has demonstrated that exposure to fluctuating ambient conditions and frequent
dynamic power demands can accelerate the membrane degradation rates by 15–30% over
1000 operational hours, leading to a 20–40% reduction in the fuel cell lifespan compared to
steady-state applications [10,11]. Similarly, empirical analyses of lithium polymer (LiPo)
batteries in UAVs have shown a measurable decline in efficiency, with a 2.14% loss in output
power over 100 flight cycles and a 1.16% drop after just 20 cycles, primarily due to repeated
charge–discharge stresses [12]. These degradation effects have tangible operational con-
sequences: UAVs may require 15–25% larger energy reserves to maintain their original
endurance, resulting in an increased takeoff mass, while the need for more frequent fuel
cell membrane replacements raises the maintenance costs [10]. Additionally, as the battery
performance deteriorates, hybrid systems often shift a greater workload to the internal
combustion engines, causing them to operate less efficiently and increasing the overall
fuel consumption by up to 12% over time [13]. These findings underscore the necessity of
degradation-aware energy management in hybrid UAV design and operation [14].
In a comparative analysis of the energy demand between fixed-wing and multirotor
drones, fixed-wing UAVs generally demonstrate superior energy efficiency due to their aero-
dynamic design, which allows for longer endurance with lower power consumption [15].
Fixed-wing drones generate lift through their wings, offering a higher lift-to-drag ratio,

## Page 3

Energies 2025, 18, 3101
3 of 25
which enables longer flight times and a greater payload capacity [16,17]. In contrast, multi-
rotor drones, which rely on continuous rotor activity to generate lift, consume more power
and have shorter flight durations, typically ranging from 15 to 60 min. Innovations in
fixed-wing drone technology, such as lightweight materials and hybrid power systems,
have further enhanced their energy efficiency, making them ideal for long-duration mis-
sions and large-area coverage [18]. While multirotors are better suited for tasks requiring
high maneuverability in confined spaces, fixed-wing drones are increasingly favored for
applications that demand extended operational times and broader coverage.
This study addresses these gaps by proposing a novel adaptive energy management
system for hybrid powerplants in drones, which combines the strengths of batteries and fuel
cells while mitigating their respective limitations. The proposed EMS leverages real-time
data on flight dynamics, environmental conditions, and power source health to optimize
energy allocation, thereby extending the operational endurance of UAVs. The selection
of fuzzy logic over model predictive control (MPC) is based on its simplicity and faster
processing times. Fuzzy logic allows for real-time control without requiring prior data
for operation, making it more suitable for dynamic, on-the-fly adjustments during flight.
In contrast, MPC necessitates knowledge of future values over a prediction horizon to
compute the optimal control strategy, which introduces delays and complexity. By integrat-
ing fuzzy logic control with a comprehensive system design, the approach aims to strike
an optimal balance between performance, efficiency, and cost-effectiveness. Extensive
simulations and experimental testing validate the effectiveness of the EMS, demonstrating
its potential to reduce operational downtime, lower costs, and enhance the sustainability of
drone operations. This work thus provides a significant step forward in the development
of efficient, reliable hybrid power systems for UAVs.
The significance of this research extends beyond technical innovation, offering tangible
benefits for industries reliant on drone technology. For example, in precision agriculture,
longer flight times enable more comprehensive crop monitoring and resource management,
potentially increasing yields by up to 20% [19]. In emergency response scenarios, extended
endurance allows drones to cover larger areas and provide critical support for longer
durations, saving lives and reducing recovery costs [1]. By addressing the energy limitations
of drones, this work contributes to the broader goal of enabling sustainable, efficient,
and scalable UAV technologies. Simulation-based predictions indicate that optimizing
energy consumption strategies can significantly extend drones’ flight times and mission
capabilities, reinforcing the potential impact of this approach on future UAV deployments.
This study addresses several critical gaps in the current literature on hybrid energy
systems for unmanned aerial vehicles. Notably, it bridges the gap between theoretical
models and practical applications by integrating experimental hybrid powerplant sizing,
degradation modeling for both fuel cells and batteries, and the validation of energy manage-
ment strategies within a UAV platform [20,21]. Previous works have identified degradation
mechanisms in fuel cells and batteries, such as voltage degradation and structural damage
to the membrane electrode assembly (MEA) in fuel cells and capacity fade in batteries.
However, these studies often treat degradation in isolation, without integrating these as-
pects into a unified model that accounts for the interplay between different energy sources
and their combined impact on system longevity [22]. Additionally, many studies fail to
incorporate integrated degradation modeling, which is essential in accurately predicting
the long-term performance and lifespans of UAV power systems [23,24]. This work also ad-
dresses the absence of real-time data utilization in energy management strategies, enabling
more adaptive and responsive control systems [25]. Furthermore, the study explores the
development of digital twins, facilitating predictive maintenance and the optimization of
energy management strategies. By addressing these deficiencies, this research contributes

## Page 4

Energies 2025, 18, 3101
4 of 25
to the advancement of more reliable, efficient, and sustainable hybrid energy systems
for UAVs.
2. Materials and Methods
This section describes the hybrid architecture employed, the aircraft studied, the soft-
ware developed for real-time control and simulations, the fuel cell degradation models,
and the energy management strategies developed (fuzzy logic and passive).
2.1. Hybrid Powerplant Architecture
The architecture used in this study is the result of previous research efforts that ex-
plored series and parallel hybrid powerplants, adjusting to the volume, weight, and power
requirements of aircraft [26].
This paper proposes two powerplants optimized in terms of weight and volume:
one designed for the implementation of passive control strategies and another for active
control strategies. The use of passive control strategies reduces the complexity of the
aircraft’s energy management system; however, this significantly decreases the lifespans of
the fuel cell and batteries. Therefore, the use of active control strategies, such as fuzzy logic,
provides excellent solutions to extend the lifespans of batteries and fuel cells [27,28]. Simula-
tion results show that control strategies can increase fuel cell lifetimes by up to 32.8% when
operated under specific degradation states. This improvement is achieved by reducing the
impacts of the operational conditions, such as load changes, stop/start cycles, idle periods,
and high-power operation, which are known to accelerate fuel cell degradation [27].
Figure 1 illustrates the employed architecture, which consists of a data bus accessed
by the onboard computer (Jetson Orin NX). This computer is responsible for maintaining
the databases and energy management algorithms. The CUAV V5+ autopilot ensures
aircraft stability and controls the motors to follow the planned route. The zero-emission
power generation system comprises a battery system that supplies power during flight
segments with high power demands, such as takeoff, landing, or vertical-to-horizontal
flight transitions, while also storing excess power from the fuel cell. The fuel cell serves as
the primary power source, and the battery provides additional power when the fuel cell
alone is insufficient.
Figure 1. The proposed architecture, which enables the combination of a fast response (battery) and
high endurance (fuel cell).
In the architecture designed for passive control strategies, a DC/DC converter is used
in the battery, setting the battery voltage to the minimum voltage of the fuel cell. This
configuration ensures that the fuel cell delivers its full power while the battery supplies

## Page 5

Energies 2025, 18, 3101
5 of 25
the remaining power demand. In Figure 1, the green-colored DC/DC converter represents
this implementation. In contrast, for active control strategies, a programmable converter is
required to limit the power output of the fuel cell. The orange-colored converter in Figure 1
represents this component. This electric motor needs an electronic speed controller (ESC)
to control the speed of the motor with the power supply.
Fuel cells have a slower operational response; incorporating a hybrid system with
batteries enables a faster dynamic response.
2.2. Sizing of Hybrid Power Systems: Battery and Fuel Cell Optimization
An essential aspect of hybrid powerplant design is the optimal sizing of both the
battery and fuel cell subsystems to meet mission-specific power and energy demands.
The battery is primarily sized to supply high instantaneous power during critical flight
phases such as takeoff, hovering, rapid transitions between flight modes, and emergency
maneuvers. These transient conditions dictate the battery’s power rating and required ca-
pacity, ensuring that voltage stability and performance are maintained without overloading
the fuel cell, which is better suited for steady-state power delivery. Batteries are heavy, so
this sizing must be considered carefully.
Energy management control strategies that allow battery recharging enable the use
of smaller-capacity batteries, reducing the weight and increasing the range [29]. Fuel cells
must be selected to cover the power demand during the longest and most efficient flight
segment, which is the cruise segment. Fuel cells with power ratings higher than the cruise
segment allow for the recharging of the battery system.
Figure 2a shows the power contribution demanded by each system during the aircraft’s
flight, while Figure 2b presents an example of a flight profile where battery recharging
occurs during the cruise segment.
(a)
(b)
Figure 2. Key factors influencing the design of hybrid architectures combining fuel cells and batteries.
(a) The sizing process supports the hybridization strategy by providing higher power availability.
(b) Illustration of the strategy used for battery recharging in hybrid architectures.

## Page 6

Energies 2025, 18, 3101
6 of 25
2.3. Application to the Mugin EV-350 Aircraft: Hybridization for Increased Range and Payload
This work focuses on an application in a commercial aircraft with vertical takeoff
capabilities, named the Mugin EV-350 [30]. This aircraft is marketed with a battery system
that adds considerable weight, reducing its payload capacity and flight range. Its detailed
specifications can be found in Table 1. This study includes the hybridization of batteries
and hydrogen to increase the aircraft’s range and payload capacity. Pre-flight tests have
been conducted on a test bench, shown in Figure 3a. The test bench consisted of a support
structure for engine and propeller tests, a fuel cell, a DC/DC converter, a battery, a hydrogen
tank, and a computer for monitoring and control.
(a)
(b)
Figure 3. Experimental systems facilitating the validation of models and control strategies in both
ground and flight test environments. (a) The test bench enables experimental validation before flight
operations. (b) The Mugin EV-350 facilitates experimental validation in flight operations.
Figure 3b shows the electric aircraft used, the Mugin EV-350, with a maximum takeoff
weight (MTOW) of 22 kg.

## Page 7

Energies 2025, 18, 3101
7 of 25
Table 1. Specifications of the selected aircraft. This table presents key physical and performance
characteristics of the Mugin EV-350 aircraft, including the dimensions, propulsion configuration,
and flight performance metrics [30].
Empty weight [kg]
6.7
Wing area [m2]
1
Wingspan [m]
3.5
Fuselage [mm]
1120 × 225 × 206
Propeller configuration
Pusher and VTOL
Propellers
4 × 24′′ and 1 × 21′′
Motor
4 × MS8014 and 1 × AT7215
Cruise speed [m/s]
21
Max speed [m/s]
30
Stall speed [m/s]
15
2.4. Software Development and Wind Tunnel Experiments
For the acquisition of experimental results and the simulation of the systems, a versatile
software program was developed in Python 3.10 [31] to enable the design, implementation,
and validation of control strategies both online and offline using experimental system data.
Figure 4 illustrates the procedure used to simulate the energy management control
strategies. A MATLAB R2023b-based tool [32] was developed to process experimental
data obtained from wind tunnel tests conducted under various flight conditions using
electric motors and propellers [33,34]. These data, combined with the corresponding
flight equations, enabled the generation of a flight power profile that reflected real system
efficiencies. Additionally, experimental data from a 300 W fuel cell were incorporated
to support realistic simulations of the control strategies. All resulting data were stored
in an InfluxDB database [35]. Finally, key performance indicators (KPIs)—including the
cost, degradation, and the remaining useful life (RUL)—were computed to evaluate and
compare the performance of the different EMS implementations. In Figure 4, green boxes
represent the experimental setup, orange boxes correspond to the simulation framework,
and blue indicates the KPI evaluation process.
The flight profile described outlines the different phases of a drone’s operation, each
with specific thrust requirements to simulate a realistic flight scenario. By implementing
the UAV flight dynamics equations in MATLAB and incorporating experimental data
obtained from motor performance tests conducted in a wind tunnel, the expected power
profile during flight is derived. This resulting power profile is presented in Figure 5.
The six segments of the flight profile are described in detail as follows.
1.
Warm-up (30 s at thrust (T) = 0.75 × weight (W)). This initial segment allows the
drone’s systems to stabilize and warm up, ensuring that the components (motors,
sensors, and battery) are properly prepared for the rest of the flight.
The thrust is set to 0.75 times the weight of the drone, which is lower than the drone’s
full weight, to avoid unnecessary wear on the systems. This lower thrust helps to
gradually bring the drone into action without inducing stress on its components.
2.
Takeoff with T = 1.25 W for 10 s. In this phase, the drone needs a significant increase
in thrust to overcome gravity and lift off the ground.
The thrust of 1.25 times the weight ensures that the drone has enough power to
initiate a takeoff, lifting off smoothly while avoiding instability that could arise from
underpowered thrust.
3.
Hovering with T = W for 10 s. Once the drone has taken off, it enters a hovering state,
where it remains stationary in the air.

## Page 8

Energies 2025, 18, 3101
8 of 25
To hover, the thrust is set equal to the weight of the drone. This condition ensures
that the drone is balanced, with the lift force exactly counteracting the force of gravity,
allowing it to remain at a fixed altitude without any upward or downward movement.
4.
Transition from hovering to forward flight for 1 min. The transition phase begins
with the drone hovering and then gradually accelerating to forward flight.
This phase represents the changeover from a vertical flight mode (hovering) to
a horizontal flight mode (forward flight), which requires precise control of the thrust
to maintain stability during the shift in aerodynamic forces.
The gradual transition takes place over one minute to ensure smooth and stable
control during this maneuver, which may involve adjusting both the thrust and the
orientation of the drone.
5.
Cruise for 3 h. During the cruise phase, the drone reaches stable forward flight, where
it maintains a constant speed and altitude.
The cruise phase is the longest and simulates the duration of a flight mission, where
the drone performs tasks such as surveying, monitoring, or delivery.
In this phase, the drone typically operates at an optimal balance of power consumption
and efficiency, sustaining steady flight with minimal energy expenditure.
6.
Landing for 20 s with T = 0.6 W. To conclude the flight, the drone begins its descent.
The thrust during landing is reduced to 0.6 times the weight, which is lower than the
thrust required for takeoff. This is to ensure a gentle, controlled descent, avoiding any
abrupt forces that could harm the drone or its payload.
The 20 s duration of this phase allows the drone to decelerate smoothly and land
safely on the ground.
Figure 4. Methodological flowchart of the simulation process. Experimental data from wind tunnel
tests and fuel cell operation are used in MATLAB-based flight equations and requirements. A power
profile is generated and used in a Python-based simulation to test various energy management
strategies, followed by KPI computation for cost, degradation, and remaining useful life assessment.
Green boxes represent the experimental setup, orange indicates the simulation framework, and blue
denotes KPI evaluation.

## Page 9

Energies 2025, 18, 3101
9 of 25
(a) Simulated power consumption profile of the UAV across the full mission timeline. The figure
highlights the distinct power demands for each flight phase, including warm-up, takeoff, hovering,
transition to forward flight, cruise, and landing. The data reflect varying thrust requirements and
their impacts on the electrical power consumption over time.
(b) Zoomed-in view of the initial phases of flight: warm-up, takeoff, hover, and transition. This
section emphasizes the high initial power spikes and the gradual decline in power as the UAV
transitions from vertical to horizontal flight.
Figure 5. Simulated power consumption profile of a UAV derived from the experimental wind tunnel
data of electric propulsion systems combined with flight dynamics models. The top figure (a) presents
the full mission profile, including all flight segments, while the bottom figure (b) provides a detailed
look at the early mission phases, where the power demand is more dynamic. These profiles are
critical for accurate energy budgeting and mission planning in long-endurance UAV operations.
2.5. Fuel Cell Degradation Model
The fuel cell used in this study is a proton-exchange membrane fuel cell with nominal
power of 300 W. In this study, we use three fuel cells of 300 W. The fuel cell converts

## Page 10

Energies 2025, 18, 3101
10 of 25
hydrogen energy into electrical power (Pf c) through a series of electrochemical reactions.
A fraction of the generated power is consumed by auxiliary systems (air supply, cooling
systems, purging, controllers, etc.) to ensure the proper operation of the overall system.
The auxiliary power consumption is unknown and varies during the fuel cell’s operation.
The minimum power required by these auxiliary systems is estimated at 10 W, based on
the observed consumption when no load draws power.
Figure 6 shows the polarization curve of the fuel cell at an ambient temperature of
25 ◦C, 50% relative humidity, and a hydrogen supply pressure of 0.7 bar. It represents the
cell’s voltage output as a function of current density. This is a crucial tool in evaluating fuel
cell performance under various operating conditions.
Figure 6. Experimentally obtained hydrogen fuel cell polarization curve.
During the operation of the fuel cell, the mass of consumed hydrogen (mH2) can be
calculated as [36]
MH2 =
Z t
0
Pf c(τ)
ηf c(τ)LHVH2
dτ
(1)
where ηf c = Pf c/PH2 is the fuel cell efficiency, PH2 is the theoretical power supplied
by hydrogen, and LHVH2 is the lower heating value of hydrogen (120,000 J/g) [37].
To calculate the mass of consumed hydrogen, it is necessary to quantify PH2 using the
following equation:
PH2 = LHVH2
˙
mH2
(2)
where
˙
mH2 is the hydrogen flow rate, obtained by fitting an experimental linear
equation [38]. Obtained from experimental data provided by the manufacturing company,
the hydrogen consumption for a 300 W power output is
˙
mH2 = 0.3143 g/min [39].
˙
mH2 = a
Pf cncell
v f c
(3)
where a = 6.3 · 10−4, ncell = 40 is the number of cells, and v f c is the fuel cell output voltage.
The reduction in fuel cell efficiency is associated with inefficiencies in heat dissipation,
among other factors. To illustrate the influence of factors that can degrade fuel cell perfor-
mance, data were collected under different environmental conditions, after five months
of fuel cell inactivity, and after normal cell degradation due to operation. The fuel cell
operating range can be divided into three power intervals: low (Pf c ≤Pf cmax/3), medium
(Pf cmax/3 < Pf c ≤2Pf cmax/3), and high (Pf c > 2Pf cmax/3) [36]. These intervals define the

## Page 11

Energies 2025, 18, 3101
11 of 25
medium operating zone as the optimal region for fuel cell operation, where degradation is
reduced and the efficiency per unit of generated electrical power is higher [40].
Developing fuel cell degradation models requires a deep understanding of the degrada-
tion mechanisms, which involve complex processes influenced by multiple electrochemical
and mechanical factors [41]. Other studies indicate that membrane degradation can severely
impact the normal operation of the fuel cell [42]. The primary factors contributing to degra-
dation include the startup and shutdown cycles, power oscillations, and extreme power
outputs (both high and low) [42]. Therefore, the fuel cell lifetime estimation model [40]
is used:
Vd = Nstart−stopv1 + Tlowv2 + Nchangev3 + Te f f iciencyv4 + Thighv5
(4)
RUL = ∆V
Vd
(5)
where Nstart−stop represents the average number of startup and shutdown cycles per hour,
Tlow is the average time operating in the low-power zone per hour, Nchange is the average
number of power transitions per hour, Te f f iciency is the average time operating in the
medium-power zone per hour, and Thigh is the average time operating in the high-power
zone per hour. Vd is the average voltage degradation rate per hour during fuel cell operation.
The coefficients v1, v2, v3, v4, and v5 represent the voltage degradation rates per cycle and
per hour for each operating condition. ∆V is the allowable voltage degradation of a single
fuel cell at the end of its lifespan (typically considered as a 10% decrease from the nominal
voltage [40]), and RUL is the estimated remaining useful life of the fuel cell. For this
study, ∆V = 0.7 V is considered. Table 2 presents the voltage degradation rates used as
reference values.
Table 2. Voltage degradation rates of a single fuel cell under different operating conditions [36,42].
Operating Condition
Voltage Degradation Rate
Startup and Shutdown
v1 = 13.79
µV/cycle
Low Power
v2 = 8.662
µV/h
Power Transitions
v3 = 0.0441
µV/∆kW
Medium Power
v4 = 4.881
µV/h
High Power
v5 = 10
µV/h
2.6. Battery Model
In this study, a six-cell LiPo battery system configured in a 6S1P arrangement is
employed as a supplementary energy source for scenarios in which the instantaneous
power demand exceeds the output capacity of the fuel cell. The battery has a nominal
energy capacity of 729.6 Wh (22.8 V, 32 Ah). In the original powerplant configuration
of the Mugin EV-350, two such battery packs were utilized. Under the proposed hybrid
configuration, only a single battery is required, resulting in a significant reduction in battery
weight without compromising the overall operational performance.
The state of charge (SOC) of the battery is an indicator of the remaining battery capacity
relative to its nominal capacity, expressed as
SOC(t) = SOCini −
Z t
0
ηbatibat(τ)
Cbat
(6)
where Cbat is the nominal capacity of the battery system, SOCini is the initial SOC, and ηbat
is the battery efficiency (typically 1 for discharge and 0.95 for charge).

## Page 12

Energies 2025, 18, 3101
12 of 25
With the use of the battery as an energy supply or absorption system, its capacity
gradually degrades, reaching an irreversible physical state and undergoing electrochemical
changes [43]. To estimate the decrease in the nominal capacity of the battery, a battery
degradation model, developed in [43], is employed. According to the Arrhenius equation,
the percentage decrease in the capacity of battery cells, ∆Qcell(%), relative to their initial
capacity (100%) can be expressed as [44]
∆Qcell = B(crate)exp
−Ea(crate)
RT

(Ah(crate))z
(7)
where crate is the battery c-rate, and B is a coefficient as a function of the c-rate, with values
found in Table 3. Additionally, Ea is the activation energy, R is the ideal gas constant
(8.31 J/(molK)), T is the temperature of the battery cells (considered 298.2 K (25 ◦C)), Ah is
the amount of energy provided by the battery during cycles, and z is a coefficient given by
a law. Based on [44], z = 0.55, and Ea is obtained as
Ea = 31700 −370.3crate(J/molK)
(8)
Table 3. Coefficient B as a function of the c-rate [36].
crate
0.5
2
6
10
B
31.630
21.681
12.934
15.512
For a cell, a 20% reduction in its nominal capacity is considered the end of its life,
and its energy at the end of life (AEoL
h
)
AEoL
h
(crate) =


20
B(crate)exp
 −Ea(crate)
RT



1/z
(9)
On the other hand, the total number of cycles (NEoL) until the end of life can be
obtained as [45]
NEoL(crate) = AEoL
h
(crate)
Qcell
(10)
The state of health (SOH) of the battery is defined as [45]
SOH(t) = 1 −
R t
0 |icell(τ)|dτ
2NEoL(crate)Qcell
(11)
This model allows the prediction of future battery states for predictive control strate-
gies like MPC.
2.7. Fuzzy Logic
Fuzzy logic, based on the principles of fuzzy set theory, allows for the effective han-
dling of imprecision and uncertainty. Unlike conventional control systems, which operate
on binary logic, fuzzy logic works across a continuous spectrum, enabling decision-making
in conditions of ambiguity. This characteristic is particularly useful in controlling vertical
takeoff and landing (VTOL) aircraft, where the flight conditions can vary unpredictably
due to environmental factors, load changes, and other dynamic variables. An overview of
fuzzy logic operation is illustrated in Figure 7.
In the context of aircraft powered by hydrogen fuel cells and batteries, fuzzy logic
is used to manage the distribution of power between the different propulsion systems,
optimizing the performance and prolonging the lifespans of the components.

## Page 13

Energies 2025, 18, 3101
13 of 25
Figure 7. Fuzzy logic operation diagram.
Designing a fuzzy controller for VTOL aircraft involves defining a series of rules
based on experience and system knowledge. These rules, expressed in linguistic terms,
are translated into membership functions that describe the relationship between input
variables (such as battery charge level and power demanded by the motors) and output
variables (such as fuel cell power). The fuzzy inference process converts these inputs into
concrete actions by evaluating the defined rules and combining their results.
Table 4 shows the implemented logical rules. The rules have been designed using
experimental knowledge to prioritize medium- and high-power states of the fuel cell, while
maintaining appropriate charge levels in the battery system. The specification of the rules
of the fuzzy logic controller depends on the designer’s knowledge about the supplies and
motor constraints; intuitive and practical aspects regarding the propulsion mechanism’s
dynamic behavior; and successive experiments to assure the process’s robustness and
reliability [46,47]. Since the flight process can be divided into five stages according to the
required power—takeoff and landing, transition, climbing, cruise, and descent—the input
variable, the demand power (Pd), is classified into five levels: very high (VH), high (H),
medium (M), low (L), and very low (VL) [48]. Similarly, the state of charge (SoC) is classified
into three levels: high (H), medium (M), and low (L). For the output variable of the fuzzy
controller, the fuel cell power (Pf c), its upper limit is determined by the maximum output
power of the fuel cell and the converter efficiency. The maximum output power of the
fuel cell and converter combination in this work is 873 W. The output variable of the fuzzy
controller is classified into five levels: VH, H, M, L, and VL. This results in 15 logical rules.
Table 4. Logical rules for fuzzy control strategy.
Pfc
PD
VH
H
M
L
VL
SoC
L
VH
VH
VH
VH
VH
M
VH
H
H
H
H
H
H
H
M
L
M
Figure 8a,b show the membership functions designed for the input variables to the
fuzzy logic system. Since these were designed using a heuristic approach, further fine-tuning
techniques may be explored. The output variable of the system is the power generated by
the fuel cell, and the membership function for this is shown in Figure 9. For simplification,
the system architecture models the use of three fuel cells as a combined equivalent power
source of 900 W. The computational performance of the developed control framework was
evaluated during operation, yielding a processing time of less than 0.1 ms. Benchmark
testing was conducted on a system equipped with a 13th-Gen Intel® Core™i7-1355U pro-

## Page 14

Energies 2025, 18, 3101
14 of 25
cessor (1.70 GHz) with 16 GB RAM and running Windows 11. The low processing latency
demonstrates the framework’s suitability for real-time embedded applications.
(a)
(b)
Figure 8. Fuzzy logic membership functions used to evaluate the system’s input conditions. Each
graph represents how crisp values are mapped to fuzzy sets for decision-making. (a) Membership
functions for the input variable, i.e., power demand. These define fuzzy linguistic terms such as very
low, low, medium, high, and very high power needs. (b) Membership functions for the input variable,
i.e., battery state of charge. These represent levels like low, medium, and high levels of charge.

## Page 15

Energies 2025, 18, 3101
15 of 25
Figure 9. Fuzzy logic membership functions used to evaluate the system’s output condition. Mem-
bership functions for the input variable, i.e., fuel cell power. These define fuzzy linguistic terms such
as very low, low, medium, high, and very high fuel cell power outputs.
3. Results
Using the battery model described in the previous section and the experimental
data obtained from the fuel cell, simulations are conducted with two control strategies to
evaluate the costs and system degradation after operation. The objective is to quantify
the performance improvement of the aircraft with this new powerplant design, consid-
ering metrics such as autonomy, the payload capacity, costs, and maintenance due to
system degradation.
These results are obtained using three 300 W fuel cells and a 32 Ah battery system,
replacing the original powerplant of the Mugin EV-350, which consisted of two 32 Ah
batteries each. The simulation uses experimental data from the 300W fuel cell.
The initial conditions of the energy generation system are indicated in Table 5, where
hydrogen is stored at pressure of 300 bar and 20 ◦C in a 5 L tank.
Table 5. Initial conditions of the energy generation system. The table shows the initial simulation
values for LOH, mh2, SOH, and SOC, assuming full capacity at the start of the mission. These
conditions reflect the energy availability for the evaluation of the hybrid powerplant’s performance.
LOH (%)
mh2 (g)
SOH (%)
SOC (%)
100
104
100
100
3.1. Energy Contribution Analysis
The power profiles of aircraft with vertical takeoff capabilities require high power
during takeoff. In hybrid powerplants, most of this power is supplied by the batteries.
The compared control strategies differ in the degree of power contribution from the fuel cell
during these phases. It is desirable for fuel cells to operate without abrupt power variations
and at moderate power levels, where they are more efficient and have an extended lifespan.
Figure 10 shows the power supplied under different control strategies, while Figure 11 pro-

## Page 16

Energies 2025, 18, 3101
16 of 25
vides a detailed view of the initial flight phase, highlighting the dynamic power demands
during warm-up, takeoff, and early transition.
Figure 10. Comparison of power supplied under different control strategies. In the passive control
strategy, the fuel cell serves as the primary power source. In contrast, under fuzzy logic control,
the fuel cell output is regulated according to predefined logic rules, limiting its power contribution.
Figure 11. Detailed view of the initial flight phase under both control strategies, including warm-
up, takeoff, and early transition. This portion of the mission is characterized by rapidly changing
power demands.
Figure 12 illustrates the variations in the battery and hydrogen energy levels. These
variations directly reflect the power usage of each system according to the control strategy
employed. In Figure 12b, it can be observed that the passive control strategy makes the
highest use of the fuel cell, significantly depleting the hydrogen levels more rapidly than
the fuzzy logic strategy with different battery usage, as shown in Figure 12a.

## Page 17

Energies 2025, 18, 3101
17 of 25
(a)
(b)
Figure 12. Evolution of energy storage levels for the battery and hydrogen tank under different
control strategies. These trends reflect how each energy source is managed during system operation.
(a) Battery state of charge over time under different control strategies. (b) Level of hydrogen over
time under different control strategies.
3.2. Operational Cost Analysis
The minimization of costs is the primary objective of this comparative study on
control strategies. Maintaining low operational costs ensures that drones remain a viable
and competitive solution compared to other alternatives. Figures 13–16 present the total
operational costs and the costs per component.
The operational costs of the battery (Figure 13) are negligible compared to the costs
of the fuel cell (Figure 15) and hydrogen consumption (Figure 16). Figure 14 shows that
the fuzzy logic strategy achieves the lowest operational costs. These costs are primarily
associated with hydrogen consumption, which represents the highest expense.

## Page 18

Energies 2025, 18, 3101
18 of 25
Figure 13. Battery-related costs, including charging cycles and degradation.
Figure 14. Total operational cost over the mission or system duration for different control strategies.
Figure 15. Fuel cell-related costs, including fuel cell degradation factors.

## Page 19

Energies 2025, 18, 3101
19 of 25
Figure 16. Hydrogen consumption cost throughout the operation period.
Figure 17a shows that the battery’s state of health remains unchanged during opera-
tion, since it is an indicator with a slow dynamic response. On the other hand, Figure 17b
presents the evolution of the accumulated hydrogen consumption, which is directly re-
lated to the hydrogen operating cost (Figure 16). All control strategies fully deplete the
available hydrogen.
Another important indicator is the voltage degradation of the fuel cell’s individual
cells, which is caused by inefficiencies in heat dissipation and the operational stress in-
duced by large power variations. This result is presented in Figure 18, where the highest
degradation is observed in the fuzzy logic strategy due to significant power increases and
variations during operation.
Notably, the passive control strategy results in the lowest accumulated fuel cell degra-
dation over time. Although it initially experiences the highest rate of degradation—since
the fuel cell supplies the full power demand from the outset—it subsequently operates at
a steady maximum power level, minimizing dynamic stress and limiting further degrada-
tion. This is reflected in the constant slope observed in the degradation curve. In contrast,
the fuzzy logic strategy exhibits the highest accumulated degradation, primarily due to
frequent and abrupt variations in the fuel cell’s power output. These fluctuations impose
dynamic loading conditions that accelerate the degradation mechanisms.
Finally, it is observed that shutting down the fuel cell due to hydrogen depletion
causes a sharp increase in degradation due to the abrupt power variation (see the final
section of the curve in the graph). Future control strategies should incorporate a gradual
reduction in power during the shutdown phase to mitigate this effect.
As shown in Table 6, implementing a controlled shutdown strategy can significantly
improve the operational lifetime of the fuel cell. In particular, the absolute reference
method with a 50% slope yields the highest estimated remaining useful life, achieving
an improvement of up to 13.54% compared to operation without any shutdown strategy.
The estimated remaining useful life varies depending on the shutdown strategy and the
slope reference used to reduce the fuel cell power output. These results highlight the
importance of selecting an appropriate balance between the shutdown duration and the
magnitude of power decrements. Longer shutdown times, associated with smaller power
reductions, increase the total operating time and lead to higher accumulated degradation.
In contrast, shorter shutdowns with larger power decrements reduce the exposure time
but introduce greater power fluctuations, accelerating degradation due to transient stress.

## Page 20

Energies 2025, 18, 3101
20 of 25
Therefore, a sensitivity analysis is necessary to determine the optimal shutdown profile
that minimizes fuel cell degradation while maintaining operational efficiency.
(a)
(b)
Figure 17. Key performance indicators for the evaluation of control strategies: battery degradation
and hydrogen usage. These metrics highlight the tradeoffs between system longevity and energy
resource consumption. (a) Battery state of health degradation over time under different control
strategies. (b) Total hydrogen consumption during system operation for each control strategy.
Table 6. Remaining useful life represents the estimated operational time remaining for the fuel cell,
expressed in hours. It is used to assess system degradation and support predictive maintenance.
Two methods are used to reduce the fuel cell’s power output during the shutdown phase. In the
absolute method, the power decrement is defined as a fixed percentage of the fuel cell’s output at the
start of the shutdown. In the relative method, the power decrement is calculated as a percentage of
the most recent power output and is updated at each time step, allowing dynamic adaptation to the
operating conditions.
Reference of Slope
1%
5%
10%
30%
50%
100%
Absolute
5626.56 h
5675.83 h
5748.07 h
5833.33 h
6390.36 h
5628.37 h
Relative
5585.70 h
5620.23 h
5624.30 h
5634.26 h
5628.82 h
-

## Page 21

Energies 2025, 18, 3101
21 of 25
Figure 18. Fuel cell degradation.
4. Discussion
The results of this study demonstrate clear improvements in reducing the operational
costs and extending the aircraft’s endurance, achieving an increase in flight autonomy of
50% compared to conventional configurations. This enhancement is particularly signif-
icant for missions requiring extended loitering or range, such as surveillance, mapping,
or delivery in remote areas. While previous research has investigated hybridization in
quadcopters—aircraft that benefit from lower power requirements during takeoff due to
their lightweight nature and vertical lift mechanisms—this work advances the field by
adapting hybrid energy management to fixed-wing UAVs with horizontal flight capabilities.
Fixed-wing platforms are inherently more efficient in cruise flight, offering better energy
utilization, and thus present greater potential for endurance optimization when equipped
with intelligent energy control strategies.
During the development and testing phases, several areas for system enhancement
were identified, particularly related to the fuel cell shutdown process. Experimental
results demonstrated that implementing a controlled and gradual reduction in power
output during shutdown helped to mitigate abrupt transients, thereby improving the
system’s stability and extending the fuel cell’s longevity. Specifically, as shown in Table 6,
the application of a shutdown strategy using an absolute reference with a 50% slope
yielded an improvement of up to 13.54% in the estimated remaining useful life compared
to operation without a shutdown mechanism. Additionally, the study emphasizes the
operational benefits of maintaining a near-constant power output from the fuel cell, which
reduces power fluctuations and associated degradation. These findings also highlight the
importance of appropriate fuel cell sizing; systems in which the fuel cell’s rated power
falls below the aircraft’s steady-state cruise demand were found to restrict the effectiveness
of intelligent energy management strategies, leading to suboptimal performance and
accelerated wear.
Building upon these findings, future studies should focus on the implementation of
control strategies inspired by passive hybrid systems, wherein the fuel cell operates at
a constant baseline power output for most of the mission, supplemented by the battery
during transients or periods of increased demand. In this context, small and gradual ad-
justments to the fuel cell power output may be introduced to enhance the overall efficiency
while preserving the system’s simplicity and reliability.

## Page 22

Energies 2025, 18, 3101
22 of 25
Another critical area for future research involves optimizing fuzzy logic-based energy
management strategies. Efforts should focus on developing methods for both the offline
and online tuning of fuzzy logic rules, potentially using optimization algorithms or machine
learning techniques. These approaches could allow for adaptation based on mission profiles,
performance objectives, or changing environmental conditions. Furthermore, exploring
ways to improve the fuzzy control system through the use of confidence intervals and
sensitivity analysis could provide deeper insights into its performance, enhancing the
gains in endurance and reducing the costs. In addition, implementing techniques to
manage the power slope variation of the fuel cell, such as model predictive control or
reinforcement learning, could offer more precise control, improving the overall system
efficiency and resilience. Adaptive fuzzy logic systems could learn from past flights and
continuously refine their rules, providing a dynamic and data-driven approach to UAV
energy management.
Moreover, it would be valuable to explore power management strategies that incorpo-
rate predefined constraints on the fuel cell power increase rates to limit rapid transitions
and reduce thermal and mechanical stresses. Incorporating flight mission planning into
the control algorithm—where the expected power demand is known in advance—could
further improve the energy distribution and prolong the system’s life.
To validate the real-world applicability of these strategies, full-scale experimental flight
tests should be conducted, involving complete UAV missions under a range of operational
conditions. These tests would enable the assessment of the control performance under
realistic aerodynamic loads, sensor noise, and external disturbances. Additionally, future
work should focus on improving the fuel cell degradation model through experimental
testing under different operational conditions, including temperature, pressure, and hu-
midity variations, as well as fluctuations in these parameters, to provide more accurate
insights into fuel cell performance and longevity. Experimental validation of the battery
degradation model, particularly under higher current loads typical in UAV operations,
should also be prioritized to enhance model accuracy. Furthermore, the integration of
digital twins—using real-time data for system simulation and prediction—could support
the development of more precise models. Future work should also explore the integration
of environmental adaptability into the control system, enabling the UAV to dynamically
respond to varying wind conditions, ambient temperature fluctuations, and altitude-related
performance shifts.
In addition, future work should address the co-optimization of the hybrid energy
system design, which includes the sizing and selection of fuel cells, batteries, and hydrogen
storage, alongside the development of control strategies. A system-level design framework
that jointly considers factors such as the energy capacity, weight, mission requirements,
and control performance would enable the creation of more efficient, customized UAV
configurations. Furthermore, improvements to the current framework will enhance the
operation of energy management strategies by allowing the use of real-time data for
both simulation purposes and real-world applications. Future versions of the framework
should focus on improving the digital twins, enabling the implementation of more efficient
energy management strategies. These advancements would provide better predictions of
system behavior, optimize the energy consumption, and ultimately enhance the UAV’s
operational efficiency.
Lastly, the inclusion of fault detection and recovery mechanisms in the energy man-
agement architecture is essential in enhancing its reliability and ensuring safety during
autonomous missions. Such features could allow the system’s performance to degrade
gradually in the event of a component failure, maintaining safe operation until recovery or
landing is possible.

## Page 23

Energies 2025, 18, 3101
23 of 25
Author Contributions: Conceptualization, S.E., C.B. and J.A.Q.; Data curation, J.A.Q.; Funding
acquisition, C.B., S.E. and J.D.; Investigation, J.A.Q.; Methodology, J.A.Q.; Project administration,
C.B. and S.E.; Resources, C.B. and S.E.; Software, J.A.Q.; Supervision, C.B. and S.E.; Validation,
J.A.Q.; Visualization, J.A.Q.; Writing—original draft, J.A.Q. All authors have read and agreed to the
published version of the manuscript.
Funding: This research was funded by ‘MCIN/AEI/10.13039/501100011033/FEDER’, EU project
name PID2022-142069OB-I00; by ‘Consejería de Transformación Económica, Industria, Conocimiento
y Universidades de la Junta de Andalucía’, project name ‘QUAL21 006 USE’; and by ZELENZA
and CDTI in the context of the project ‘PLATAFORMA SENSE AVOID INTEROPERABLE DE UAS
BAJO MODELOS GEOESPACIALES DE IA, REALIDAD EXTENDIDA Y COMUNICA CIONES 5G
CIBERSEGURAS EN EL U-SPACE U5-SPACE’, funded by the European Union within the Intelligent
Management for Drones in U-Space Call. Project supported by the Ministry of Science, Innovation,
and Universities of Spain.
Data Availability Statement: The raw data supporting the conclusions of this article will be made
available by the authors on request.
Conflicts of Interest: Author Julian Delgado was employed by the Zelenza S.L. The remaining authors
declare that the research was conducted in the absence of any commercial or financial relationships
that could be construed as a potential conflict of interest. The authors declare that this study received
part funding from ZELENZA and CDTI. The funder was not involved in the study design, collection,
analysis, interpretation of data, the writing of this article or the decision to submit it for publication.
Abbreviations
The following abbreviations are used in this manuscript:
UAV
Unmanned Aerial Vehicle
EMS
Energy Management System
MPC
Model Predictive Control
MTOW
Maximum Takeoff Weight
PEMFC
Proton-Exchange Membrane Fuel Cell
LHV
Low Heating Value
RUL
Remaining Useful Life
SOC
State of Charge
VTOL
Vertical Takeoff and Landing
ESC
Electronic Speed Controller
References
1.
Research, G.V. Drone Market Size, Share & Trends Analysis Report by component (Hardware, software, services), by product, by
technology, by payload capacity, by power source, by end use, by region, and segment Forecasts, 2025–2030. In Market Analysis
Report; Grand View Research: San Francisco, CA, USA, 2025.
2.
Telli, K.; Kraa, O.; Himeur, Y.; Ouamane, A.; Boumehraz, M.; Atalla, S.; Mansoor, W. A comprehensive review of recent research
trends on unmanned aerial vehicles (uavs). Systems 2023, 11, 400. [CrossRef]
3.
Aurambout, J.P.; Gkoumas, K.; Ciuffo, B. Last mile delivery by drones: An estimation of viable market potential and access to
citizens across European cities. Eur. Transp. Res. Rev. 2019, 11, 30. [CrossRef]
4.
Gong, A.; Verstraete, D. Fuel cell propulsion in small fixed-wing unmanned aerial vehicles: Current status and research needs.
Int. J. Hydrogen Energy 2017, 42, 21311–21333. [CrossRef]
5.
Swarnkar, A.; Maherchandani, J.K. Performance analysis of hybrid fuel cell/battery/supercapacitor electric vehicle for different
battery state of charge levels. In Proceedings of the 2018 International Conference on Recent Innovations in Electrical, Electronics
& Communication Engineering (ICRIEECE), Bhubaneswar, India, 27–28 July 2018; pp. 2306–2311. [CrossRef]
6.
Xu, L.; Huangfu, Y.; Ma, R.; Xie, R.; Song, Z.; Zhao, D.; Yang, Y.; Wang, Y.; Xu, L. A comprehensive review on fuel cell UAV key
technologies: Propulsion system, management strategy, and design procedure. IEEE Trans. Transp. Electrif. 2022, 8, 4118–4139.
[CrossRef]
7.
Zhang, H.; Yue, D.; Xie, X. Distributed model predictive control for hybrid energy resource system with large-scale decomposition
coordination approach. IEEE Access 2016, 4, 9332–9344. [CrossRef]

## Page 24

Energies 2025, 18, 3101
24 of 25
8.
Singh, A.R.; Kumar, R.S.; Bajaj, M.; Khadse, C.B.; Zaitsev, I. Machine learning-based energy management and power forecasting
in grid-connected microgrids with multiple distributed energy sources. Sci. Rep. 2024, 14, 19207. [CrossRef]
9.
Renau, J.; Tejada, D.; García, V.; López, E.; Domenech, L.; Lozano, A.; Barreras, F. Design, development, integration and evaluation
of hybrid fuel cell power systems for an unmanned water surface vehicle. Int. J. Hydrogen Energy 2024, 54, 1273–1285. [CrossRef]
10.
Donateo, T. Simulation Approaches and Validation Issues for Open-Cathode Fuel Cell Systems in Manned and Unmanned Aerial
Vehicles. Energies 2024, 17, 900. [CrossRef]
11.
Borup, R.; Meyers, J.; Pivovar, B.; Kim, Y.S.; Mukundan, R.; Garland, N.; Myers, D.; Wilson, M.; Garzon, F.; Wood, D.; et al. Scientific
aspects of polymer electrolyte fuel cell durability and degradation. Chem. Rev. 2007, 107, 3904–3951. [CrossRef]
12.
Eleftheroglou, N.; Mansouri, S.S.; Loutas, T.; Karvelis, P.; Georgoulas, G.; Nikolakopoulos, G.; Zarouchas, D. Intelligent
data-driven prognostic methodologies for the real-time remaining useful life until the end-of-discharge estimation of the Lithium-
Polymer batteries of unmanned aerial vehicles with uncertainty quantification. Appl. Energy 2019, 254, 113677. [CrossRef]
13.
Saravanakumar, Y.N.; Sultan, M.T.H.; Shahar, F.S.; Giernacki, W.; Łukaszewicz, A.; Nowakowski, M.; Holovatyy, A.; St˛epie´n, S.
Power sources for unmanned aerial vehicles: A state-of-the art. Appl. Sci. 2023, 13, 11932. [CrossRef]
14.
Nhamo, L.; Magidi, J.; Nyamugama, A.; Clulow, A.D.; Sibanda, M.; Chimonyo, V.G.; Mabhaudhi, T. Prospects of improving
agricultural and water productivity through unmanned aerial vehicles. Agriculture 2020, 10, 256. [CrossRef]
15.
Hassanalian, M.; Abdelkefi, A. Classifications, applications, and design challenges of drones: A review. Prog. Aerosp. Sci. 2017,
91, 99–131. [CrossRef]
16.
Zhang, C.; Kovacs, J.M. The application of small unmanned aerial systems for precision agriculture: A review. Precis. Agric. 2012,
13, 693–712. [CrossRef]
17.
Gong, H.; Huang, B.; Jia, B.; Dai, H. Modeling power consumptions for multirotor UAVs. IEEE Trans. Aerosp. Electron. Syst. 2023,
59, 7409–7422. [CrossRef]
18.
Colomina, I.; Molina, P. Unmanned aerial systems for photogrammetry and remote sensing: A review. ISPRS J. Photogramm.
Remote Sens. 2014, 92, 79–97. [CrossRef]
19.
Daud, S.M.S.M.; Yusof, M.Y.P.M.; Heo, C.C.; Khoo, L.S.; Singh, M.K.C.; Mahmood, M.S.; Nawawi, H. Applications of drone in
disaster management: A scoping review. Sci. Justice 2022, 62, 30–42. [CrossRef]
20.
Cardone, M.; Gargiulo, B.; Fornaro, E. Modelling and experimental validation of a hybrid electric propulsion system for light
aircraft and unmanned aerial vehicles. Energies 2021, 14, 3969. [CrossRef]
21.
Aslam, Z.; Felix, A.; Kalyvas, C.; Chizari, M. Design of a fuel cell/battery hybrid power system for a micro vehicle: Sizing design
and hydrogen storage evaluation. Vehicles 2023, 5, 1570–1585. [CrossRef]
22.
Choi, J.; Park, H.J.; Han, J. Development of Hydrogen Fuel Cell–Battery Hybrid Multicopter System Thermal Management and
Power Management System Based on AMESim. Energies 2025, 18, 447. [CrossRef]
23.
Lei, T.; Wang, Y.; Jin, X.; Min, Z.; Zhang, X.; Zhang, X. An optimal fuzzy logic-based energy management strategy for a fuel
cell/battery hybrid power unmanned aerial vehicle. Aerospace 2022, 9, 115. [CrossRef]
24.
Boukoberine, M.N.; Zia, M.F.; Benbouzid, M.; Zhou, Z.; Donateo, T. Hybrid fuel cell powered drones energy management strategy
improvement and hydrogen saving using real flight test data. Energy Convers. Manag. 2021, 236, 113987. [CrossRef]
25.
Yang, C.; Moon, S.; Kim, Y. A fuel cell/battery hybrid power system for an unmanned aerial vehicle. J. Mech. Sci. Technol. 2016,
30, 2379–2385. [CrossRef]
26.
Quintana, J.A.; Bordons, C.; Esteban, S. Energy Management System for a Hybrid Fuel Cell Unmanned Aerial Vehicle: Sistema de
gestión de energía para aeronaves híbridas con pila de combustible. Jorn. Autom. 2024, 45.
27.
Luca, R.; Whiteley, M.; Neville, T.; Shearing, P.R.; Brett, D.J. Comparative study of energy management systems for a hybrid
fuel cell electric vehicle-A novel mutative fuzzy logic controller to prolong fuel cell lifetime.
Int. J. Hydrogen Energy 2022,
47, 24042–24058. [CrossRef]
28.
Mazouzi, A.; Hadroug, N.; Alayed, W.; Hafaifa, A.; Iratni, A.; Kouzou, A. Comprehensive optimization of fuzzy logic-based
energy management system for fuel-cell hybrid electric vehicle using genetic algorithm. Int. J. Hydrogen Energy 2024, 81, 889–905.
[CrossRef]
29.
de Frutos, V.M.; Parra, J.R.; Esteban, S.; Bordons, C. Analysis of hybrization for the use of hydrogen for aircraft propulsion in an
existing platform. In Proceedings of the AIAA AVIATION 2023 Forum, San Diego, CA, USA, 12–16 June 2023; p. 3876. [CrossRef]
30.
Mugin. Mugin EV-350. Available online: https://www.muginuav.com/es/product/mugin-ev350-carbon-fiber-full-electric-vtol-
uav-platform/ (accessed on 28 April 2025).
31.
Python. Available online: https://www.python.org/ (accessed on 28 April 2025).
32.
MATLAB. Available online: https://www.mathworks.com/products/matlab.html (accessed on 28 April 2025).
33.
Ortega, F.; Esteban, S.; Núñez, M. Aerodynamics and Propulsive Modeling of a Bi-Rotor Convertible Aircraft for the Identification
of Trim Conditions in Longitudinal Flight. In Proceedings of the Vertical Flight Society’s 77th Annual Forum & Technology
Display, Online, 10–14 May 2021. [CrossRef]

## Page 25

Energies 2025, 18, 3101
25 of 25
34.
Martínez, Á.; Franco, A.; Esteban, S. Single-Segment Analysis for the Performance Optimization of a Tilt-Rotor All-Electric
RPAS. ProVANT-EMERGENTIa Project. In Proceedings of the Climbing and Walking Robots Conference; Springer: Berlin/Heidelberg,
Germany, 2023; pp. 129–140. [CrossRef]
35.
Influxdb. Available online: https://www.influxdata.com/ (accessed on 28 April 2025).
36.
Zhou, Y.; Ravey, A.; Péra, M.C. Real-time cost-minimization power-allocating strategy via model predictive control for fuel cell
hybrid electric vehicles. Energy Convers. Manag. 2021, 229, 113721. [CrossRef]
37.
LHV Hydrogen. Available online: https://www.engineeringtoolbox.com/fuels-higher-calorific-values-d_169.html (accessed on
9 August 2024).
38.
Herwerth, C.; Chiang, C.; Ko, A.; Matsuyama, S.; Choi, S.B.; Mirmirani, M.; Gamble, D.; Paul, R.; Sanchez, V.; Arena, A.;
et al. Development of a Small Long Endurance Hybrid PEM Fuel Cell Powered UAV; Technical report, SAE Technical Paper; SAE
International: Warrendale, PA, USA, 2007. [CrossRef]
39.
Spectronik | Hydrogen Fuel Cells. Available online: https://www.spectronik.com (accessed on 28 April 2025).
40.
Chen, H.; Pei, P.; Song, M. Lifetime prediction and the economic lifetime of proton exchange membrane fuel cells. Appl. Energy
2015, 142, 154–163. [CrossRef]
41.
Yuan, X.Z.; Li, H.; Zhang, S.; Martin, J.; Wang, H. A review of polymer electrolyte membrane fuel cell durability test protocols.
J. Power Sources 2011, 196, 9107–9116. [CrossRef]
42.
Fletcher, T.; Thring, R.; Watkinson, M. An Energy Management Strategy to concurrently optimise fuel consumption & PEM fuel
cell lifetime in a hybrid vehicle. Int. J. Hydrogen Energy 2016, 41, 21503–21515. [CrossRef]
43.
Bloom, I.; Cole, B.; Sohn, J.; Jones, S.A.; Polzin, E.G.; Battaglia, V.S.; Henriksen, G.L.; Motloch, C.; Richardson, R.; Unkelhaeuser, T.;
et al. An accelerated calendar and cycle life study of Li-ion cells. J. Power Sour. 2001, 101, 238–247. [CrossRef]
44.
Wang, J.; Liu, P.; Hicks-Garner, J.; Sherman, E.; Soukiazian, S.; Verbrugge, M.; Tataria, H.; Musser, J.; Finamore, P. Cycle-life model
for graphite-LiFePO4 cells. J. Power Sour. 2011, 196, 3942–3948. [CrossRef]
45.
Ebbesen, S.; Elbert, P.; Guzzella, L. Battery state-of-health perceptive energy management for hybrid electric vehicles. IEEE Trans.
Veh. Technol. 2012, 61, 2893–2900. [CrossRef]
46.
Gao, D.; Jin, Z.; Lu, Q. Energy management strategy based on fuzzy logic for a fuel cell hybrid bus.
J. Power Sour. 2008,
185, 311–317. [CrossRef]
47.
Lee, C.C. Fuzzy logic in control systems: Fuzzy logic controller. I. IEEE Trans. Syst. Man Cybern. 1990, 20, 404–418. [CrossRef]
48.
Zhu, Y.; Zhu, B.; Yang, X.; Hou, Z.; Zong, J. Fuzzy logic-based energy management strategy of hybrid electric propulsion system
for fixed-wing VTOL aircraft. Aerospace 2022, 9, 547. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
