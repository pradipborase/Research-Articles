# Disturbance Observer-based Robust Control.pdf

## Page 1

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
 
Abstract—Disturbance Observer (DOb) has been one of 
the most widely used robust control tools since it was 
proposed by K. Ohnishi in 1983. This paper introduces the 
origins of DOb and presents a survey of the major results 
on DOb-based robust control in the last thirty-five years. 
Furthermore, it explains DOb’s analysis and synthesis 
techniques for linear and nonlinear systems by using a 
unified framework. In the last section, this paper presents 
concluding remarks on DOb-based robust control and its 
engineering applications. 
Index Terms — Disturbance Observer, Robust Control. 
I. INTRODUCTION 
ITH the severe sensitivity problem of the optimal 
control theory in engineering applications, robust 
control was emerged to deal with plant uncertainties and 
external disturbances in the beginning of 1970s. Several robust 
control techniques since then have been proposed in the 
literature. Among them, DOb is one of the most popular 
robust control tools due to its simplicity, flexibility and 
efficacy. In DOb-based robust control, internal and external 
disturbances are estimated by using identified dynamics and 
measurable states of plants, and the robustness of systems is 
simply 
achieved 
by 
feedbacking 
the 
estimations 
of 
disturbances. In the last four decades, this intuitive robust 
control technique has been experimentally verified in many 
different engineering applications, such as in robotics, 
mechatronics, automotive and power electronics. The 
objective of this paper is to provide an overview on DOb-
based robust control and its engineering applications. In this 
paper, DOb-based robust control technique is exemplified in 
the motion control framework.  
The paper is organized as follows. In section II, the origins 
of DOb is introduced. In section III, the major results on DOb-
 
E. Sariyildiz is with the School of Mechanical, Materials, 
Mechatronic and Biomedical Engineering, University of Wollongong, 
Wollongong, NSW 2522, Australia (corresponding author: phone: +61-
242213319; fax: +61- 242214577; e-mail: emre@uow.edu.au).  
 © 
20XX 
IEEE.  
Personal 
use 
of 
this 
material 
is 
permitted.  Permission from IEEE must be obtained for all other uses, 
in any current or future media, including reprinting/republishing this 
material for advertising or promotional purposes, creating new 
collective works, for resale or redistribution to servers or lists, or reuse 
of any copyrighted component of this work in other works. 
 
based robust control and its applications are presented. In 
section IV, DOb is synthesized in frequency and time 
domains. In section V, a Two-Degrees-of-Freedom (2-DoF) 
robust control system is synthesized by using DOb. In section 
VI, the paper ends with conclusion and remarks.  
II. ORIGINS OF DISTURBANCE OBSERVER 
A. Birth of Robust Control (1960s – 1980s): 
Plant uncertainties and external disturbances are inevitable 
and indispensable in many engineering systems; e.g., robots, 
hard-disk drives, chemical reactors and spacecraft [1]–[5]. 
Feedback controllers are designed so that the performance 
goals of systems can be achieved by attenuating disturbances 
in real implementations. Classical feedback control methods, 
such as Bode and root-locus, implicitly synthesize robust 
controllers with limited disturbance suppression capability [6, 
7]. Horowitz, for the first time, analytically formulized the 
trade-off between the robustness and performance of classical 
feedback control systems without explicitly using the 
robustness term in 1963 [8]. However, the significance of 
Horowitz’s contribution was not recognized in 1960s as the 
large model-plant mismatches were generally neglected in the 
ad hoc methods of classical design [7, 8]. At the same time, 
modern optimal control theory received increasing attention to 
tackle more complex control problems such as control of 
nonlinear and Multi-Input-Multi-Output (MIMO) systems [9]. 
Although 
modern 
control 
techniques 
provide 
strong 
mathematical tools, as well as wider application area, they are 
more sensitive to disturbances than classical control 
techniques. In the early 1970s, many researchers reported the 
failures of modern optimal control techniques due to lack of 
robustness [9]–[11]. A consensus was immediately reached on 
the importance of treating large disturbances in the design of 
controllers; and the robust control field was born in 1970s [9]. 
To describe the tracking performance of a system which 
suffers from disturbances, the robustness term was first 
explicitly used by Pearson and Stats in 1974 and Davison in 
1975 [12, 13]. In the following years, many robust control 
techniques were proposed to improve the stability and 
performance (i.e., robust stability and robust performance) of 
control systems in the presence of plant uncertainties and 
external disturbances; e.g., H∞ control, Sliding Mode Control 
(SMC), Structured Singular Values (SSV) or µ-synthesis, 
Internal Model Control (IMC) and Robust Parametric Control 
Disturbance Observer-based Robust Control 
and Its Applications: 35th Anniversary 
Overview 
Emre Sariyildiz, Member, IEEE, Roberto Oboe, Senior Member, IEEE, Kouhei Ohnishi, Life 
Fellow, IEEE 
W

## Page 2

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
such as Kharitonov’s theorem [14]–[18]. The failures of 
modern optimal control techniques have resulted in a 
significant paradigm shift from optimality to robustness in 
control theory. Today, robustness against disturbances, as well 
as achieving stability and performance goals, has become the 
key objective of a feedback controller synthesis.  
In general, robust control techniques can be divided into 
two categories: suppressing disturbances via feedback control, 
such as IMC and SSV, and cancelling disturbances via 
feedforward control [16, 17, 19]. The former has been well-
developed in the last four decades. However, it generally 
synthesizes complex controllers, it cannot react fast enough in 
the presence of strong disturbances although they can be 
eventually suppressed, and conservatism is a challenging 
problem in many robust feedback control methods such as H∞ 
control [20, 21]. In the latter, the reverse of disturbance signal 
is feedforwarded so that the robustness of a system is 
intuitively achieved by cancelling disturbances [19, 20]. The 
main drawback of this robust control technique is that 
disturbances are unknown and unmeasurable in many 
engineering systems so the robust feedforward controller 
synthesis is generally impractical. To tackle this problem, 
many observers have been proposed to estimate disturbances 
by using the measurable states and known dynamics of plants. 
The robustness of a system is similarly achieved by 
feedforwarding the estimations of disturbances instead of 
exact disturbances. In fact, a robust feedback controller is 
implicitly synthesized due to the dynamics of disturbance 
estimation when observers are used in the robust feedforward 
control 
technique. 
Therefore, 
observer-based 
robust 
controllers have also been described as an IMC method by 
many researchers in the literature [22, 23]. 
B. Birth of DOb (1960s – 1980s): 
DOb is the most popular robust control tool that is used to 
estimate plant uncertainties and external disturbances [24]. 
Similar to the robust control theory, the origins of DOb can be 
traced back to the 1960s. To deal with the sensitivity problems 
of conventional state observers (e.g., Luenberger observer), 
robust state observers were proposed by considering 
unknown/unmeasured inputs (i.e., external disturbances) of a 
system in 1960s and 1970s [25, 26]. Soon, it has been noticed 
that an Unknown Input Observer (UIO) that estimates external 
disturbances can be designed by slightly modifying robust 
state observers [27]. For the first time, Johnson improved the 
robustness of a control system by implicitly using the 
estimations of constant disturbances in 1968 and general 
disturbances in 1970 [28, 29]. In the following year, he 
designed an optimal robust controller, namely Disturbance 
Accommodating Controller (DAC), by explicitly using the 
estimations of external disturbances [30]. It is worth noting 
that Johnson made very important contributions to the 
observer-based robust control theory in the 1970s. For 
example, in 1973, he designed a robust controller by using an 
observer that estimates not only the external disturbances but 
also the states of a system [31]. Today, this robust control tool 
is known as Extended State Observer (ESO) in the literature 
[19]. The model-plant mismatches were neglected in the 
conventional DAC synthesis. In 1985, an adaptive DAC was 
proposed to deal with plant uncertainties in addition to 
external disturbances [32]. However, the practical significance 
of the observer-based robust controller synthesis was not 
noticed due to the complex optimal robust control structure of 
DAC. Ohnishi, for the first time, proposed the DOb to 
estimate the external disturbances of a servo system by using 
Gopinath’s reduced-order observer design method (aka 
auxiliary variable-based observer design method) in 1983 
[33]. Similar to DAC, an optimal controller with an integrator 
was implemented so that optimal performance was achieved 
by suppressing plant uncertainties while external disturbances 
were cancelled/suppressed with their estimations via DOb. 
With the auxiliary variable-based observer design method, the 
dynamics of disturbance estimation was explicitly formulized 
as a low-pass filter (LPF); i.e., the bandwidth of disturbance 
estimation was clearly described. After the first paper of DOb, 
an implicit DOb-based robust motion control system was 
proposed by Ohnishi in 1985 [34]. This work has clarified the 
2-DoF control structure of a DOb-based robust control system 
by using classical control techniques. It was theoretically and 
experimentally proven that the robustness and performance of 
a control system can be independently adjusted by using a 
DOb and a performance controller (e.g., a PD controller), 
respectively. To deal not only with the external disturbances 
but also with the plant uncertainties of a system, Ohnishi 
explicitly synthesized a DOb-based 2-DoF robust controller in 
1987 [35]. By lumping nonlinear plant dynamics and internal 
and external disturbances together into a fictitious disturbance 
variable, a linear nominal plant model was used in the design 
of DOb. In other words, a nonlinear system was linearized 
without requiring the precise dynamic model of the plant, and 
a robust controller was practically synthesized for a nonlinear 
system by using linear control methods. The DOb-based 2-
DoF robust controller was experimentally verified by 
performing the decentralized position control of a robot 
manipulator in this paper. In the 1980s, Ohnishi elegantly and 
cogently explained the practical significance of the observer-
based robust control by shifting its analysis and synthesis 
techniques from time domain to frequency domain. His 
proposals have been applied to many complex engineering 
systems in the last thirty-five years [36–39]. 
III. DEVELOPMENT OF DOB-BASED ROBUST CONTROL  
A. DOb-based Robust Control (1990s): 
Observer-based robust control received increasing attention 
by control practitioners in 1990s. DOb was applied to many 
different engineering applications from motion control of 
servo systems and CNC machines to power electronics, 
system identification and fault diagnosis [40] – [44]. Loop-
shaping control techniques, such as Bode/Nyquist plots and 
H∞ control, were generally used in continuous and discrete 
time domains in order to tune the stability and performance of 
the robust controller, i.e., the outer-loop performance 
controller, nominal plant dynamics and LPF of DOb. For 
example, Hori tuned the robustness and noise-sensitivity by 
shaping the frequency responses of the sensitivity and 
complementary sensitivity functions, respectively, in [40], 
Tomizuka improved the tracking performance of a servo 
system by combining Zero Phase Error Tracking Controller 
(ZPETC) and DOb in [45], Kempf showed that the design

## Page 3

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
constraints of DOb change when the plant includes time-delay 
in [46] and Mita proposed a new robust H∞ controller by 
using DOb in [47].  Although they were not as popular as the 
loop-shaping control methods, there were also few examples 
of advanced DOb-based robust control methods in 1990s; e.g., 
nonlinear  analysis and synthesis of the observer and robust 
controller [48] – [50], robust model predictive controller 
synthesis [51, 52], suppressing the chattering of an SMC 
controller by eliminating disturbances [53], robust repetitive 
learning control [54], robust fuzzy logic control [55], and the 
optimal robust controller synthesis by using Linear Quadratic 
Integral method [56]. In addition, there were some important 
theoretical results on the observer-based robust control 
method; e.g., the necessary and sufficient conditions for the 
existence of an observer with unknown inputs were given in 
[57, 58] and the equivalence of the passivity and DOb based 
robust control systems was shown in [48]. However, the 
significance of these studies was not recognized among 
control practitioners in 1990s due to complex control 
structures, practical limitations in implementations and lack of 
analysis and synthesis tools. Active Disturbance Rejection 
(ADR) control proposed by Han started to become popular in 
these years, particularly in China because it was originally 
published 
in 
Chinese 
[19]. 
An 
ADR 
controller 
is 
conventionally synthesized by using an ESO and minimum 
information for the nominal plant model (i.e., only the relative 
degree of the plant). Synthesizing the robust controller by 
using a simple dynamic model for complex systems is one of 
the most important advantageous of the DOb-based robust 
control technique (e.g., Ohnishi used a linear nominal plant 
model for a robot manipulator in [35]). Although a simple 
control law can be theoretically obtained by ignoring the 
complex dynamics of plants, this oversimplification has severe 
limitations in practice. The stability and performance of an 
observer-based robust control system may significantly 
deteriorate if the plant-model mismatches cannot be 
compensated due to practical design constraints such as noise 
and sampling time [23, 59]. The conventional ADR controller 
has several limitations in practice [59] – [62]. However, Han’s 
philosophical discussion on PID and ADR control frameworks 
has inspired many researchers in the last two decades [19]. 
B. DOb-based Robust Control (2000s): 
In addition to servomotors, robots and power electronics, 
DOb was applied to many different engineering systems, such 
as automobiles, electric commuter trains, networks, missile 
seekers, and spacecraft, in the last two decades [63] – [67]. 
High performance engineering applications have motivated 
not only control practitioners but also control theoreticians to 
study 
DOb-based 
robust 
control 
method. 
Today, 
if 
“disturbance observer” is searched in IEEE Xplore, then more 
than 990 Journals & Magazines and 3970 conference papers 
published between 2010 and 2019 are found. The same search 
results with 282 Journals & Magazines and 1309 conference 
papers published between 2000 and 2009 and 100 Journals & 
Magazines and 445 conference papers published between 
1990 and 1999. More and more researchers are adopting the 
DOb-based robust control method every year. 
In order to improve the stability and performance of DOb-
based robust control applications, more rigorous analysis and 
synthesis techniques were proposed by using linear control 
methods in 2000s. Compared to 1990s, not only the dynamics 
of the LPF of DOb, e.g., the bandwidth and order of the LPF, 
but also the nominal plant model and outer loop controller 
were thoroughly considered in the analysis. It was shown that 
the robust stability and performance significantly change when 
the plant includes right-half-plane pole(s)/zero(s) and/or time-
delay [23]. For example, an almost necessary and sufficient 
condition for the robust stability of the controller was given 
for minimum phase systems in [68], the exact condition was 
derived 
for 
minimum 
phase 
plants 
with 
parametric 
uncertainties in [69], a guide for the DOb-based robust 
controller synthesis was proposed for minimum and non-
minimum phase systems by using Bode Integral Theorem in 
[21, 23], a generalized DOb was proposed to estimate higher-
order disturbances in [70], a sensitivity optimization approach 
was proposed for digital implementation in [71], periodic 
disturbances were suppressed by using a periodic DOb in [72], 
the stability of the robust controller was analyzed under time 
delay in [73], and frequency and time domain analysis and 
synthesis techniques were developed in [74, 75]. The proposed 
linear control methods were widely adopted and applied to 
many 
different 
engineering 
applications 
by 
control 
practitioners. Today, we have several advanced linear control 
tools to analyze and synthesize DOb-based robust control 
systems.   
On the other hand, nonlinear control techniques became 
popular in the analysis and synthesis of DOb-based robust 
control systems in the early 2000s. X. Chen and Fukuda 
proposed a nonlinear DOb synthesis technique by using 
variable structure system theory in 2000 [76]. In the same 
year, W. Chen showed that the performance of disturbance 
estimation –thus the robustness of the control system– can be 
improved by using a nonlinear nominal dynamic model in the 
auxiliary variable-based design method [62]. The stabilities of 
the DOb and robust controller were proved by using the 
Lyapunov’s direct method [77]. When more complex nominal 
dynamic models (e.g., nonlinear dynamics of plants) are used 
in the design of DOb: better disturbance estimation can be 
achieved, the stability and performance of the robust control 
system can be improved, the bandwidth of DOb can be 
increased in practice and the trade-off between the robustness 
and noise-sensitivity can be tuned better [78]. Moreover, the 
nonlinear analysis and synthesis techniques help extend the 
application areas of DOb. The robust controller synthesis, 
however, may become less intuitive. Several nonlinear 
analysis and synthesis techniques since then have been 
developed for DOb-based robust control systems. For 
example, DOb was synthesized for multivariable nonlinear 
systems in [79], the robust controller was synthesized in a 
back-stepping manner and an input-to-state nonlinear stability 
analysis was proposed in [80], a linear DOb was extended to 
nonlinear systems in [81], a modular design method was 
proposed in [82], and a nonlinear stability analysis was 
proposed by considering the practical design constraints of 
DOb in [78]. With the proposed analysis and synthesis 
techniques, DOb was applied to different nonlinear systems 
such as a Duffing–Holmes chaotic system and nonlinear 
multi-agent systems [83, 84].

## Page 4

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
The flexible structure of the 2-DoF control method has 
allowed researchers to develop different DOb-based robust 
controllers in the last two decades. Several controllers were 
synthesized by combining DOb and an advanced control 
method, such as intelligent control, so that the robust stability 
and performance of the latter were improved. Some examples 
of these controllers in 2018 are as follows: a Neural Network 
controller was combined with an observer to control the 
trajectory of an underwater vehicle in [85], a Model Predictive 
controller was combined with an observer to control three-
phase inverters in [86], an SMC controller was combined with 
an observer to control fractional order systems in [87] and H∞ 
and resilient control methods were combined with an observer 
to control a nonlinear singular stochastic hybrid system with 
partly unknown Markovian jump parameters in [88]. The 
recent trend in DOb research shows that we will see more 
examples of the advanced 2-DoF robust controllers in the 
future. Nevertheless, the analysis and synthesis of the 
advanced robust controllers are more complicated than that of 
the conventional DOb-based robust controllers. 
C. Observer-based Robust Control and Applications: 
Robust motion control (e.g., position, force and compliance 
control) has been one of the most popular application areas of 
DOb since 1980s. The 2-DoF robust controller was applied to 
the motion control problem of many different engineering 
systems, spanning from industrial robots, hard-disk drives, 
automobiles and Hubble Space Telescope to today’s cutting 
edge robotic systems such as compliant exoskeletons, surgery 
robots and unmanned aerial vehicles [35] – [37], [89-92]. It 
was shown by Murakami that a DOb can be used not only to 
achieve the robustness of a motion control system but also to 
estimate contact force/torque as a force sensor [93]. This 
specific application of DOb is known as Reaction Force 
Observer (RFOb) in the literature, and it has been verified in 
many different engineering applications, e.g., in rehabilitation 
robotics, electric commuter trains and automotive [38, 64, 89].  
As a robust motion control tool, DOb has been rapidly 
matured in the last three decades. Today, DOb-based motion 
control products are commercially available in the market, and 
new motion control products keep being developed. For 
example, DOb was embedded in the Panasonic’s MINAS-A5 
series motor drivers to diminish the impact of the disturbance 
torque, reduce vibration, and offset any speed decline [94]; 
and a new LSI module was developed for real haptics by using 
DOb and RFOb in [95, 96]. 
In addition to motion control, DOb has been applied to 
several applications in different research fields in the last 
thirty-five years. For example, robotic eye-hand calibration 
[97], robust control of mineral grinding process [98], time 
delay estimation and compensation of network control systems 
[99], DC-bus voltage control of micro-grid systems [100], 
deadbeat control for UPS [101], partial synchronization of 
neurons [102], sensorless measurement of pulsatile flow rate 
[103], temperature control of a superheated steam [104], and 
feedback linearization control of a nuclear reactor [105]. Since 
plant dynamics are more complicated than servo systems, 
nonlinear nominal plant models and advanced performance 
controllers, 
such 
as 
nonlinear 
and 
iterative 
learning 
controllers, have been generally employed in the design of the 
robust controllers [87, 106, 107]. Although the performance 
controller and DOb can be independently synthesized thanks 
to the flexible structure of the 2-DoF control method, the 
analysis and synthesis of the advanced robust controllers are 
generally complicated.      
In the last three decades, DOb-based robust control has 
inspired many researchers. Several linear and nonlinear 
observer-based robust controllers have been independently 
developed in the literature. For example, the robust controllers 
based on: Perturbation Observer (PO), Equivalent Input 
Disturbance (EID) estimator, Uncertainty and Disturbance 
Estimator (UDE), Generalized Proportional Integral Observer 
(GPIO), Extended State Observer (ESO) and Extended High 
Gain Observer (EHGO) [108] – [112]. In these robust control 
systems, the fundamental idea behind the controller synthesis 
is same as the DOb-based robust control system: estimating 
the internal and external disturbances by using the known 
dynamics and measurable states of a system (i.e., disturbance 
observer 
synthesis), 
feedbacking 
the 
estimations 
of 
disturbances so as to intuitively achieve the robustness of the 
control system (i.e., disturbance cancellation/suppression) and 
tuning the performance controller by considering the nominal 
plant model (i.e., 2-DoF control). Therefore, they are 
described as DOb-based robust control in this paper. The 
reader is recommended to refer to [113] for a recent 
comprehensive survey on the observer-based robust control 
techniques. 
IV. ANALYSIS AND SYNTHESIS OF DOB  
A. Classical Control: 
Block diagram of a DOb is illustrated in Fig. 1a. In this 
figure, 




1
n
G
s
W s

 represents plant dynamics with 
unstructured uncertainty in which 

n
G
s  is nominal plant 
 
a) DOb is designed for a general linear system. 
 
b) DOb is designed for a servo system.  
Fig.1: Block diagrams of DOb.
+
+
+
+
+
-
-
-
d

q

n
G
s

1
n
G
s


Q s
n

des

dis

ˆdis

DOb

W s

+
+




Plant: 
1
n
G
s
W s

1
s
1
s
1
m
J
K
n
K
n
m
DOb
J
g
n
m
DOb
J
g
DOb
DOb
g
s
g

1
n
K

q
q
q
I

d








ˆdis

v
v
g
s
g

n
n
m
J
K
des
q


n

DOb
Servo Dynamics
des
I

## Page 5

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
model, 

W s  is a fixed stable transfer function, the weight, 
and 
s

 is a variable stable transfer function satisfying 

1
s



; 
d
 and 
n
 represent exogenous disturbance and 
noise inputs, respectively; q represents output; 
des

 represents 
the control signal of the performance controller; 

Q s  
represents the LPF of DOb; s  represents Laplace variable; 
dis

 represents a fictitious disturbance variable which includes 
internal and external disturbances; and ˆdis

represents the 
estimation of
dis

.  
By neglecting the exogenous noise input, the relation 
between input and output is derived from Fig. 1a as follows: 
                       


ˆ
n
des
dis
dis
q
G
s 





                        (1) 
where 





ˆ
1
dis
d
des
dis
W s
W s








 and

ˆdis
dis
Q s



. 
Eq. (1) shows that if the bandwidth of DOb is large enough, 
(i.e., 

1
Q s  and ˆdis
dis



), then the plant uncertainties and 
external disturbances are precisely eliminated with their 
estimations, and thus the performance controller can be 
designed by considering only the nominal plant dynamics. 
Indeed, this simple analysis works very-well in many practical 
applications such as robust motion control of robot 
manipulators. This is why frequency domain analysis and 
synthesis techniques of DOb have been widely adopted by 
control practitioners.  
Since the dynamics of the LPF of DOb directly influences 
the estimations of disturbances, its synthesis has received 
special consideration by many researchers [23, 34, 40]. The 
performance of disturbance estimation, and thus the 
robustness of the control system (See Fig. 1a), can be simply 
improved by either increasing the bandwidth of DOb or using 
a higher order LPF [23]. However, the bandwidth and the 
order of the LPF of a DOb are limited by practical and 
theoretical design constraints, e.g., noise and the waterbed 
effect, respectively [23, 42]. The former depends on the 
specifications of control equipment such as resolution of an 
encoder and sampling time of a real-time controller, and the 
latter depends on the dynamics of plants, such as RHP zeros 
and poles [23, 42].  
The sensitivity and complementary sensitivity transfer 
functions of a DOb-based robust control system are derived 
from Fig. 1a as follows: 
Sensitivity Function: 
              






1
1
1
DOb
Q s
S
Q s
W s
Q s





                   (2) 
Complementary Sensitivity Function: 
        









1
1
1
1
DOb
DOb
W s
Q s
T
S
Q s
W s
Q s






            (3) 
where 

1
DOb
S
Q s

 and 

DOb
T
Q s

 when 

0
W s 
, i.e., 
plant model is precisely known; 
0
DOb
S

 and 
1
DOb
T
as 
0
s
j


, i.e., at low frequencies; and 
1
DOb
S

 and 
0
DOb
T

as s
j

, i.e., at high frequencies.  
Eq. (2) and Eq. (3) show that a DOb-based robust controller 
can precisely suppress disturbances and noise at the 
asymptotic frequencies. However, the dynamic responses of 
the sensitivity and complementary sensitivity functions 
depend on the plant uncertainties and the LPF of DOb at the 
middle frequencies. In other words, the robustness, stability 
and performance of a DOb-based control system can be 
adjusted by tuning either the bandwidth of DOb or the 
nominal plant dynamics.  
To show how the bandwidth of LPF and the dynamics of 
nominal plant model influence the robust stability and 
performance, let us consider a DOb-based robust motion 
control system which is illustrated Fig. 1b. In this figure, 
m
J  
and 
n
m
J
 represent the uncertain and nominal inertias, 
respectively; Kand
n
Krepresent the uncertain and nominal 
thrust coefficients, respectively; 
,
q q and q represent the 
angle, velocity and acceleration of the servo system,  
respectively; 
DOb
g
 and 
vg  represent the bandwidths of the 
LPF of DOb and velocity measurement, respectively; I  
represents the motor current; and 
des
I
 and 
des
q
represent the 
desired I  and q, respectively. 
The sensitivity function of a DOb-based robust motion 
control system is derived from Fig. 1b as follows: 
                     


2
v
DOb
v
v
DOb
s s
g
S
s
g s
g g





                          (4) 
where 



n
n
m
m
J
K
J
K



.        
  Eq. (4) and Fig. 2 show that the robustness against 
disturbances can be simply improved at low frequencies by 
increasing either the bandwidth of DOb or. Higher values of 
 can be obtained by increasing 
n
m
J
or decreasing
n
K. 
However, the robust motion control system becomes more 
noise sensitive (See the waterbed effect in Fig. 2) [23]. The 
robust performance and stability of the motion control system 
deteriorate as the peaks of the sensitivity and complementary 
sensitivity transfer functions are increased at the middle 
frequencies as shown in Fig. 2. 
B. Modern Control: 
To synthesize a DOb in state space, let us consider the 
following dynamic model.  
                         
u
u






d
n
n
dis
x
Ax b
τ
x
A x b
τ


                                     (5) 
where x  and 
n

x
 represent the state vector of the system 
and its time derivative, respectively; A  and 
n n


n
A

 
represent the uncertain and nominal system matrices, 
respectively; b and 
n

n
b
 represent the uncertain and 
nominal control input vectors, respectively; u represents 
 
Fig.2: Frequency responses of the sensitivity function of Fig. 1b, i.e., Eq. (4),
when
1000rad/s
vg 
. 
101
102
103
104
Magnitude (dB)
-50
-40
-30
-20
-10
0
10
20
Bode Diagram
Frequency  (rad/s)

## Page 6

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
the control input; 
n

d
τ
 represents a disturbance vector 
which includes unknown plant dynamics and external 
disturbances; and 
n

dis
τ
 represents a disturbance vector 
which includes parametric uncertainties and 
d
τ , i.e., 




n
u






dis
n
n
d
τ
A
A x
b
b
τ
. 
For 
the 
sake 
of 
simplicity, the dynamic model of a single input system is used 
in Eq. (5). 
The disturbance vector 

dis
τ
 can be estimated by designing 
a minimum order observer for the following augmented state 
space model of the system [24, 30]. 
                   
u





























dis
dis
dis
dis
n
τ
n
τ
τ
τ
A
C
x
x
b
x
x
0
A
0


                  (6) 
where
m×m

dis
τ
A

and 
n×m

dis
τ
C

represent the system and 
output matrices of the disturbance model, i.e.,

dis
dis
dis
τ
τ
τ
x
A x

and 

dis
dis
dis
τ
τ
τ
C x
, respectively.  
Eq. (6) shows that the dynamic model of disturbances 
should be known a priori in the design of DOb. This 
assumption is indeed very strict as the dynamics of 
disturbances is generally unknown in engineering systems. A 
DOb, however, can precisely estimate disturbances by using 
very simple dynamic models; e.g., a constant disturbance 
model 


dis
τ
0

 is generally used to estimate not only constant 
but also variable disturbances in practice. It has been 
theoretically and experimentally verified in many studies since 
DOb was proposed in 1983 [23, 114]. For example, Fig. 2 
shows how variable disturbances are suppressed within the 
bandwidth of DOb. Of course, the performance of disturbance 
estimation can be improved with better approximation of the 
disturbance model; e.g., periodic disturbances are modeled to 
improve the robustness of DOb in [72].Disturbance estimation 
can also be improved by using Generalized DOb [70]. 
Instead of the conventional minimum order observer-based 
design method, the state space synthesis of DOb has been 
generally performed by using the auxiliary variable design 
method due to its simplicity [24, 35]. 
C. First-order DOb Synthesis using an Auxiliary Variable: 
The estimation of the disturbance vector 

dis
τ
 is derived in 
terms of an auxiliary variable and the states of the system as 
follows: 
                             ˆ
L


dis
τ
z
x                                     (7) 
where 
n
ˆ

dis
τ
 represents the estimation of 
dis
τ
; L
represents the observer gain of DOb to be tuned; and 
n

z
 
represents the auxiliary variable vector which is derived by 
integrating 
                       


ˆ
L
u



n
n
dis
z
A x b
τ

                            (8) 
The derivative of Eq. (7) is obtained by using Eq. (8) as 
follows: 
           




ˆ
ˆ
L
u
L
u






dis
n
n
dis
n
n
dis
τ
A x b
τ
A x b
τ

        (9) 
If 
dis
τ
 is subtracted from both sides of Eq. (9), then 
                            
L


dis
dis
τ
τ
dis
e
e
τ


                           (10) 
where 
n
ˆ



dis
τ
dis
dis
e
τ
τ
. 
Eq. (10) shows that asymptotic stability is achieved if L is 
strictly positive and 

dis
τ
0

. As it is discussed in the 
minimum order observer-based design method, the latter 
assumption of the asymptotic stability is very strict. If a more 
practical assumption is made by using 



dis
dis
τ
τ
 and 



dis
dis
τ
τ


, then it can be shown that the error of 
disturbance estimation is uniformly ultimately bounded when 
L is strictly positive, i.e.,  
           






0
0
exp
t
L t
t
t
L







dis
dis
dis
τ
τ
τ
e
e

        (11) 
where 
0

.  
Eq. (11) shows that the convergence rate and the accuracy 
of disturbance estimation can be simply improved by 
increasing the observer gain L, i.e., the bandwidth of DOb. 
However, the asymptotic stability of disturbance estimation 
cannot be achieved when

dis
τ
0

. 
D. High-order DOb Synthesis using Auxiliary Variables: 
Not only disturbances but also their successive time 
derivatives can be estimated by using a higher order DOb. To 
estimate the disturbance vector and its successive time 
derivatives up to the order of k-1, a kth order DOb can be 
similarly designed as follows: 
                                



1
2
ˆ
ˆ
k
L
L
L






k -1
dis
1
dis
2
dis
k
τ
z
x
τ
z
x
τ
z
x


                           (12) 
where 
n
ˆ

dis
τ
 represents the estimation of the disturbance 
vector
dis
τ
; 



n
ˆ
ˆ
,
,
,

k-1
dis
dis
dis
τ
τ
τ



 represent the estimations of the 
disturbance 
vector’s 
successive 
time 
derivatives, 
i.e., 


n
,
,
,

k-1
dis
dis
dis
τ
τ
τ



, respectively; 
jL  represents the jth 
observer gain to be tuned; and 
n

jz
 represents the jth 
auxiliary variable vector. The auxiliary variable vectors are 
derived by integrating        
                       






1
2
ˆ
ˆ
ˆ
ˆ
ˆ
k
L
u
L
u
L
u











1
n
n
dis
dis
2
n
n
dis
dis
k
n
n
dis
z
A x b
τ
τ
z
A x b
τ
τ
z
A x b
τ






                       (13) 
where 
n

jz
 represents the derivative of 
jz . 
Similar to the first order DOb analysis, if the kth order 
derivative of the disturbance vector is zero, then asymptotic 
stability can be achieved. However, if it is not zero but the 
disturbance vector and its successive time derivatives are 
bounded, then uniformly ultimately bounded estimation error 
can be achieved [20, 75]. The stability and performance of 
disturbance estimation are similarly adjusted by tuning 
observer gains as follows [20, 75]: 
     

1
2
1
2
1
k
k
k
k
DOb
k
k
g
L
L
L
L
















            (14) 
where 
DOb
g
 represents the bandwidth of the kth order DOb.

## Page 7

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
The performance of disturbance estimation can be improved 
by using a higher order DOb. However, it is more noise-
sensitive as it estimates the derivatives of disturbances; i.e., 
the bandwidth limitation becomes stricter as the order of DOb 
is increased. The reader is recommended to refer to [20, 23, 
75] for further details on the higher-order DOb analysis and 
synthesis. 
E. DOb Synthesis using Nonlinear Dynamics: 
A DOb can be similarly synthesized for a nonlinear system 
by using auxiliary variable design method. Let us consider the 
following 
nonlinear 
dynamic 
model 
to 
estimate 
the 
disturbance vector. 
                            




u
u






d
n
n
dis
x
f x
g x
τ
x
f
x
g
x
τ


                          (15) 
where 
f x  and 

n

nf
x
 represent the nonlinear uncertain 
and nominal system vectors, respectively; and 

g x  and

n

n
g
x
 represent the nonlinear uncertain and nominal 
control input vectors, respectively. The other parameters are 
same as defined earlier; however, 






dis
d
n
τ
τ
f
x
f x
 




n
u


n
g
x
g x
in Eq. (15).  
The estimation of the disturbance vector is derived in terms 
of an auxiliary variable and the states of the system as follows: 
                               

ˆ


dis
τ
z
L x                               (16) 
where 

n

L x
 represents the observer gain vector to be 
tuned; and z is derived by integrating 
                  





ˆ
u





n
n
dis
L x
z
f
x
g
x
τ
x

                  (17) 
The dynamic equation of disturbance estimation is derived 
by taking the derivative of Eq. (16) as follows:  
                            





dis
dis
τ
τ
dis
L x
e
e
τ
x


                     (18) 
where 
n
ˆ



dis
τ
dis
dis
e
τ
τ
; and 

n×n


L x
x

 represents 
the observer gain matrix to be tuned. 
Similar to Eq. (10), the stability of disturbance estimation 
can be achieved if 



L x
x  is a positive definite matrix. To 
adjust the stability and performance of disturbance estimation, 
a positive definite observer gain matrix, which satisfies Eq. 
(16) and Eq. (17), can be designed in different ways [62, 78]. 
Let us synthesize DOb for robot manipulators by intuitively 
tuning the observer gain matrix. The following nonlinear plant 
dynamics is used in the design of DOb.  
               







n
n
n
dis
M
q q
C
q,q q
g
q
τ- τ


               (19) 
where 

n×n

n
M
q

 represents the positive definite nominal 
inertia matrix;


n×n

n
C
q,q

represents the nominal Coriolis 
and centrifugal matrix; 

n

n
g
q
 represents the nominal 
gravity vector; 
n

τ
 represents the joint torque vector; 
n

dis
τ
 represents the disturbance vector which includes 
plant uncertainties and external disturbances; and 
,
q q and 
n

q
 represent the position, velocity and acceleration 
vectors of joints, respectively. 
A DOb can be designed by using known nonlinear dynamic 
model of a robot manipulator as follows: 
                                ˆ
L


dis
τ
z
q                                  (20) 
where ˆdis
τ
 is the estimation of 
dis
τ
; L is an observer gain 
to be tuned; and z  is derived by integrating 
            






ˆ
L



-1
n
n
n
dis
z
M
q
τ
C
q,q q
g
q - τ


            (21) 
The dynamic equation of disturbance estimation is derived 
by taking the derivative of Eq. (20) as follows:  
                            

L


dis
dis
-1
τ
n
τ
dis
e
M
q e
τ


                   (22) 
where 
n
ˆ



dis
τ
dis
dis
e
τ
τ
; and 


L



-1
n
L x
M
q
x
. 
If L  is strictly positive, then the stability (either asymptotic 
stability when  

dis
τ
0

 or uniformly ultimately bounded 
estimation error when 
dis
τ
 and 
dis
τ
 are bounded) of 
disturbance estimation is achieved [78]. Eq. (22) shows that 
the stability and performance of disturbance estimation can be 
directly adjusted by tuning the nominal inertia matrix and the 
observer gain of DOb. 
V. 2-DOF ROBUST CONTROLLER SYNTHESIS 
A. Classical Control: 
Block diagram of a DOb-based robust control system is 
illustrated in Fig. 3a. In this figure, 

C s  represents the 
performance controller, and 
ref
q
 represents the exogenous 
reference input. The other parameters are same as defined 
earlier.  
It has been experimentally verified in many applications 
that the performance controller can be tuned by considering 
only nominal plant dynamics in the outer-loop as DOb cancels 
plant uncertainties and external disturbances in the inner-loop. 
 
a) 
2-DoF robust control system via DOb. 
 
b) 
Acceleration-based robust position control system.  
Fig.3: Block diagrams of 2-DoF robust control systems via DOb. 
+
+
+
+
+
-
-
-
d

q

n
G
s

1
n
G
s


Q s
n

des

dis

ˆdis

DOb

W s

+
+




Plant: 
1
n
G
s
W s


C s
+
-
ref
q
Outer-Loop

Inner-Loop 
 
n
G
s

1
s
1
s
1
m
J
K
n
K
n
m
DOb
J
g
n
m
DOb
J
g
DOb
DOb
g
s
g

1
n
K

q
q
q
I

d







ˆdis

v
v
g
s
g

n
n
m
J
K
des
q

n
DOb
Servo Dynamics
des
I
D
p
K s
K

ref
q
ref
q





Inner-Loop 
 
n
G s

Outer-Loop

## Page 8

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
Since the robustness and performance of the control system 
can be independently adjusted by tuning DOb and the 
performance controller in the inner and outer loops, 
respectively, Fig. 3a is widely known as a 2-DoF robust 
controller in the literature [24]. In fact, this assumption has 
some practical limitations. The inner-loop dynamics, i.e., 
imperfect disturbance estimation, may affect the stability and 
performance of the robust control system if the model-plant 
mismatches cannot be precisely compensated by DOb. It can 
be easily shown by deriving the transfer function between the 
reference input and output from Fig. 3a as follows: 
            









1
1
1
n
ref
n
CG
s
W s
q
q
WQ s
CG
s
W s





            (23) 
where 


1
n
ref
n
CG
s
q
q
CG
s

as

1
Q s , i.e., 
0
s
jw


 or the 
bandwidth of DOb goes to infinite. 
Eq. (23) shows that the characteristic polynomial of the 
robust control system is influenced by the dynamics of the 
LPF of DOb, unstructured uncertainties, nominal plant model, 
and performance controller. The outer-loop transfer function 
of the robust control system can be free from the dynamics of 
the plant-model mismatches and the estimation of disturbances 
when the bandwidth of the LPF of DOb goes to infinite and/or 
the frequency of disturbances goes to zero. However, the 
former assumption is impractical as shown in Fig. 2 and the 
latter assumption is very strict for many engineering 
applications.   
To show how the nominal plant dynamics influences the 
stability of the 2-DoF robust control system, let us consider 
the Acceleration-Based Controller (ABC) that is illustrated in 
Fig. 3b. In this figure, 
P
K  and 
D
K  represent the position and 
velocity control gains of the outer-loop performance 
controller, respectively. The other parameters are same as 
defined earlier.  
 When the dynamics of velocity measurement is neglected 
(i.e., 
vg ), the transfer function between q and 
des
q
 is 
derived from Fig. 3b as follows: 
                               
DOb
des
DOb
s
g
q
q
s
g







                            (24) 
Eq. (24) shows that a DOb can be designed as a phase lead-
lag compensator by tuning  in the inner-loop. The phase 
margin, and thus the stability, of the robust position control 
system can be simply improved by increasingas shown in 
Fig. 4. However, it has an upper bound in practice (See the 
waterbed effect due to increasing in Fig. 2). 
B. Modern Control: 
If a plant includes only matched disturbances which act 
through the same channel as that of the control input, then the 
2-DoF robust controller can be similarly synthesized in state 
space. When a state feedback controller is used in the outer-
loop, the dynamic model of the closed-loop system is derived 
by using Eq. (5) as follows:  
                     




ˆdis
dis






n
n
n
x
A
b K x b

                     (25) 
where 
dis

and ˆdis

 represent the matched disturbance and 
its estimation, respectively; and 
T
n

K
represents the state 
feedback control gain. 
The stability of the robust control system can be proved by 
using the following Lyapunov function candidate. 
                                       
T
V x Px                                      (26) 
where



T




n
n
n
n
A
B K
P
P A
B K
Q; and P and 
n×n

Q 
 
are positive definite matrices.       
The derivative of Eq. (26) satisfies the following inequality. 
              







2
2
ˆ
V
min eig
1
dis
dis






n
Q
x
Pb

           (27) 
where 



min eig Q
 represents the slowest eigenvalue of Q . 
Eq. (27) shows that the time derivative of the Lyapunov 
function is negative outside of the compact set defined by  
        




2
2
n
1
ˆ
:
dis
dis
t
t












n
x
x
Pb


           (28) 
where




min eig
1


Q

.  
Eq. (27) and Eq. (28) show that any states start out of the 
compact set ultimately enter in  when the outer-loop 
performance controller and DOb are properly tuned. As the 
accuracy of disturbance estimation improves, i.e., ˆdis
dis



, 
the bound of the compact set  shrinks. In addition to 
disturbance estimation, the stability of the overall robust 
control system can be improved by properly tuning the 
performance controller; e.g., the upper bound of the set  
depends on Q and P as well as the disturbance estimation error 
as shown in Eq. (28).  
If a plant includes not only matched but also mismatched 
disturbances which act through the different channels from 
that of the control input, then the robustness cannot be 
achieved by directly cancelling disturbances with their 
estimations via DOb. Different control techniques have been 
proposed to deal with the mismatched disturbances by using 
DOb [20, 114, 115]. In general, the state space model of the 
system can be reconstructed by using the estimations of 
mismatched disturbances and their successive time derivatives 
so that a new state space model which suffers from only 
matched disturbances is obtained [20, 114]. The reconstructed 
states of the system are bounded when DOb is properly tuned. 
Therefore, a stable robust controller can be similarly 
synthesized by using a state feedback controller and canceling 
the matched disturbances of the reconstructed state space 
model of the system with their estimations as shown in Eq. 
(25) [20]. Since the estimations of disturbances and their 
Fig.4: Root-locus of the acceleration-based robust position control system
with respect towhen the LPF of velocity measurement is neglected. 
Imaginary Axis (seconds-1)

## Page 9

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
successive time derivatives are required to reconstruct the 
state space model with only matched disturbances, the 2-DoF 
robust controller becomes more sensitive to noise. The reader 
is recommended to refer to [20] for DOb-based robust control 
of a system with mismatched disturbances. 
A 2-DoF robust controller can be similarly synthesized for a 
nonlinear system by implementing a DOb in the inner-loop 
and a nonlinear performance controller in the outer-loop [53, 
62, 77, 78, 80, 81]. However, it is very hard to obtain a general 
2-DoF robust control structure as different observers and 
nonlinear controllers are synthesized in the inner and outer 
loops, respectively [77, 78, 87]. The stabilities of the observer 
and 2-DoF robust control system can be analyzed by using 
Lyapunov’s second method [77, 78]. 
VI. CONCLUDING REMARKS 
This paper has presented an overview on DOb-based robust 
control and its engineering applications. It is shown that the 
origins of DOb is as early as the origins of robust control 
theory which can be traced back to the end of 1960s. To 
improve the robustness of a Linear Quadratic Regulator, DOb-
based robust control, for the first time, was proposed by using 
Gopinath’s observer synthesis method in state space in 1983 
[33]. However, DOb-based robust control has received 
significant attention, particularly from control engineering 
practitioners, with its frequency domain analysis and synthesis 
techniques. This has caused a common mistake in the 
literature. Many researchers have erroneously described DOb 
as a linear disturbance estimation method which is synthesized 
in Laplace domain. In fact, for the first time, a DOb was 
proposed by using auxiliary variable design method in time 
domain. Moreover, this design method is applicable for not 
only linear but also nonlinear systems as shown in Section IV. 
Since a DOb-based robust controller can be intuitively 
synthesized without a strong mathematics background and 
easily implemented by using a simple microcontroller, control 
engineering practitioners have widely adopted this robust 
control technique and applied it to different engineering 
applications, particularly in the motion control and power 
electronic fields, in the last thirty-five years. Although a robust 
controller synthesis is the main driving force in the 
engineering applications of DOb, it has inspired many 
researchers to establish new practical control tools. For 
example, Murakami developed RFOb to estimate contact force 
by using DOb as a force sensor in [93], Natori developed 
Communication 
Disturbance 
Observer 
(CDOb) 
to 
estimate/compensate delay in network systems without using a 
model for delay in [65, 99], and Fujimoto developed Yaw-
Moment Observer (YMOb) to improve steering stability and 
comfortability in electrical vehicles in [89].Today, commercial 
robust motion control products developed by using DOb are 
available in the market and show superior performance results 
over conventional PID controllers [95, 96]. This motivates 
researchers to develop new DOb-based practical control tools 
and commercial robust motion control products. 
With the high performance motion control applications, 
many researchers from different fields have been attracted to 
the DOb-based robust control. Today, the examples of this 
robust control method can be found in Chemical Engineering 
[98], Telecommunications Engineering [99], Automotive 
Engineering [89], Aerospace Engineering [67], Biomedical 
Engineering [38], Renewable Energy Systems [116], Nuclear 
Science [105] and Biology [102], in addition to Electrical, 
Electronics and Mechanical Engineering [24, 111]. Several 
advanced control methods, such as nonlinear control, model 
predictive control, SMC and intelligent control, have been 
combined with DOb in order to apply the 2-DoF robust 
controller into complex systems. However, compared to 
motion control, DOb-based robust control and its applications 
are not matured in these fields yet. More practical and 
theoretical research should be conducted in order to improve 
the robust stability and performance of these applications, 
develop new analysis and synthesis techniques and establish 
new control tools such as RFOb. 
The intuitive robust controller synthesis is one of the most 
important superiorities of DOb-based 2-DoF control over 
other robust control methods such as H∞ and µ-synthesis. 
Many successful robust control implementations of DOb have 
been reported by intuitively synthesizing the 2-DoF robust 
controller in the last three decades. The main drawback of this 
method is that the design parameters (i.e., the dynamics of the 
LPF of DOb, nominal plant model and outer-loop controller) 
are generally tuned by trial and error, so the performance of 
the robust controller highly depends on designers’ own 
experience. To tackle this problem, several theoretical studies 
have been conducted in the last three decades. However, there 
is still lack of practical analysis and synthesis techniques for 
DOb-based robust control applications, particularly for 
systems with complex dynamics. The robust stability and 
performance of a DOb-based control system should be further 
investigated by considering the dynamics of the LPF of DOb 
(e.g., higher-order LPF) and nominal plant model (e.g., non-
minimum phase plants) in addition to the bandwidth of DOb. 
For example, although one of the earliest applications of DOb 
is the robust motion control of a robot manipulator proposed 
in 1987, tuning the parameters of the nominal inertia matrix is 
still an open problem [35]. Experimental results show that the 
robust stability and performance of the motion controller may 
significantly deteriorate when the nominal inertia matrix 
changes [78]. The practical design constraints (e.g., sampling 
time in digital implementation and noise-sensitivity due to 
encoder reading in motion control) and conservatism, which 
may cause a severe limitation for the bandwidth of DOb, 
should be considered when new analysis and synthesis 
techniques are developed. Besides, more effort should be paid 
to understand the practical limitations, (e.g., bounds on the 
robustness and performance) of the DOb-based robust control 
systems. 
Last but not least, developing standard analysis and 
synthesis tools for DOb-based control will help researchers 
easily adopt this robust control technique and apply it to 
various systems. To this end, H. Shim recently developed a 
new MATLAB toolbox for DOb-based robust control method, 
namely DO_DAT: Disturbance Observer – Design & Analysis 
Toolbox, [117]. Considering the significant increase in the 
popularity of DOb in the last decades, it is expected to see 
more examples of such control tools for DOb-based robust 
control method in the future.

## Page 10

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
REFERENCES 
[1] 
H. W. Bode, “Variable equalizers,” in The Bell System Technical 
Journal, vol. 17, no. 2, pp. 229-244, 1938. 
[2] 
H. G. Sage, M. F. De Mathelin  and E. Ostertag “Robust control of robot 
manipulators: A survey,” Int. J Control, vol. 72, no. 16, pp. 1498-1522, 
1999. 
[3] 
M. T. White, M. Tomizuka and C. Smith, “Improved track following in 
magnetic disk drives using a disturbance observer,” IEEE/ASME Trans 
Mechatron., vol. 5, no. 1, pp. 3-11, Mar 2000. 
[4] 
S. Skogestad, “Control structure design for complete chemical plants,”  
Computers & Chemical Engineering, vol. 28, no. 1–2, pp. 219-234, Jan. 
2004.  
[5] 
H. Gao, X. Yang and P. Shi, "Multi-Objective Robust H∞ Control of 
Spacecraft Rendezvous," IEEE Trans Control Syst Technol., vol. 17, no. 
4, pp. 794-802, July 2009. 
[6] 
I. R. Petersen and R. Tempo, “Robust control of uncertain systems: 
Classical results and recent developments,” Automatica, vol. 50, no. 5, 
pp. 1315-1335, May 2014.  
[7] 
M. G. Safonov, “Origins of robust control: Early history and future 
speculations,” Annual Reviews in Control, vol. 36, no. 2, pp. 173-181, 
Dec. 2012.  
[8] 
I. Horowitz, “Synthesis of feedback systems,” New York: Academic 
Press, 1963. 
[9] 
M. Athans, “On the LQG Problem,” IEEE Trans Automat Contr, vol. 16, 
no. 6, pp. 528-528, Dec 1971. 
[10] H. Rosenbrock and P. McMorran, "Good, bad, or optimal?," IEEE Trans 
Automat Contr, vol. 16, no. 6, pp. 552-554, Dec 1971.  
[11] J. Doyle, “Guaranteed margins for LQG regulators,” IEEE Trans 
Automat Contr, vol. 23, no. 4, pp. 756-757, Aug. 1971. 
[12] J. Pearson and P. Staats, “Robust controllers for linear regulators,”  
IEEE Trans Automat Contr, vol. 19, no. 3, pp. 231-234, Jun 1974. 
[13]  E. Davison, “The robust control of a servomechanism problem for linear 
time-invariant multivariable systems,” IEEE Trans Automat Contr, vol. 
21, no. 1, pp. 25-34, Feb 1976. 
[14] G. Zames, "Feedback and optimal sensitivity: Model reference 
transformations, multiplicative seminorms, and approximate inverses," 
IEEE Trans Automat Contr, vol. 26, no. 2, pp. 301-320, April 1981. 
[15] V. Utkin, "Variable structure systems with sliding modes," IEEE Trans 
Automat Contr, vol. 22, no. 2, pp. 212-222, Apr 1977. 
[16] J. C. Doyle, “Structured uncertainty in control system design,” IEEE 
Conference on Decision and Control, Fort Lauderdale, FL, USA, 1985, 
pp. 260-265. 
[17] B. A. F Francis, W. M. Wonham, “The internal model principle for linear 
multivariable regulators,” Applied Mathematics and Optimization, vol. 
2, no. 2, pp. 170-194, June 1974. 
[18] V. L. Kharitonov, “Asymptotic stability of an equilibrium position of a 
family of systems of linear differential equations”, Differential‘Nye 
Uravnenia, vol. 14, pp. 2086-2088, 1978. 
[19] J. Han, “From PID to active disturbance rejection control,” IEEE Trans. 
Ind. Electron., vol. 56, no. 3, pp. 900-906, Mar. 2009. 
[20] E. Sariyildiz, R. Mutlu, C. Zhang, “Active Disturbance Rejection Based 
Robust Trajectory Tracking Controller Design in State Space,” ASME. J. 
Dyn. Sys., Meas., Control, 2019. doi:10.1115/1.4042878. 
[21] E. Sariyildiz, K. Ohnishi, “Analysis the Robustness of Control Systems 
Based on Disturbance Observer”, Int. J Control, vol. 86, no. 10, pp. 
1733-1743, Oct. 2013. 
[22] R. Gorez, D. Galardini and K. Y. Zhu, “Internal model control and 
disturbance observers,” Proceedings of the 30th IEEE Conference on 
Decision and Control, Brighton, pp. 229-234, vol. 1, 1991. 
[23] E. Sariyildiz and K. Ohnishi, “A Guide to Design Disturbance 
Observer,” ASME. J. Dyn. Sys., Meas., Control, vol. 136, no. 2, pp. 1-10 
(021011) Mar. 2014. 
[24] K. Ohnishi, M. Shibata and T. Murakami, “Motion Control for 
Advanced Mechatronics,” IEEE/ASME Trans. Mechatron., vol. 1, no. 1, 
pp. 56–67, 1996. 
[25]  F. Schweppe, “Recursive state estimation: Unknown but bounded errors 
and system inputs,” IEEE Trans Automat Contr, vol. 13, no. 1, pp. 22-
28, Feb 1968. 
[26]  S. Bhattacharyya, “Observer design for linear systems with unknown 
inputs,” IEEE Trans Automat Contr, vol. 23, no. 3, pp. 483-484, Jun 
1978. 
[27] J. S. Meditch and G. H. Hostetter, “Observers for systems with unknown 
and inaccessible inputs,” Int J Control, vol. 19, no. 3, pp. 473-480, 1974. 
[28] C. Johnson, “Optimal control of the linear regulator with constant 
disturbances,” IEEE Trans Automat Contr, vol. 13, no. 4, pp. 416-421, 
Aug 1968. 
[29] C. Johnson, “Further study of the linear regulator with disturbances--The 
case of vector disturbances satisfying a linear differential equation,” 
IEEE Trans Automat Contr, vol. 15, no. 2, pp. 222-228, April 1970. 
[30] C. Johnson, “Accommodation of external disturbances in linear 
regulator and servomechanism problems,” IEEE Trans Automat Contr, 
vol. 16, no. 6, pp. 635-644, Dec 1971. 
[31] C. Johnson, “Accommodation of disturbances in optimal control 
problem,” Int. J. Control, vol. 15, no. 2, pp. 209-231, 1972. 
[32]  C. Johnson, “Adaptive controller design using disturbance accom-
modation techniques,” Int. J. Control, vol. 42, no. 1, pp. 193-210, 1985. 
[33] K. Ohishi, K. Ohnishi and K. Miyachi, “Torque – speed regulation of 
DC motor based on load torque estimation method,” International 
Power Electronics Conference, Tokyo, Japan, 27 – 31 Mar, 1983. 
[34] K. Tamaki, K. Ohishi, K. Ohnishi and K. Miyachi, “Microprocessor-
based robust control of a DC servo motor,” IEEE Control Syst Mag, vol. 
6, no. 5, pp. 30-36, Oct.1986. 
[35] M. Nakao, K. Ohnishi and K. Miyachi, “A Robust decentralized joint 
control based on interference estimation,” IEEE International 
Conference on Robotics and Automation, Raleigh, NC, USA, 1987. 
[36] L. Wang and J. Su, “Robust Disturbance Rejection Control for Attitude 
Tracking of an Aircraft,” IEEE Trans Control Syst Technol, vol. 23, no. 
6, pp. 2361-2368, Nov. 2015. 
[37] E. Sariyildiz, C. Gong, H. Yu, “An Acceleration-based Robust Motion 
Controller Design for a Novel Series Elastic Actuator”,  IEEE Trans on 
Ind. Electron, vol. 63, no. 3, pp. 1900-1910, Mar. 2016. 
[38] B. Ugurlu, M. Nishimura, K. Hyodo, M. Kawanishi and T. Narikiyo, 
“Proof of Concept for Robot-Aided Upper Limb Rehabilitation Using 
Disturbance Observers,” IEEE Trans. Human-Mach Syst, vol. 45, no. 1, 
pp. 110-118, Feb. 2015. 
[39]  Y. Wang, H. Fujimoto and S. Hara, “Driving Force Distribution and 
Control for EV With Four In-Wheel Motors: A Case Study of 
Acceleration on Split-Friction Surfaces,” IEEE Trans. Ind. Electron, vol. 
64, no. 4, pp. 3380-3388, April 2017. 
[40] T. Umeno and Y. Hori, “Robust speed control of DC servomotors using 
modern two degrees-of-freedom controller design,” IEEE Trans Ind 
Electron, vol. 38, no. 5, pp. 363-368, Oct 1991. 
[41] B-K Choi, C-H Choi and H. Lim, "Model-based disturbance attenuation 
for CNC machining centers in cutting process,"IEEE/ASME Trans 
Mechatron, vol. 4, no. 2, pp. 157-168, June 1999. 
[42] T. Yokoyama, A. Kawamura, "Disturbance observer based fully digital 
controlled PWM inverter for CVCF operation," IEEE Trans Power 
Electron, vol. 9, no. 5, pp. 473-480, Sept. 1994. 
[43] K. Ohnishi, T. Murakami, “Dynamics Identification of Multi-Degrees-
of-Freedom Manipulator Based on Disturbance Observer,” IFAC 
Proceedings Volumes, vol. 26, no. 2, pp. 685-688, 1993. 
[44] H. Wang, S. Daley, "Actuator fault diagnosis: an adaptive observer-
based technique," IEEE Trans Automat Contr, vol. 41, no. 7, pp. 1073-
1078, July 1996. 
[45] H. S. Lee, M. Tomizuka, "Robust motion controller design for high-
accuracy positioning systems," IEEE Trans. Ind. Electron, vol. 43, no. 1, 
pp. 48-55, Feb. 1996. 
[46] C. J. Kempf and S. Kobayashi, "Disturbance observer and feedforward 
design for a high-speed direct-drive positioning table," IEEE Trans 
Control Syst Technol, vol. 7, no. 5, pp. 513-526, Sept. 1999. 
[47] T. Mita, M. Hirata, K. Murata and H. Zhang, "H∞ control versus 
disturbance-observer-based control," IEEE Trans Ind Electron, vol. 45, 
no. 3, pp. 488-495, June 1998. 
[48]  R. Bickel and M. Tomizuka, “Passivity-based versus disturbance 
observer-based robot control: Equivalence and stability,” ASME. J. Dyn. 
Sys., Meas., Control, vol. 121, no.1, pp. 41-47, 1999. 
[49]  S. Oh, H. K. Khalil, “Nonlinear Output-Feedback Tracking Using High-
gain Observer and Variable Structure Control,” Automatica, vol. 33, no. 
10, pp. 1845-1856, 1997. 
[50] K.K. Busawon, M. Saif, “An observer for a class of disturbance driven 
nonlinear systems,” Applied Mathematics Letters, vol. 11, no 6, 1998, 
[51] K. S. Low, K. Y. Chiun and K. V. Ling, "A DSP-based servo system 
using generalized predictive control," Proceedings of Power Conversion 
Conference - PCC '97, Nagaoka, Japan, pp. 507-512 vol.1,1997. 
[52] K S Low, H. Zhuang, “Robust model predictive control and observer for 
direct drive applications,” IEEE Trans. Power Electron, vol. 15, no. 6, 
pp. 1018-1028, Nov. 2000.

## Page 11

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
[53] A. Kawamura, H. Itoh, K. Sakamoto, "Chattering reduction of 
disturbance observer based sliding mode control," IEEE Trans Ind Appl, 
vol. 30, no. 2, pp. 456-461, March-April 1994. 
[54] Y. Hamada and H. Otsuki, "Repetitive learning control system using 
disturbance observer for head positioning control system of magnetic 
disk drives," IEEE Trans Magn, vol. 32, no. 5, pp. 5019-5021, Sept. 
1996. 
[55] M. Shibata, T. Murakami and K. Ohnishi, "A unified approach to 
position and force control by fuzzy logic," IEEE Trans Ind Electron, vol. 
43, no. 1, pp. 81-87, Feb. 1996. 
[56] T. Hagiwara, E. Furutani and M. Araki, "Optimal observers for 
disturbance rejection in two-degree-of-freedom LQI servo systems," IEE 
Proceedings - Control Theory and Applications, vol. 144, no. 6, pp. 575-
581, Nov. 1997. 
[57]  M. Hou and P. C. Muller, "Disturbance decoupled observer design: a 
unified viewpoint," IEEE Trans Automat Contr, vol. 39, no. 6, pp. 1338-
1341, June 1994. 
[58] M. Hou, A. C. Pugh and P. C. Muller, "Disturbance decoupled 
functional observers," IEEE Trans Automat Contr, vol. 44, no. 2, pp. 
382-386, Feb. 1999. 
[59] E. Sariyildiz and K. Ohnishi, “Stability and Robustness of Disturbance 
Observer Based Motion Control Systems,” IEEE Trans Ind Electron, 
vol. 62, no. 1, pp. 414-422, Jan. 2015. 
[60] Z. Gao, "Scaling and bandwidth-parameterization based controller 
tuning," Proceedings of the 2003 American Control Conference, 2003, 
Denver, CO, USA, 2003, pp. 4989-4996. 
[61] S. Li, J. Yang, W. Chen and X. Chen, "Generalized Extended State 
Observer Based Control for Systems With Mismatched Uncertainties," 
IEEE Trans Ind Electron, vol. 59, no. 12, pp. 4792-4802, Dec. 2012. 
[62] W. Chen, D. J. Ballance, P. J. Gawthrop, J. O'Reilly, "A nonlinear 
disturbance observer for robotic manipulators," IEEE Trans Ind 
Electron, vol. 47, no. 4, pp. 932-938, Aug 2000. 
[63]  T. Bünte, D. Odenthal, B. A.-Guvenc, L. Guvenç, “Robust vehicle 
steering control design based on the disturbance observer,” Annual 
Reviews in Control, vol. 26, no. 1, pp. 139-149, 2002. 
[64] S. Kadowaki, K. Ohishi, I. Miyashita & S. Yasukawa “Anti-Slip/Skid 
Re-Adhesion Control of Electric Motor Coach Based on Disturbance 
Observer and Sensor-Less Vector Control,” EPE Journal, vol. 16, no. 2, 
pp. 7-15, 2006. 
[65] K. Natori and K. Ohnishi, "A Design Method of Communication 
Disturbance Observer for Time-Delay Compensation, Taking the 
Dynamic Property of Network Disturbance Into Account," IEEE Trans 
Ind Electron, vol. 55, no. 5, pp. 2152-2168, May 2008. 
[66] S. Sadhu and T. K. Ghoshal, "Sight Line Rate Estimation in Missile 
Seeker Using Disturbance Observer-Based Technique," IEEE Trans 
Control Syst Technol, vol. 19, no. 2, pp. 449-454, March 2011. 
[67] Z. Liu, J. Liu, L. Wang, “Disturbance observer based attitude control for 
flexible spacecraft with input magnitude and rate constraints,” 
Aerospace Science and Technology, vol. 72, pp. 486-492, 2018. 
[68] H. Shim and N. H. Jo, “An almost necessary and sufficient condition for 
robust stability of closed-loop systems with disturbance observer,” 
Automatica, vol. 45, no. 1, Pages 296-299, 2009. 
[69]  E. Sariyildiz and K. Ohnishi, “Bandwidth Constraints of Disturbance 
Observer in the Presence of Real Parametric Uncertainties,” European 
Journal of Control, vol. 19, no. 3, pp.199–205, May 2013. 
[70] K. Kim, K. Rew and S. Kim, "Disturbance Observer for Estimating 
Higher Order Disturbances in Time Series Expansion," IEEE Trans 
Automat Contr, vol. 55, no. 8, pp. 1905-1911, Aug. 2010. 
[71] A. Tesfaye, Ho Seong Lee and M. Tomizuka, "A sensitivity 
optimization approach to design of a disturbance observer in digital 
motion control systems," IEEE/ASME Trans Mechatron, vol. 5, no. 1, 
pp. 32-38, March 2000. 
[72] H. Muramatsu and S. Katsura, "An Adaptive Periodic-Disturbance 
Observer for Periodic-Disturbance Suppression," IEEE Trans Ind 
Informat, vol. 14, no. 10, pp. 4446-4456, Oct. 2018. 
[73] L.A. Castañeda, A. L. Juárez, G. O. Ortega, I. Chairez, Tracking control 
of uncertain time delay systems: An ADRC approach, Control 
Engineering Practice, vol. 78, pp. 97-104, 2018. 
[74] J. R. Ryoo, T-Y Doh, M. J. Chung, “Robust disturbance observer for the 
track-following control system of an optical disk drive,” Control 
Engineering Practice, vol. 12, no. 5, pp. 577-585, 2005. 
[75] E. Sariyildiz, C. Gong and H. Yu, “Robust Trajectory Tracking Control 
of Multi-mass Resonant Systems in State-Space,” IEEE Trans Ind 
Electron, vol. 64, no. 12, pp. 9366 - 9377, Dec. 2017. 
[76] X. Chen, S. Komada, T. Fukuda, "Design of a nonlinear disturbance 
observer," in IEEE Trans Ind Electron, vol. 47, no. 2, pp. 429-437, Apr 
2000. 
[77] Wen-Hua Chen, “Disturbance observer-based control for nonlinear 
systems,” IEEE/ASME Trans Mechatron, vol. 9, no. 4, pp. 706-710, Dec 
2004. 
[78] E. Sariyildiz, H. Sekiguchi, T. Nozaki, B. Ugurlu and K. Ohnishi, "A 
Stability Analysis for the Acceleration-based Robust Position Control of 
Robot Manipulators via Disturbance Observer," IEEE/ASME Trans. 
Mechatron, vol. 23, no. 5, pp. 2369-2378, Oct. 2018.  
[79] X. Chen, C-Y Su, T. Fukuda, "A nonlinear disturbance observer for 
multivariable systems and its application to magnetic bearing systems," 
IEEE Trans Control Syst Technol, vol. 12, no. 4, pp. 569-577, July 2004. 
[80] Z. Yang, H. Tsubakihara, S. Kanae, K. Wada and C. Su, "A Novel 
Robust Nonlinear Motion Controller With Disturbance Observer," IEEE 
Trans Control Syst Technol, vol. 16, no. 1, pp. 137-147, Jan. 2008. 
[81] J. Back, H. Shim, “Adding robustness to nominal output-feedback 
controllers for uncertain nonlinear systems: A nonlinear version of 
disturbance observer,” Automatica, vol 44, no 10, pp. 2528-2537, 2008. 
[82] C. Kravaris, G. Savoglidis, “Modular design of nonlinear observers for 
state and disturbance estimation,” Systems & Control Letters, vol. 57, 
no. 11, pp. 946-957, 2008. 
[83] M. Chen, S. S. Ge, “Direct Adaptive Neural Control for a Class of 
Uncertain Nonaffine Nonlinear Systems Based on Disturbance 
Observer,” IEEE Trans Cybern, vol. 43, no. 4, pp. 1213-1225, Aug. 
2013. 
[84] X. Ai, J. Yu, Z. Jia, D. Yang, X. Xu,Y. Shen, “Disturbance observer–
based consensus tracking for nonlinear multiagent systems with 
switching topologies” International Journal of Robust and Nonlinear 
Control, vol. 28, pp. 2144–2160, 2018. 
[85] Z. Peng and J. Wang, "Output-Feedback Path-Following Control of 
Autonomous Underwater Vehicles Based on an Extended State Observer 
and Projection Neural Networks," IEEE Trans Syst, Man, Cybern: 
Systems, vol. 48, no. 4, pp. 535-544, April 2018. 
[86] H. T. Nguyen and J. Jung, "Disturbance-Rejection-Based Model 
Predictive Control: Flexible-Mode Design With a Modulator for Three-
Phase Inverters," IEEE Trans Ind Electron, vol. 65, no. 4, pp. 2893-
2903, April 2018. 
[87] J. Wang, C. Shao, Y-Q, Chen, “Fractional order sliding mode control via 
disturbance observer for a class of fractional order systems with 
mismatched disturbance,” Mechatronics, vol. 53, pp. 8-19, 2018. 
[88] Y. Li, M. Chen, L. Cai, Q. Wu, “Resilient control based on disturbance 
observer for nonlinear singular stochastic hybrid system with partly 
unknown Markovian jump parameters,” Journal of the Franklin 
Institute, vol 355, no. 5, pp. 2243-2265, 2018. 
[89] H. Fujimoto, T. Saito, and T. Noguchi, “Motion stabilization control of 
electric vehicle under snowy conditions based on yaw-moment 
observer,” in Proc. 8th IEEE Int. Workshop Adv. Motion Control, 
Kawasaki, Japan, 2004, pp. 35–40. 
[90] I. S. Addington and C. D. Johnson, “Dual-mode disturbance 
accommodating pointing controller for Hubble Space Telescope”, 
Journal of Guidance, Control, and Dynamics, March, Vol. 18, No. 2, pp. 
200-207, Apr. 1995.  
[91] E. Sariyildiz, C. Gong, H. Yu, “A Unified Robust Motion Controller 
Design for Series Elastic Actuators”,  IEEE Trans. Mechatron, vol. 22, 
no. 5, pp. 2229 – 2240, Oct 2017. 
[92] Y. Nakajima, T. Nozaki and K. Ohnishi, "Heartbeat Synchronization 
With Haptic Feedback for Telesurgical Robot," IEEE Trans Ind 
Electron, vol. 61, no. 7, pp. 3753-3764, July 2014. 
[93] T. Murakami, F. Yu and K. Ohnishi, "Torque sensorless control in 
multidegree-of-freedom manipulator," IEEE Trans Ind Electron, vol. 40, 
no. 2, pp. 259-265, Apr 1993. 
[94] “Minas A5 series Operation Instruction”, https://www.panasonic-
electric-works.com/eu/minas-a5-motion-controller.htm.  
[95]  K. Ohnishi, T. Mizoguchi, “Real haptics and its applications”, IEEJ 
Transactions on Electrical Engineering, vol. 12, pp. 803-808, 2017. 
[96] https://www.motionlib.com/product/abc-core 
[97] J. Su, W. Qiu, H. Ma, P-Y Woo, "Calibration-free robotic eye-hand 
coordination based on an auto disturbance-rejection controller," in IEEE 
Trans Robot, vol. 20, no. 5, pp. 899-907, Oct. 2004. 
[98] P. Zhou, W. Dai and T. Y. Chai, "Multivariable Disturbance Observer 
Based Advanced Feedback Control Design and Its Application to a 
Grinding Circuit," IEEE Trans on Cont Syst Technol, vol. 22, no. 4, pp. 
1474-1485, July 2014.

## Page 12

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS 
 
[99] K. Natori, T. Tsuji, K. Ohnishi, A. Hace and K. Jezernik, "Time-Delay 
Compensation by Communication Disturbance Observer for Bilateral 
Teleoperation Under Time-Varying Delay," IEEE Trans Ind Electron, 
vol. 57, no. 3, pp. 1050-1062, March 2010. 
[100] C. Wang, X. Li, L. Guo and Y. W. Li, "A Nonlinear-Disturbance-
Observer-Based DC-Bus Voltage Control for a Hybrid AC/DC 
Microgrid," IEEE Trans Power Electron, vol. 29, no. 11, pp. 6162-6177, 
Nov. 2014. 
[101] H-S. Kim, H-T Moon, M-J Youn, “Online dead-time compensation 
method using disturbance observer”, IEEE Trans. Power Electron, vol. 
18, no. 6, pp. 1336-1345, Nov. 2003. 
[102] L. Siyao, Z. Guoshan, “Partial synchronization of Hindmarsh-Rose 
neurons via active disturbance rejection control,” 24th Chinese Control 
and Decision Conference (CCDC), Taiyuan, 2012, pp. 3751-3756. 
[103] C N Pai, T Shinshi, A Shimokohbe, “Sensorless measurement of 
pulsatile flow rate using a disturbance force observer in a magnetically 
levitated centrifugal blood pump during ventricular assistance,” Flow 
Measurement and Instrumentation, vol. 21, no. 1, pp. 33-39, 2010. 
[104] Z. Wu, T. He, D. Li, Y. Xue, L. Sun, L. Sun, “Superheated steam 
temperature control based on modified active disturbance rejection 
control,” Control Engineering Practice, vol. 83, pp. 83-97, 2019. 
[105] M. Eom, D. Chwa and D. Baang, "Robust Disturbance Observer-Based 
Feedback Linearization Control for a Research Reactor Considering a 
Power Change Rate Constraint," IEEE Trans Nucl Sci, vol. 62, no. 3, pp. 
1301-1312, June 2015. 
[106] G. J. Maeda, I. R. Manchester and D. C. Rye, "Combined ILC and 
Disturbance Observer for the Rejection of Near-Repetitive Disturbances, 
With Application to Excavation," IEEE Trans Control Syst Technol, vol. 
23, no. 5, pp. 1754-1769, Sept. 2015. 
[107] B-Z Guo and Z-L Zhao, “On Convergence of the Nonlinear Active 
Disturbance Rejection Control for MIMO Systems,” SIAM Journal on 
Control and Optimization, vol. 51, no. 2, pp. 1727–1757, 2013. 
[108] S. Kwon and W. K. Chung, “A discrete-time design and analysis of 
perturbation observer for motion control applications,” IEEE Trans 
Control Syst Technol, vol. 11, no. 3, pp. 399-407, May 2003. 
[109] J. H. She, M. Fang, Y. Ohyama, H. Hashimoto and M. Wu, “Improving 
Disturbance-Rejection Performance Based on an Equivalent-Input-
Disturbance Approach,” IEEE Trans Ind Electron, vol. 55, no. 1, pp. 
380-389, Jan. 2008. 
[110] Q. C. Zhong, A. Kuperman and R. K. Stobart, “Design of UDE-based 
controllers from their two-degree-of-freedom nature,” International 
Journal of Robust and Nonlinear Control, vol. 17, no. 21, pp. 1994–
2008, 2011. 
[111] H. Sira-Ramirez and M. A. Oliver-Salazar, “On the Robust Control of 
Buck-Converter DC-Motor Combinations,” 
IEEE Trans Power 
Electron, vol. 28, no. 8, pp. 3912-3922, Aug. 2013. 
[112] L. B. Freidovich and H. K. Khalil, “Performance Recovery of Feedback-
Linearization-Based Designs,” IEEE Trans Automat Contr, vol. 53, no. 
10, pp. 2324-2334, Nov. 2008. 
[113] W. H. Chen, J. Yang, L. Guo and S. Li, “Disturbance-Observer-Based 
Control and Related Methods—An Overview,” IEEE Trans Ind 
Electron, vol. 63, no. 2, pp. 1083-1095, Feb. 2016. 
[114] H. Shim, G. Park, Y. Joo, J. Back, N. Jo, “Yet another tutorial of 
disturbance observer: robust stabilization and recovery of nominal 
performance,” Control Theory and Technology, vol. 14, no. 4, pp. 237-
249, 2016. 
[115] J. Yang, S. Li and X. Yu, "Sliding-Mode Control for Systems with 
Mismatched Uncertainties via a Disturbance Observer," IEEE 
Transactions on Industrial Electronics, vol. 60, no. 1, pp. 160-169, Jan. 
2013. 
[116]J. J. Rubio, G. Ochoa, R. Balcazar, J. Pacheco, “Uniform stable observer 
for the disturbance estimation in two renewable energy systems,” ISA 
Transactions, vol. 58, pp. 155-164, 2015. 
 [117] H. Chang, H. Kim, G. Park, H. Shim, “DO-DAT: A MATLAB toolbox 
for design & analysis of disturbance observer,” IFAC-Papers OnLine, 
vol. 51, no. 25, pp. 340-345, 2018.
