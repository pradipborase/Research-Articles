# An Intelligent Energy Management System for Enhanced Performance in Electric UAVs,.pdf

## Page 1

Aerospace Systems (2025) 8:701–716
https://doi.org/10.1007/s42401-025-00343-3
ORIGINAL PAPER
An intelligent energy management system for enhanced performance
in electric UAVs
Mohamed S. Elkerdany1 · Ibrahim M. Safwat1 · Ahmed Medhat M. Youssef2 · Mohamed M. Elkhatib3
Received: 8 October 2024 / Revised: 7 December 2024 / Accepted: 3 January 2025 / Published online: 26 January 2025
© Shanghai Jiao Tong University 2025
Abstract
Unmanned aerial vehicles (UAVs) propelled by electricity have emerged as a prominent concept in aviation due to their
eco-friendly and stealth characteristics. To address the limitations of Polymer Membrane Fuel Cell (PMFC), which serve
as the primary power source but exhibit sluggish responses to sudden load changes, this research proposes a novel hybrid
power system incorporating a Li-Ion battery. This hybrid setup ensures superior dynamic response while maintaining high
power-to-weight efﬁciency. This paper presents an intelligent energy management system (EMS), which effectively regulates
power ﬂow between the PMFC and Li-Ion battery through a multi-input multi-output (MIMO) control framework. The
uniqueness of this study lies in the comparative evaluation of two advanced EMS control strategies: Fuzzy Logic Control
and the Adaptive Neuro-Fuzzy Inference System (ANFIS), under multiple ﬂight modes. By thoroughly analyzing system
transients and dynamic behaviors using MATLAB/SIMULINK, this work provides a detailed insight into optimizing UAV
power efﬁciency. Unlike previous studies, this research highlights the distinct advantages and limitations of each control
strategy for different ﬂight phases, providing a comprehensive benchmark for future EMS designs in UAV applications.
Keywords Energy management system · Fuzzy logic control · BLDC motors control · Intelligent control · Hybrid power
systems · Power electronic converters
1 Introduction
1.1 Technical aspects
Large UAVs typically employ internal combustion engines
(ICEs) as their main source of propulsion due to the high
energy density of gasoline. However, the range of these UAVs
is inherently limited by the quantity of fuel they can carry;
B Mohamed S. Elkerdany
mohamed_elkerdany@ieee.org; m.sameh93@mtc.edu.eg
Ibrahim M. Safwat
Khalilos81@yahoo.com
Ahmed Medhat M. Youssef
ammyk.khater@yahoo.com
Mohamed M. Elkhatib
mohamed.m.elkhatib@ieee.org;
mohamed.elkhatib@mtc.edu.om
1
Military Technical College, Kobry Elkobbah, Cairo, Egypt
2
The High Institute for Engineering and Technology, K21
Cairo/Belbeis Rd., Al-Obour, Egypt
3
Military Technological College, Muscat, Oman
increasing the amount of fuel also adds to the overall weight,
reducing efﬁciency and performance [1]. In contrast, elec-
tric motors are smaller and lighter, making them a more
favorable choice for smaller UAV applications [2]. For UAV
propulsion, energy sources must have high power and energy
density, in addition to a quick dynamic response. Multiple
types of DC electric energy sources have been utilized, with
various studies examining their strengths and weaknesses to
determine the most effective option [3].
The motivation for this research lies in improving the
power supply system for UAVs to boost their capability.
Enhancements in this area have notably increased the UAV’s
endurance, extending ﬂight duration from 1.22h using only
a battery to 3h when employing a hybrid system of fuel
cells and batteries [4]. Solar energy, though considered as
a DC energy source, is insufﬁcient for small reconnais-
sance UAVs because it requires a large wingspan, and its
reliance on sunlight limits its operational time to daylight
hours only. Super-capacitors offer beneﬁts like a long opera-
tionallifespanandminimalmaintenance,buttheirlimitations
include high weight, large size, low energy density, rapid
self-discharge, and high startup costs. Therefore, batteries
123

## Page 2

702
Aerospace Systems (2025) 8:701–716
are widely used due to their high power density, ability to
respond quickly to changes in load, and almost zero emis-
sions. Nevertheless, batteries also face constraints, such as
low energy density and long charging times [5].
Hydrogen fuel cells are attractive for UAV propulsion
because they provide high power and energy densities,
long service lives, and produce low emissions, noise, and
heat. However, their disadvantages include slow dynamic
response, sensitivity to sudden load changes, and the need for
a prolonged warm-up period to reach nominal power output.
Based on earlier research, this paper proposes energy man-
agement strategies that integrate both batteries and fuel cells
to maximize the advantages and minimize the drawbacks
of these energy sources [6]. This strategy allows the Energy
Management System (EMS) to control essential performance
variables like current and voltage, thereby optimizing power
management [7]. In this work, an EMS interfaced with a
regulated system is designed and developed, employing two
distinct control approaches.
1.2 Ethical considerations of using hydrogen fuel
cells in UAVs
Beyond the technological aspects, it is crucial to consider
the ethical implications of using hydrogen fuel cells in UAV
operations. Hydrogen fuel cells are often perceived as an
environmentally friendly power source because they do not
emit carbon during use, signiﬁcantly lowering their eco-
logical impact compared to traditional internal combustion
engines. However, the production of hydrogen, particularly
when derived from non-renewable sources, can negatively
affect the environment. For instance, hydrogen extraction
methods like steam methane reforming can contribute to
increased greenhouse gas emissions if not conducted respon-
sibly.
Furthermore, the storage and transportation of hydrogen
involve signiﬁcant risks due to high-pressure storage require-
ments and the energy demands associated with maintaining
those conditions. Despite these challenges, recent advance-
ments in green hydrogen production, such as electrolysis
powered by renewable energy sources, provide a promising
direction for minimizing environmental harm.
1.3 Energy management technology for UAVs
UAVs using energy management technologies provide sev-
eral beneﬁts, including improved performance, dependabil-
ity, and efﬁciency. Power distribution to propulsion, avionics,
and payload systems is made efﬁcient by EMS. Reducing
power losses prolongs battery life, enabling UAVs to function
for extended periods of time without needing to be recharged
or refueled. makes sure the UAV uses energy as efﬁciently
as possible by adjusting energy usage based on real-time
power demands. Certain UAVs can improve total energy
utilization by capturing and reusing energy (for example,
during descent or deceleration). Ensure smooth operation by
effectively managing a variety of energy sources, including
solar panels, fuel cells, and batteries. Prioritize and alternate
energy sources automatically according to efﬁciency, load
demands, and availability.
In order to avoid over-discharge or overheating, which
could result in system failures, EMS can monitor bat-
tery degradation, temperature, and charge levels. smartly
distributes reserve energy to guarantee that electricity is
available for vital systems in an emergency. UAVs’ mission
capabilities can be enhanced by optimizing energy consump-
tion so they can save power for more payloads, such as
more advanced sensors, cameras, or cargo. optimizes per-
formance under various operational situations by modifying
power allocation to meet certain mission requirements, such
as delivery, mapping, or surveillance. ensures efﬁcient use of
energybyautomaticallyadjustingtochangesinﬂightdynam-
ics (such as strong winds or a heavy load). UAVs stay relevant
as technology advances thanks to energy management sys-
tems, which make it possible to integrate new technologies
like more effective propulsion systems, sophisticated sen-
sors, and AI-powered energy optimization algorithms.
This research outlines the development of the hybrid
Energy Management System (EMS), which integrates the
EMS concept with the design and control of energy source
converters to establish a cohesive control scheme. Section (2)
outlines the methodology of the contents of the work. Sec-
tion (3) details the power requirements for UAV propulsion
across various ﬂight modes. In Sect. (4), the focus is on the
design aspects of both interleaved and bidirectional convert-
ers. Section (5) discusses the characteristics and outcomes
of the proposed EMS. Results and discussion of the of the
proposed system is explained in Sect. (6). Finally, Sect. (7)
provides a summary of the entire study and its conclusions.
2 Methodology
This research looks into energy management techniques for a
hybrid electric UAV powered by a fuel cell and a lithium-ion
battery system, with a BLDC motor as the propulsion mech-
anism. The major goal is to improve the UAV’s endurance
through effective energy management. The suggested sys-
tem incorporates advanced power converters and two energy
management strategies: fuzzy logic control and an adaptive
neuro-fuzzy inference system (ANFIS), which are tested for
performance comparison.
123

## Page 3

Aerospace Systems (2025) 8:701–716
703
Fig. 1 Proposed electric
propulsion system [9]
2.1 System architecture
The hybrid electric UAV system comprises the following
components:
• Fuel Cell: Acts as the main energy source, and its output
is controlled by an interleaved boost converter.
• Lithium-Ion Battery: serves as a second source of energy
and is connected via a bidirectional DC/DC converter to
regulate energy ﬂow throughout cycles of charging and
discharging.
• BLDC Motor: used to describe the load on the system for
UAV propulsion.
• DC Bus: Maintains a stable voltage for system opera-
tions.
2.2 Energy management strategies
Two distinct energy management strategies are implemented
and compared:
1. Fuzzy Logic Control: A rule-based system that dynam-
ically modiﬁes power ﬂow according to input variables
including battery state of charge (SOC) and load demand.
2. ANFIS: Fuzzy logic and neural networks are combined
in this hybrid intelligent approach to improve power dis-
tribution under changing operational conditions.
2.3 Simulation framework
The complete system was modeled and simulated using
MATLAB/Simulink. The following steps were followed:
• The interleaved boost converter for the fuel cell and the
bidirectional converter for the battery were designed and
integrated into the simulation environment.
• To govern the ﬂow of electricity between the fuel cell,
battery, and load, a fuzzy logic controller was created
using a predetermined set of rules.
• In order to determine the best power distribution patterns,
the ANFIS controller was trained using datasets created
from the system’s operating situations.
• To mimic real-world operating situations, simulation
parameters were deﬁned, including load changes, battery
state of charge, and UAV mission patterns.
2.4 Performance evaluation
The system’s performance was evaluated under various sce-
narios to assess:
• Power Flow: The distribution of power between the fuel
cell, battery, and load.
• Hydrogen Consumption: The efﬁciency of the fuel cell
in terms of hydrogen utilization.
• Battery Utilization: The stress on the battery during
charge and discharge cycles.
• Response Time: The time taken by each energy manage-
ment strategy to stabilize under dynamic load conditions.
2.5 Key metrics
The key comparative criteria were fuel cell power, battery
power, load power, hydrogen consumption, and total energy
efﬁciency. These outcomes were shown using time-domain
plots, which highlighted the performance of fuzzy logic and
ANFIS techniques under the same operating conditions.
123

## Page 4

704
Aerospace Systems (2025) 8:701–716
Table 1 UAV speciﬁcations [10]
Parameter
Value
Maximum operating altitude
600 (m)
Rate of climb ( R/C )
1 (m/s)
Stall speed (Vstall)
8 (m/s)
Take-off distance (d)
20 (m)
Maximum lift coefﬁcient (CLmax )
1.25
Zero lift drag coefﬁcient (CD,0)
0.036
Maximum L/D ratio
16.4
Total mass
7.75 (kg)
Table 2 Required UAV speeds
Flying mode
Required speed (rpm)
Take-off
1867
Climb
2445
Cruise
3183
Endurance
3395
Maximum velocity
4277
Table 3 UAV power requirement
Flying mode
Nominal power (W)
DC bus input power
Take-off
266
335
Maximum rate of climb
154.2
205
Cruise
84.6
125
Endurance
53.3
85
Maximum velocity
250
315
3 Analysis of proposed electric propulsion
system
The BLDC motor operates using an electronic commutation
system, thereby eliminating the need for brush maintenance
[8]. The conﬁguration of the proposed electric propulsion
system can be seen in Fig.1 [9]. The speciﬁcations of the
UAV are presented in Table 1. Based on these speciﬁcations,
therequiredoperatingspeedsarelistedinTable2,whichwere
used to determine the necessary power. The power require-
ments for UAV propulsion are outlined in Table 3, leading to
the selection of the motor whose speciﬁcations are provided
in Table 4.
3.1 Proposed propulsion system mathematical
modeling
The rotor of the BLDC motor is constructed from stainless
steel. Due to the high resistivity of stainless steel, the rotor
current was disregarded [11]. A topology scheme employ-
Table 4 BLDC motor speciﬁcations [10]
Parameter
Value
Maximum speed (rpm)
8000
Torque peak (mN.m)
1160
Maximum continuous torque (mN.m)
463
Motor constant (mN.m/W1/2)
103
Rotor inertia (g.cm2)
230
Number of phases (delta conﬁguration)
3
Number of poles
4
Phase-to-phase resistance ()
0.25
Torque constant (mN.m/A)
50.4
Back EMF constant (V/(rad/s))
0.0504
Inductance (mH)
0.59
Fig. 2 Six-switch three-phase inverter BLDC Motor drive [12]
ing a three-phase symmetrical bridge inverter, illustrated in
Fig.2, enables the use of six switches. The voltage equations
for a non-ideal six-switch three-phase inverter (SSTPI) are
provided as follows [11].
u A =

Ra + RDs(on)

ia
+ d
dt (La ia + Mab ib + Mac ic) + ea
(1)
Similarly, the voltage from point B to N and point C to N are
shown in Eqs. (2) and (3) respectively.
uB =

Rb + RDs(on)

ib
+ d
dt (Lb ib + Mba ia + Mbc ic) + eb
(2)
uC =

Rc + RDs(on)

ic
+ d
dt (Lc ic + Mca ia + Mcb ib) + ec
(3)
(u A), (uB), and (uC) denote the terminal voltages for phases
(a), (b), and (c) respectively, including the upper or lower
non-ideal MOSFET when it is in the ON state. The phase
123

## Page 5

Aerospace Systems (2025) 8:701–716
705
resistances for phases (a), (b), and (c) are represented as
(Ra), (Rb), and (Rc). The resistance from drain to source
when in the ON state is indicated by (RDs(on)). The self-
inductance values for phases (a), (b), and (c) are denoted as
(La), (Lb), and (Lc). Mutual inductances are represented
by (Mab) and (Mac) for phase (a) interacting with phases (b)
and (c), respectively. Similarly, (Mba) and (Mbc) describe the
mutual inductance between phase (b) and the other phases,
while (Mca) and (Mcb) correlate to phase (c) and its mutual
inductances. The back-EMFs for the respective phases (a),
(b), and (c) are shown as (ea), (eb), and (ec).
A salient-pole surface-mounted rotor is utilized in BLDC
motors [13]. Therefore, we can set (Ra = Rb = Rc = R),
(La = Lb = Lc = L), and (Mab = Mba = Mcb = Mbc =
Mac = Mca = M). Let (r) be deﬁned as (Ra + RDs(on)). By
inserting these values into Eq. (1), we can derive the required
results.
u A = r ia + L dia
dt + M dib
dt + M dic
dt + ea
(4)
Similarly,
uB = r ib + L dib
dt + M dia
dt + M dic
dt + eb
(5)
uC = r ic + L dic
dt + M dia
dt + M dib
dt + ec
(6)
The three phases’ current equation can be written as
ia + ib + ic = 0
(7)
Eq. (4) can be further simpliﬁed as:
u A = r ia + (L −M) dia
dt + ea
(8)
Similarly,
uB = r ib + (L −M) dib
dt + eb
(9)
uC = r ic + (L −M) dic
dt + ec
(10)
Let m = L −M. Next, the SSTPI BLDC motor’s voltage
equation matrix form can be written as follows:
⎡
⎣
u A
uB
uC
⎤
⎦=
⎡
⎣
r 0 0
0 r 0
0 0 r
⎤
⎦
⎡
⎣
ia
ib
ic
⎤
⎦+
⎡
⎣
m 0 0
0 m 0
0 0 m
⎤
⎦d
dt
⎡
⎣
ia
ib
ic
⎤
⎦+
⎡
⎣
ea
eb
ec
⎤
⎦
(11)
Hence in state space form:
d
dt
⎡
⎣
ia
ib
ic
⎤
⎦=
⎡
⎢⎣
1
m
0
0
0
1
m
0
0
0
1
m
⎤
⎥⎦
⎡
⎣
⎡
⎣
u A
uB
uC
⎤
⎦−
⎡
⎣
r 0 0
0 r 0
0 0 r
⎤
⎦
⎡
⎣
ia
ib
ic
⎤
⎦−
⎡
⎣
ea
eb
ec
⎤
⎦
⎤
⎦
(12)
3.2 Analysis and design of a DC-link voltage buck
converter
Connecting a DC buck converter to a BLDC motor drive
as a DC-link offers several advantages. The buck converter
ensures the BLDC motor receives a stable and controlled
voltage, regardless of ﬂuctuations in the input power source
(e.g., battery, fuel cell). This is critical for optimal motor
performance and efﬁciency. The buck converter ensures the
BLDC motor receives a stable and controlled voltage, regard-
less of ﬂuctuations in the input power sources. By stepping
down the input voltage to the optimal level required by the
motor drive, the buck converter minimizes power losses and
improves the overall system efﬁciency. A well-regulated DC-
link voltage simpliﬁes the control algorithms for the BLDC
motor drive. It allows for more precise modulation of the
inverter’s pulse-width modulation (PWM), improving the
motor’s performance. The buck converter can adjust the DC-
link voltage dynamically to suit the speciﬁc speed-torque
characteristics of the BLDC motor, enabling efﬁcient opera-
tion under varying load conditions. This is critical for optimal
motor performance and efﬁciency.
Considering the voltage across the diode, denoted as
(VDF), and the output voltage of the transistor, represented
as (Vout), this is illustrated in Eq. (13). The output voltage
ripple, (Vripple), is intended to be 1% of (Vout), and the min-
imum output current, (Imin), is assumed to be 10% of (Iout).
The voltage drop across (RDs(on)) is described in Eq. (14).
D = Vout + VDF
Vin −VDs(on)
(13)
VDs(on) = RDs(on) Iout
(14)
Switching period (T ) is:
T = 1/ fsw
(15)
The output capacitance at minimum

Cout(min)

is:
Cout ≥Cout(min) ,
Cout(min) = 2 Imin T
8 Vripple
(16)
123

## Page 6

706
Aerospace Systems (2025) 8:701–716
The inductor value at minimum (LCritical ) is:
L ≥LCritical,
LCritical =

Vin −Vout −VDs(on)

Ton
2 Imin
(17)
where Ton represents the time the system is in the "on" state,
and fsw denotes the switching frequency. The BLDC motor
control circuit is equipped with two PI controllers-one for
speed control and the other for current control. The mathe-
matical representation of the PI controller is given by:
u(t) = K pe(t) + Ki

 t
0
e(τ)dτ
(18)
where: K p represents the proportional gain, which is a tuning
parameter,and Ki istheintegralgain,alsoatuningparameter.
The term e(t) = SP−PV (t) indicates the error, where SP is
the set-point, and PV (t) is the process variable. The variable
t refers to time, speciﬁcally the present or instantaneous time,
while τ is the integration variable that takes values from time
0 up to the current time t. A PI speed controller is employed
to match the reference velocity

ωref

-which is the desired
motor speed-with the actual motor speed (ω).
4 Power converters design and control
Power converters play a vital role in the electric power sys-
tems and energy management systems of UAVs. With their
many beneﬁts that improve performance and dependability,
power converters are crucial parts of UAVs’ electric power
and energy management systems. They facilitate effective
voltage conversion and regulation, guaranteeing interoper-
ability across different UAV subsystems as sensors, avionics,
and propulsion motors. These gadgets maximize battery
efﬁciency and prolong the UAV’s operational duration by
reducing energy losses during power conversion. In order to
lessen reliance on primary energy sources, power converters
also make it easier to incorporate renewable energy sources-
like solar panels and fuel cells-into hybrid power systems.
They also help with load balancing and efﬁcient battery
management by stabilizing the power supply and shield-
ing delicate components from voltage swings. Their small
size and light weight help to optimize total weight, which is
essential for UAV effectiveness. Furthermore, because they
allow for quick reaction to changing power demands and
accurate control, power converters are essential components
of electric propulsion systems. All things considered, their
effectiveness and versatility are essential for contemporary
UAV applications, guaranteeing dependable and energy-
efﬁcient functioning. The BLDC motor was chosen as the
propulsion motor for the UAV, as described in the previous
Table 5 Selected battery pack speciﬁcation [10]
Parameter
Value
Fully charge voltage
12.2V
Minimum voltage
10V
Rated capacity
14Ah
Charging voltage
13.3V
Internal resistance
0.021 
Nominal discharge current
2.17A
Dimensions(mm)
161 × 115 × 56
Weight
950g
section. A boost converter connects the fuel cell (FC) stack
to the DC bus, whereas a bidirectional DC/DC converter is
used to link the battery pack to the system. The Li-Ion bat-
tery is utilized when additional load power beyond what the
FC can provide is required. Additionally, the battery helps to
maintain propulsion during transient conditions. The battery
capacityCB inthehybridelectricpowersystemisdetermined
by the bidirectional converter selection procedure.
As a design concern, the bidirectional converter input volt-
age is adjusted between 10 and 13 V, whereas the suggested
hybrid power system has a 24 V DC bus voltage. As a result,
a 12 V Li-Ion battery is chosen as the backup power supply.
At the battery minimum voltage, which denotes the bat-
tery’s lowest energy capacity, the necessary battery capacity
is calculated. The relationship between battery voltage and
capacity under speciﬁc power conditions is depicted in Eq.
(19). To avoid damage from excessive current, the maximum
discharging current is restricted to (0.5−0.7) CB. The spec-
iﬁcation of the battery pack is listed in Table 5.
CB =
PDC
0.7 · ηBDC · Vbat.min.
(19)
The hybrid system’s main source of power is the PEM
fuel cell system. Throughout the mission, the fuel cell system
serves as the primary power supply unit, producing electric-
ity continually. The maximum power of the PEM fuel cell
system is 150 W. To achieve 125 W of cruising power and
86 W of endurance power, a commercially available Horizon
H-100 PEM fuel cell system is chosen. The fuel cell system
has 24 cells with rated voltages of 14 V and 7.2 A. The input
voltage of the fuel cell system ranges from 13 to 23V. A
hydrogen ﬂow rate of 1.4liters per minute is necessary for
the PEM fuel cell system, and the supply hydrogen pressure
should be between 0.4 and 0.6 bars. The speciﬁcations for
the FC stack is listed in Table 6.
123

## Page 7

Aerospace Systems (2025) 8:701–716
707
Table 6 Selected fuel cell stack speciﬁcations [14]
Parameter
Value
Number of cells
24
Rated power
100W
Maximum power
150W
Rated voltage
14V
Rated current
7.2A
Output voltage range
13–23V
Weight
0.95Kg
Rated H2 gas consumption
1.4 l/min
Hydrogen pressure
0.4−0.6 bar
Max stack temperature
65 ◦C
Hydrogen purity
99.999%
Efﬁciency of system
40 % @ 14V
Table 7 Interleaved boost converter design speciﬁcations
Parameter
Value
Maximum power (W)
150
Maximum input voltage (V)
18
Minimum output voltage (V)
13
Regulated voltage output (V)
24
Percentage of peak current ripple (%)
1
Percentage of voltage ripple (%)
2
Switching frequency (Hz)
20,000
4.1 Interleaved boost converter
To ensure that each power stage delivers an equal share of
power, the interleaved boost converter (IBC) uses regulated
current distribution between stages. Therefore, in an inter-
leaved design, both channels should have matching inductors
and diodes, meaning that each inductor will have the same
inductance value; L1 = L2 = L. The duty cycles for Q1
and Q2 are assumed to be identical and are represented by
D1 and D2, i.e., D1 = D2 = D. The IBC operates in either
continuous or discontinuous mode, depending on the condi-
tions. The speciﬁcations for the IBC are provided in Table
7.
The capacitive and inductive components of the IBC
are designed to meet full power requirements. Depending
on its operating characteristics, the fuel cell (FC) output
voltage can range between 13 V and 18 V. The maximum
duty ratio (Dmax) for the pulse width modulation (PWM)
is determined when the FC voltage is at its minimum value
(VFC(min) = 13 V), as given in Eq. (20). Interleaved boost
converter Schematic Diagram is shown in Fig.3.
When the FC output voltage reaches its maximum
(VFC(max) = 18 V), the minimum conduction time is added
by reducing the PWM duty ratio, which is calculated using
Fig. 3 Interleaved boost converter Schematic Diagram
Eq. (21). The resulting IBC duty ratio range is between
0.25 ≤Dt ≤0.46. The output current (Io) of the converter
is based on the output power (cruise power) and the regulated
output voltage, as described in Eq. (22). The average induc-
tor current (IL( avg )) and the ripple current (IL) for each
phase are calculated using Eqs. (23) and (24), respectively.
Dmax = 1 −VFC(min)
VDC(bus)
(20)
Dmin = 1 −VFCmax
VDC(bus)
(21)
Io = Po
Vo
(22)
IL( avg ) =
0.5 Io
1 −Dmax
(23)
IL = 2 × (0.01) × IL( avg )
(24)
L = Vin(min) Dmax
IL Fs
(25)
The DC bus capacitor (CDC(bus)) stores energy during
Continuous Conduction Mode (CCM) when Q1 is in the OFF
state and releases this energy once Q1 switches ON. The
ripple voltage has a magnitude equivalent to 2% of the output
voltage, resulting in Vo = 0.48 V. The switching frequency
(Fs) effectively doubles when the output capacitor combines
all phases. The value of the output capacitor CDC(bus) can be
calculated using Eq. (26).
CDC(bus) =
Io Dmax
Vo (2Fs)
(26)
In conclusion, the interleaved boost converter has a
number of beneﬁts over the conventional boost converter,
especially for applications like UAV power systems that
demand high power and efﬁciency. The interleaved design
greatly lowers input current ripple by using numerous paral-
lel switching circuits, which lessens input source stress and
increases its longevity. Additionally, by dividing the electri-
cal and thermal load among several parts, this arrangement
improves dependability and thermal management. Addi-
tionally, by lowering switching and conduction losses, the
123

## Page 8

708
Aerospace Systems (2025) 8:701–716
Fig. 4 Schematic diagram of bidirectional converter
interleaved boost converter raises overall efﬁciency. It can
be scaled to meet different power demands because to its
modular design.
4.2 Bidirectional converter design and control
Bidirectional converters provide signiﬁcant beneﬁts for
effective power ﬂow and system ﬂexibility, making them
essential components of hybrid UAV energy management
systems. They make it possible for energy to move smoothly
between the UAV’s power sources, like fuel cells or solar
panels, and energy storage devices, including batteries and
supercapacitors. Dynamic power balancing is supported
by this dual-direction capability, which guarantees energy
availabilityduringperiodsofhighdemandandpermitsregen-
erative energy recovery during descent or deceleration.
Bidirectional converters extend battery life and improve
system efﬁciency by optimizing charge and discharge cycles.
They are crucial for hybrid UAVs that need precise energy
management for prolonged operation and a variety of mission
proﬁles because of their high efﬁciency and quick reaction
to power variations, which enhance dependability and per-
formance.
The bidirectional converter (BDC) adjusts the battery cur-
rent ﬂow path to meet load power requirements. During
conditions of high power demand or at startup, the BDC
boosts the battery voltage (boost mode), while during charg-
ing, the BDC operates in buck mode. The speciﬁcations for
designing the bidirectional converter are provided in Table
8.
4.2.1 Bidirectional converter boost mode operation
The duty cycle D is determined from the voltages of the LV
side and the HV side.
D = Vo(max) −ηVin(nom)
Vo(max)
(27)
The maximum duty cycle Dmax would, thus, be:
Dmax = Vo(max) −ηVin(min)
Vo(max)
(28)
For boost conﬁguration, The HV side DC bus current Io:
Io = Po
vo
= PL(max) −PFC(max)
vo
(29)
The LV side current IBat, which is the battery output current,
is determined as follows:
IBat =
Io
1 −D
(30)
The ripple of the peak-to-peak inductor current would be:
 IL = 2 × 0.01 × IL(max)
(31)
 IL = 2 × 0.01 ×
Io
1 −Dmax
(32)
The inductance value is:
L = Vin(min) Dmax
IL Fs
(33)
The HV side capacitor value can be calculated:
Chigh = Io Dmax
Vo Fs
(34)
4.2.2 Bidirectional converter buck mode operation
Bidirectional converters are essential to hybrid UAV energy
management systems because they facilitate effective energy
transfer and guarantee system adaptability. They facilitate
power transfer from energy storage systems (such as batter-
ies and supercapacitors) to the UAV’s subsystems and back
during regenerative operations because, in contrast to uni-
directional converters, they permit energy to ﬂow in both
directions.
Because it allows for dynamic power balancing between
various energy sources, such batteries, fuel cells, or solar
panels, and load demands, this dual-direction capability is
essential for hybrid UAVs. The schematic diagram of the
proposed BDC is illustrated in Fig.4. In the charging phase,
the BDC enters buck mode, where the active component is
MOSFET Q3, while Q2 remains passive. The PWM duty
ratio for Q3 is calculated using Eq. (35), assuming a mini-
mum voltage of VBat(min) = 10 V. The required maximum
duty cycle, corresponding to a battery voltage of 12.2 V, is
presented in Eq. (36). The BDC is controlled to regulate the
123

## Page 9

Aerospace Systems (2025) 8:701–716
709
Table 8 Bidirectional converter
design speciﬁcations
Boost conﬁguration
Parameter
Value
Buck conﬁguration
Minimum input LV (V)
10
Maximum input LV (V)
12.2
Nominal input LV (V)
12
Minimum output HV (V)
16
Maximum output HV (V)
30
Output LV (V)
13.3
Input HV (V)
24
Converter efﬁciency (%)
95
Percentage of peak current ripple (%)
1
Percentage of maximum HVS voltage ripple (%)
2
Switching frequency (Hz)
20,000
DC voltage and facilitate both battery charging and discharg-
ing operations [15].
Dmin = VBat(min)
VDC(bus)
(35)
Dmax = VBat(max)
VDC(bus)
(36)
The voltage ripple is to be 2% around the VLow.
CLV =
VLow (1 −Dbuck)
8 L F2s VLow(max)
(37)
The bidirectional converter effectively draws extra power
from storage to suit the UAV’s operational requirements dur-
ing times of high energy consumption, including takeoff or
quick maneuvers. On the other hand, the converter enables
regenerative energy recovery during low-power periods, such
braking or descent, returning the extra energy to storage sys-
tems for future use. By preserving stored energy, this feature
not only increases energy efﬁciency but also increases the
UAV’s operational durability.
Additionally, bidirectional converters’ precise control
maximizes battery charge and discharge cycles, prolong-
ing battery life and minimizing wear. Even in situations
when conditions ﬂuctuate, power supply is stable due to
their capacity to react swiftly to changes in power require-
ments. Bidirectional converters are an essential part of hybrid
UAVs that need great efﬁciency and dependability since they
also reduce energy losses during power transmission, which
increases system efﬁciency overall.
In conclusion, bidirectional converters are crucial for con-
temporary hybrid UAV systems that seek to optimize energy
utilization and reliability because they enable hybrid UAVs
to achieve increased energy efﬁciency, enhanced operational
performance, and longer ﬂight times. Their adaptability sup-
ports a wide range of mission proﬁles, guaranteeing that the
UAV can effectively adapt to varying power demands and
environmental conditions.
5 Proposed energy management system
Hybrid electric UAVs are highly dependent on the Energy
Management System (EMS) [16]. For the small UAV fuel
cell hybrid system described in Table 1, this study presents
a comparison between two different EMS strategies. The
hybrid system consists of a fuel cell (FC), a lithium-ion
battery, and DC/DC converters. Managing energy ﬂow in
this hybrid electric power system, especially in response to
changes in load demand and battery State of Charge (SOC), is
a critical aspect of these strategies [17]. The two energy man-
agement schemes compared include a rule-based fuzzy logic
control approach and an intelligent strategy utilizing an adap-
tive neuro-fuzzy inference system (ANFIS). The Proposed
hybrid electric system for the UAV is depicted in Fig.5.
Two primary performance metrics are used for compari-
son: hydrogen consumption and battery SOC. An effective
EMS should aim to maximize fuel efﬁciency while ensuring
responsible usage of each energy source. To optimize energy
usage in the hybrid system, the EMS monitors variations in
both transient load current and fuel cell power. These analy-
ses provide deeper insights into how the EMS functions and
how power is managed in hybrid power systems [16].
5.1 Proposed energy management system
architecture
The architecture of the hybrid model includes a primary fuel
cell (FC) source and secondary Li-Ion battery packs. The
design requirements for energy management are detailed
in Table 9. The EMS should achieve several objectives,
including an extended system lifespan, optimal system per-
formance, minimized hydrogen consumption, and a limited
123

## Page 10

710
Aerospace Systems (2025) 8:701–716
Fig. 5 Proposed hybrid electric
system for UAV
Table 9 Design requirements
for energy management system
Energy management design requirements
Value
Fuel cell converter output power [Pf c(min) - Pf c(max)] (Watt)
72.17–125
Battery SOC [SOCmin - SOCmax] (%)
60–90
DC bus voltage [VDC] (V)
24
Fig. 6 Fuel cell converter control scheme
Fig. 7 Battery converter control scheme
range of battery State of Charge (SOC). The EMS assesses
thereferencepowerforthefuelcell,withthisreferencepower
and voltage deﬁning the current of the FC, bounded by its
maximum and minimum values [18]. The unidirectional duty
cycle is determined using the error between the reference cur-
rent and the actual FC current. Figure6 depicts the control
scheme for the fuel cell converter as a subsystem of the over-
all EMS. For both EMS strategies, the VDC is regulated, as
illustrated in Fig.7.
The PI controller gains, tuned using a genetic algo-
rithm, compute the bidirectional duty ratio and facilitate both
battery charging and discharging operations [18]. The sub-
sequent sections provide a detailed examination of the EMS
strategies used to determine the reference FC power. The
rule-based fuzzy logic (RBFL) control strategy uses SOC
Table 10 Fuzzy logic control rules
Fuzzy logic control rules
SOC High
& PLow V ery Low
P⋆
f c = V ery Low
SOC High
& PLow Low
P⋆
f c = Low
SOC High
& PLow Medium
P⋆
f c = Medium
SOC High
& PLow High
P⋆
f c = High
SOC Medium
& PLow V eryLow
P⋆
f c = V ery Low
SOC Medium
& PLow Low
P⋆
f c = Low
SOC Medium
& PLow Medium
P⋆
f c = Medium
SOC Medium
& PLow High
P⋆
f c = High
SOC Low
& PLow V eryLow
P⋆
f c = Low
SOC Low
& PL Low
P⋆
f c = Medium
SOC Low
& PL Medium
P⋆
f c = High
SOC Low
& PL High
P⋆
f c = High
membership functions (MFs) and load power, along with
IF-THEN rules to decide on fuel cell power output. The
design is developed using a method similar to [18], in which
trapezoidal MFs are applied. The approach of Mamdani’s
fuzzy inference with the centroid method for defuzziﬁcation
is used. The rules are based on the “and” method between
them. Table 10 shows fuzzy logic rules.
The ANFIS, on the other hand, combines artiﬁcial neural
networks (ANN) with fuzzy logic techniques to establish the
reference FC power. This method integrates feedback data
with human expertise. The adaptability of ANFIS lies in its
hybrid learning algorithm, which combines gradient descent
123

## Page 11

Aerospace Systems (2025) 8:701–716
711
Fig. 8 Architecture of adaptive-neuro-fuzzy Controller
for optimizing neural network weights and least squares
estimation for ﬁne-tuning the fuzzy membership functions.
These mechanisms ensure that the system learns from input–
output data and reduces prediction errors iteratively. The
ﬂexibility of ANFIS is especially evident in its capacity to
adjust membership function parameters and fuzzy rules in
response to novel patterns found in the training set.
Without the need for human intervention, ANFIS can
adapt to changing circumstances and enhance its predic-
tive abilities by learning directly from datasets. Its efﬁciency
and adaptability are increased by this data-driven approach,
which makes it appropriate for dynamic, complicated sys-
tems. Furthermore, following training, ANFIS generalizes
well to unseen data, guaranteeing dependable performance
in practical applications. Combining the accuracy of neu-
ral networks with the adaptability of fuzzy systems, ANFIS
provides a potent solution for tasks like forecasting, opti-
mization, and control systems by dynamically adjusting to
changing issues. The proposed ANFIS controller architec-
ture is shown in Fig. 8, which consists of ﬁve distinct layers
[19]. In order to generate crisp outputs, ANFIS is organized
into ﬁve layers: crisp input processing, fuzziﬁcation, rule
application, normalization, and defuzziﬁcation. The system
can effectively map inputs to outputs thanks to this architec-
ture’s dynamic parameter adjustments. In the architecture,
ﬁxed nodes are represented by circles, while adaptive nodes
are depicted as squares.
ANFIS allows for quick tuning and rule generation. It uti-
lizes If-Then rules and Sugeno’s fuzzy inference technique,
with the ﬁnal outcome being a weighted sum of each rule’s
output [16]. The simulation deﬁnes MFs based on training
data. Both battery SOC and load power have seven MFs each.
Infuzziﬁcationlayer1,theinputsarefuzziﬁedusingEq.(38).
μ = max

min
x −a
b −a , 1, d −x
d −c

, 0

(38)
x represents a crisp value within the deﬁned range. The four
trapezoidal membership function heads are denoted by a,
b, c, and d, and the degree of MF output for this layer is
Fig. 9 Proposed UAV mission proﬁle
calculated accordingly.
OL1,i = μAi(SOC) i = 1, 2, . . . , 7
(39)
OL1, j = μB j (PL)
j = 1, 2, . . . , 7
(40)
In layer 2, the output of each node denotes the ﬁring
strength for the subsequent node, which involves perform-
ing a fuzzy logical AND operation. The expression for this
layer is given by Eq. (41), with k subject to 49 fuzzy rules.
Layer 3 is responsible for normalizing the input weights,
as described by Eq. (42), resulting in the normalized ﬁring
strengths. Layer 4 performs defuzziﬁcation, where the output
is determined by Eq. (43), using parameters uk, sk, and rk.
Finally, Layer 5 calculates the total output by combining all
input signals, as shown in Eq. (44) [16].
Wk = OL2,k = μAi(SOC) · μB j (PL)
(41)
W k = OL3,k =
Wk

k Wk
(42)
Wk fk = OL4,k =
Wk

k Wk
[rk(SOC) + sk (PL) + uk]
(43)
f = OL5,k =

Wk fk =
 Wk fk
 Wk
(44)
6 Results and discussion
A comparison of the two EMS strategies was conducted to
understand their strengths, weaknesses, and limitations in
different scenarios. The simulations began with the initial
conditions set as BSOC = 75%, battery temperature = 30◦, FC
voltage = 14V, and FC temperature = 40◦. Figure9 presents
a test case simulating the entire UAV mission.
123

## Page 12

712
Aerospace Systems (2025) 8:701–716
6.1 Power system model aligned with the UAV
mission profile
The mission proﬁle began with take-off (from point 0 to A)
and included phases such as climb (A to B), cruise (B to C),
descent(CtoD),endurance(DtoE),andﬁnally,landing(Eto
0). Each phase imposes distinct power requirements on the
propulsion and onboard systems. During takeoff, the UAV
requires a signiﬁcant power surge to overcome initial inertia
and achieve lift-off. This is primarily supplied by the battery
through the bidirectional DC/DC converter to ensure high
power availability. During the climb and cruise phases, the
power demand gradually decreases, and steady-state cruise
conditions are achieved, requiring lower but sustained power
levels. In descent and landing phases, the power demand
drops signiﬁcantly, as indicated in the mission proﬁle. The
battery takes over in certain scenarios to ensure smooth tran-
sitions and optimal SOC utilization.
To ensure accurate modeling and simulation of the power
management system, the UAV mission proﬁle has been
carefully mapped to the power system’s operational needs.
Simulation outcomes for the RBFL strategy are presented
in Figs.10, 11, and 12. When the load power falls below
cruising power (125 W), the DC bus voltage exceeds the
reference value of 24 V, prompting the DC bus voltage regu-
lator to generate a negative current to recharge the battery. As
the load power rises above 125 W, a sudden shift in battery
response occurs before stabilizing at the desired power level.
Although hydrogen consumption remains low, the battery
experiences signiﬁcant stress, with SOC ﬂuctuating between
75 and 69.88%, while the FC exhibits a faster response.
The ANFIS control strategy simulation results are shown
in Figs.13, 14, and 15. Under this approach, the FC oper-
ates in a relatively constant manner, leading to more frequent
recharging of the battery. Despite higher hydrogen consump-
tion, the FC undergoes maximum stress, whereas the SOC
remains between 75 and 70.21%. This strategy provides
superior battery transient response.
6.2 Strategies validation and adaptability
Figures 10 and 13 show a sudden peak in battery power
after 250s, indicating a transient reaction in the energy man-
agement system produced by a large change in load power
demand. During this time, the fuel cell, as the principal power
source, produces a reasonably consistent power output, most
likely due to its slower dynamic response. As a result, the
battery, which serves as the secondary energy source, com-
pensates for the current power shortage by rapidly increasing
output. This behavior highlights the battery’s vital role in
dealing with abrupt power surges and maintaining the sta-
bility of the UAV’s energy system. Figure13, which depicts
the outcomes of the ANFIS, shows that the battery’s peak
response is more efﬁciently handled than the other strategy,
which only uses fuzzy logic.
ANFIS displays great adaptability by dynamically alter-
ing power allocation between the fuel cell and the battery
to reduce stress on the energy storage system. This opti-
mized reaction minimizes the amplitude and length of the
battery’s peak, demonstrating ANFIS’ capacity to improve
overall system performance and reliability under unexpected
load periods. The better coordination between the energy
sources results in smoother power delivery and a longer bat-
tery life. A comparative summary of the two approaches is
given in Table 11. Hydrogen utilization and mass consump-
tion are essential factors for assessing the performance of a
fuel cell in hybrid energy systems.
According to Table 11, the hydrogen utilization is deﬁned
as the ratio of hydrogen actively utilized in the electrochemi-
cal reaction to total hydrogen supplied, which is an important
measure of the fuel cell’s operational efﬁciency. Meanwhile,
mass consumption quantiﬁes the entire amount of hydro-
gen depleted over time, which has a direct impact on the
system’s endurance and autonomy. Energy usage refers to
how much of the battery’s stored energy is discharged to
fulﬁll system power demands, demonstrating its contribu-
tion to power balance. Battery stress, on the other hand,
results from rapid charging or discharging cycles, which are
frequently induced by unexpected load ﬂuctuations, putting
mechanical and chemical strain on the battery. Prolonged or
extreme stress can accelerate degradation, limiting battery
life and compromising energy system reliability. Effective
energy management solutions are thus required to maximize
hydrogen usage, minimize mass consumption, and reduce
battery stress, ensuring system efﬁciency and lifespan.
When all four performance parameters are considered,
FLC performs better in terms of hydrogen conservation
efﬁciency. With 74.9% hydrogen utilization, compared to
ANFIS’s higher utilization of 82.86%. This demonstrates
FLC’s potential beneﬁt in systems where hydrogen fuel
preservation is crucial. However, ANFIS’s greater utilization
rate means that it produces more energy per unit of hydro-
gen, making it more suited for applications that require high
energy efﬁciency. Fuel cell stack consumption of 1.5 (lpm)
over 1h using ANFIS, the hydrogen mass consumption will
be approximately 0.07263 kg. But, using FLC, it will be
0.0581 kg.
In terms of battery performance, ANFIS outperforms
FLC, with a smaller Battery SOC Scope (75−70.21%) and
lower Battery Energy Utilization (6.39%). These ﬁgures
demonstrate ANFIS’s capacity to more accurately regulate
energy utilization, decreasing battery stress and increas-
ing operating lifespan. While FLC exhibits more hydrogen
conservation, ANFIS delivers more efﬁcient overall system
energy management.
123

## Page 13

Aerospace Systems (2025) 8:701–716
713
Fig. 10 Fuzzy logic results on
power ﬂow
Fig. 11 Fuzzy logic results on
hydrogen consumption
FLC’s performance reﬂects its simplicity and durabil-
ity, making it excellent for systems that prioritize hydrogen
conservation over maximum energy output. Its rule-based
decision-making enables constant and predictable energy
management, reducing fuel consumption at the expense of
slightly increased battery stress and overall SOC variation.
FLC is especially useful in systems where fuel supplies are
limited and operational longevity is crucial.
On the other hand, ANFIS’ hybrid architecture enables
adaptive optimization, making it an effective tool for systems
that require high energy efﬁciency. Its capacity to automat-
ically modify based on real-time data results in more exact
energy utilization, as indicated by improved battery metrics.
123

## Page 14

714
Aerospace Systems (2025) 8:701–716
Fig. 12 Fuzzy logic results on
DC bus voltage and load current
Fig. 13 Adaptive neuro-fuzzy
results on power ﬂow
Fig. 14 Adaptive neuro-fuzzy
results on DC bus voltage and
load current
However, this comes at a cost: increased hydrogen consump-
tion. ANFIS is most suited for applications that require peak
performance and energy economy, where fuel availability is
less of an issue.
6.3 Design validation with mission profile
Each strategy met the energy management criteria as outlined
in Table 9. The simulation results conﬁrm that the proposed
power system model and energy management strategies:
• Effectively distribute power during the UAV’s dynamic
mission phases.
123

## Page 15

Aerospace Systems (2025) 8:701–716
715
Fig. 15 Adaptive neuro-fuzzy
results on hydrogen
consumption
Table 11 Performance criteria
of energy management strategies
Performance criteria
Energy management strategy
Fuzzy logic
ANFIS
Hydrogen utilization (%)
74.9
82.86
Hydrogen mass consumption (Kg)
0.0581
0.07263
Battery SOC scope (%)
75–69.88
75–70.21
Battery energy utilization (%)
6.82
6.39
• Minimize hydrogen and battery stress, thereby enhancing
overall system endurance and reliability.
• Achieve superior performance under the ANFIS strategy
compared to the fuzzy logic approach, particularly in sta-
bilizing power ﬂow during transitions between mission
phases.
7 Conclusions
The paper is concerned with the electric UAV propulsion
system, which consists of two main subsystems: the electric
supply subsystem and the propulsion subsystem, intercon-
nected via a monitoring and controlling subsystem. The
electric supply subsystem combines the fuel cell stack as
a primary source and a Li-Ion battery pack as a secondary
source, allowing exploitation of both devices’ advantages
while mitigating their disadvantages. The UAV propulsion
subsystem comprises a BLDC motor, its associated inverter,
and control circuitry.
Two different energy management strategies (EMSs) were
investigated and compared under various ﬂight conditions,
with each starting from the same initial conditions. The com-
parison showed that the fuzzy logic strategy offered the best
hydrogen utilization and reduced fuel cell stress, while the
adaptive neuro-fuzzy strategy minimized battery stress but
resulted in higher hydrogen consumption.
123

## Page 16

716
Aerospace Systems (2025) 8:701–716
Future research directions should focus on exploring
the scalability of the proposed EMS framework for larger
UAVs or different unmanned systems. This would involve
adapting the control strategies to handle increased power
demands and higher system complexity and incorporating
additional renewable energy sources like solar panels. More-
over, extending the application of the EMS to other ﬁelds,
such as ground robots or marine vehicles, could provide valu-
able insights into its adaptability and effectiveness in a wider
range of autonomous systems. Investigating advanced opti-
mization techniques for multi-objective EMS design would
also contribute to further enhancing performance and efﬁ-
ciency in diverse operational contexts.
Funding This research did not receive any speciﬁc grant from funding
agencies.
Data availability The data supporting this study are available from the
corresponding author upon reasonable request.
Declarations
Conﬂict of interest The authors have not disclosed any Conﬂict of inter-
est.
References
1. Cai G, Dias J, Seneviratne L (2014) A survey of small-scale
unmanned aerial vehicles: Recent advances and future develop-
ment trends. Unmanned Syst 02(02):175–199. https://doi.org/10.
1142/S2301385014300017
2. Fei Y, Ding S, Li Y, Li X, Zhou Z, Zhang B, Li W (2021) A
novel bidirectional dc solid state power controller for fuel-cell-
powered uavs. In: IECON 2021–47th Annual Conference of the
IEEE Industrial Electronics Society, pp 1–6 . https://doi.org/10.
1109/IECON48115.2021.9589709
3. Bayram S, Boynuegri AR (2020) A comperative study on wiener
ﬁlter and wavelet transform for energy management systems on
hybridunmannedaerial vehicles.In: 20206thInternational Confer-
ence on Electric Power and Energy Conversion Systems (EPECS),
pp 112–117 . https://doi.org/10.1109/EPECS48981.2020.9304965
4. Wang W, Yu Y, Xu J, Zheng S, Deng Z (2021) The application
of uav in intelligent distribution line acceptance system. In: 2021
4th International Conference on Advanced Electronic Materials,
Computers and Software Engineering (AEMCSE), pp 289–293 .
https://doi.org/10.1109/AEMCSE51986.2021.00068
5. Xu L, Hu Z, Xu L, Li J, Ouyang M (2021) Simulation analysis
of fuel economy of a fuel cell/battery passive hybrid power system
for commercial vehicles. In: 2021 IEEE 4th International Electrical
and Energy Conference (CIEEC), pp 1–5 . https://doi.org/10.1109/
CIEEC50170.2021.9510209
6. Sun Y, Xu Q, Yuan Y, Yang B (2020) Optimal energy management
of fuel cell hybrid electric ships considering fuel cell aging cost. In:
2020 IEEE/IAS Industrial and Commercial Power System Asia (I
CPS Asia), pp 240–245. https://doi.org/10.1109/ICPSAsia48933.
2020.9208534
7. Wang H, Saha T, Riar B, Zane R (2019) Design considerations for
current-regulated series-resonant converters with a constant input
current. IEEE Trans Power Electron 34(1):141–150. https://doi.
org/10.1109/TPEL.2018.2819887
8. Hazari MR, Jahan E, Siraj M, Khan M, Saleque A (2014) Design
of a brushless dc (bldc) motor controller, pp 1–6 . https://doi.org/
10.1109/ICEEICT.2014.6919048
9. Shamseldin M (2016) Speed control of high performance brushless
dc motor. PhD thesis . https://doi.org/10.13140/RG.2.1.1472.9202
10. Karunarathne L (2012) An intelligent power management system
for unmanned aerial vehicle propulsion applications
11. Aspalli MS, Munshi FM, Medegar SL (2015) Speed control of bldc
motor with four switch three phase inverter using digital signal con-
troller. In: 2015 International Conference on Power and Advanced
Control Engineering (ICPACE), pp 371–376 . https://doi.org/10.
1109/ICPACE.2015.7274975
12. Saied M, Mostafa MZ, Abdel-Moneim TM, Yousef H (2006) On
three-phase six-switchesvoltage source inverter: a 150◦conduction
mode, vol 2, pp 1504–1509 . https://doi.org/10.1109/ISIE.2006.
295694
13. Elkerdany MS, Safwat IM, Yossef AMM, Elkhatib MM (2020)
A comparative study on using brushless dc motor six-switch and
four-switch inverter for uav propulsion system. In: 2020 12th
International Conference on Electrical Engineering (ICEENG), pp
58–61 . https://doi.org/10.1109/ICEENG45378.2020.9171757
14. Smith R (2010) Design of a control strategy for a fuel cell/battery
hybrid power supply
15. Garcia P, Fernandez LM, Garcia CA, Jurado F (2010) Energy man-
agement system of fuel-cell-battery hybrid tramway. IEEE Trans
Industr Electron 57(12):4013–4023. https://doi.org/10.1109/TIE.
2009.2034173
16. Elkerdany MS, Safwat IM, Mohamed Yossef AM, Elkhatib MM
(2020) Hybrid fuel cell/battery intelligent energy management
system for uav. In: 2020 16th International Computer Engineer-
ing Conference (ICENCO), pp 88–91 . https://doi.org/10.1109/
ICENCO49778.2020.9357393
17. Thounthong P, Rael S (2009) The beneﬁts of hybridization. Ind
Electron Mag IEEE 3:25–37. https://doi.org/10.1109/MIE.2009.
933885
18. Caux S, Hankache W, Fadel M, Hissel D (2010) On-line fuzzy
energy management for hybrid fuel cell systems. Int J Hydrogen
Energy 35:2134–2143. https://doi.org/10.1016/j.ijhydene.2009.
11.108
19. Elkerdany MS, Safwat IM, Youssef AMM, Elkhatib MM (2022)
A comparative analysis of energy management strategies for a
fuel-cell hybrid electric system uav. In: 2022 IEEE Aerospace Con-
ference (AERO), pp 1–10 . https://doi.org/10.1109/AERO53065.
2022.9843240
Springer Nature or its licensor (e.g. a society or other partner) holds
exclusive rights to this article under a publishing agreement with the
author(s) or other rightsholder(s); author self-archiving of the accepted
manuscript version of this article is solely governed by the terms of such
publishing agreement and applicable law.
123
