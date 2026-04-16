# The composite disturbance observer based stochastic.pdf

## Page 1

ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Available online at www.sciencedirect.com 
Journal of the Franklin Institute xxx (xxxx) xxx 
www.elsevier.com/locate/jfranklin 
The composite-disturbance-observer based stochastic 
model predictive control for spacecrafts under 
multi-source disturbances 
Yang Xu a , Yuan Yuan a , ∗, Dalin Zhou b 
a School of Astronautics, Northwestern Polytechnical University, 710072, China 
b School of Computing, University of Portsmouth, Portsmouth PO1 3HE, U.K 
Received 13 October 2020; received in revised form 3 July 2021; accepted 5 August 2021 
Available online xxx 
Abstract 
In this paper, the attitude control problem of the spacecraft system under input/state constraints and 
multi-source disturbances is investigated. A novel estimation method, composite-disturbance-observer 
(CDO), is proposed to provide an estimate for both modeled and unmodeled disturbances in an online 
manner. Based on the estimates provided by the CDO, the composite stochastic model predictive control 
(C-SMPC) scheme is designed for attitude control. The recursive feasibility of the C-SMPC method is 
guaranteed by reformulating the state and input constraints. Furthermore, the sufﬁcient conditions are 
established to guarantee the stability of the overall closed-loop system. Finally, the simulation on the 
attitude control of the spacecraft is conducted to verify the effectiveness of the proposed method. 
© 2021 The Franklin Institute. Published by Elsevier Ltd. All rights reserved. 
1. Introduction 
Recent years have witnessed a constant research attention on the attitude control of space- 
crafts due mainly to its signiﬁcance in the critical orbital missions [1] . To accomplish these 
missions, spacecrafts may need to rotate along a relatively large-angle amplitude trajectory, 
which can be described by the nonlinear differential equations [2] . Additionally, in the attitude 
control problem, the uncertainty of spacecraft mass, the onboard payload motion, the rotation 
∗Corresponding author. 
E-mail address: snowkey@aliyun.com (Y. Yuan). 
https://doi.org/10.1016/j.jfranklin.2021.08.002 
0016-0032/© 2021 The Franklin Institute. Published by Elsevier Ltd. All rights reserved. 
Please cite this article as: Y. Xu, Y. Yuan and D. Zhou, The composite-disturbance-observer based stochastic 
model predictive control for spacecrafts under multi-source disturbances, Journal of the Franklin Institute, https: 
// doi.org/ 10.1016/ j.jfranklin.2021.08.002

## Page 2

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
of solar arrays and fuel consumption have to be simultaneously taken into consideration [3] . 
These two factors make the attitude control of spacecrafts extremely difﬁcult and motivate 
our current investigation. 
Unlike the success in an ideal environment, a practical control system is not guaranteed 
to function in real disturbance rejection problem and remains critical to be investigated. The 
problem has been signiﬁcantly addressed with an improved controller design. Among all the 
feasible candidates, the disturbance observer (DO) [4–8] driven solutions have been widely 
adopted to utilize its estimation for the disturbance. If the disturbance can be described by 
an exogenous system (modeled disturbance), the DO could make use of the information 
of the exogenous system and it is possible that the error dynamics of the DO system is 
asymptotically stable [9] . In [10] , a disturbance observer has been proposed to deal with the 
disturbances composed of the harmonic signals and signals with bounded H 2 -norm. Besides, in 
[11] , a disturbance observer has been constructed to estimate the disturbance with partially- 
known information under the white noise. On the other hand, if the disturbance can not 
be expressed by an exogenous system (unmodeled disturbance), the unmodeled disturbance 
can be treated as a slowly time-varying factor [12] yet not to be accurately estimated by 
the DO. In this case, the estimation error of the DO system can only be guaranteed to be 
bounded. To deal with the unmodeled disturbances, some other DO have been proposed. In 
[13] , an adaptive extended state observer (ESO) has been designed for nonlinear disturbed 
systems to get better ﬂexibility and performance than the traditional linear ESO. In [14] , an 
ESO has been proposed to estimate both state, and total disturbance which has included the 
internal uncertain nonlinear part and the external uncertain stochastic disturbance. Besides, 
in [15] , a learning-based DO has been augmented by a learning scheme, which has been 
motivated by iterative learning control, to further enhance the estimation and suppression of 
the disturbance when it has had repetitive components. Furthermore, in [16] , a DO has been 
developed to provide efﬁcient learning of the compounded disturbance which has included 
the effect of time-varying disturbance, fuzzy approximation error, and unknown dead zone. In 
[17] , a disturbance-observer-based control in combination with a neural network scheme and 
back-stepping method has been developed to achieve a composite anti-disturbance controller 
design that provides guaranteed performance. Despite the factual situation that engineering 
systems are subject both modeled and unmodeled disturbances simultaneously in practice, 
only a limited number of research have considered the multi-source disturbances [4,5,9] . 
Instead, most existing literature on the DO has been dedicated to solving problems under 
a unimodal (either modeled or unmodeled) disturbance. In this paper, a novel composite- 
disturbance-observer (CDO) is proposed to underpin the signiﬁcance of incorporating multi- 
source disturbances in the control problem by providing simultaneous estimate both modeled 
and unmodeled disturbances. The novel CDO forms a main contribution of this paper and 
underlies the rest research. 
Let alone the multi-source nature of disturbances in practice, their stochastic property re- 
mains another challenging issue to be addressed. As pointed out in [18] , by considering the 
state and input constraints in a probabilistic manner, the frequencies of the behaviors leading 
to the equipment fatigue could be signiﬁcantly reduced. As a result, the life of the facilities can 
be en-longed. It has been well recognized that the subsystems/facilities of the spacecraft are 
not easy to be replaced (or even repaired) [19] . As such, it is of signiﬁcance to investigate the 
control problem of the spacecraft subject to the probabilistic state and input constraints. Out of 
a number of candidates, stochastic model predictive control (SMPC) method is recognized as 
effective to accommodate stochastic disturbances. Different from the SMPC, the robust MPC 
2

## Page 3

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
has also been used to deal with uncertainties [20–23] . In [20] , the robust distributed MPC 
has been presented for a class of linear systems subject to structured time-varying uncertain- 
ties. In [21] , the robust distributed MPC has been proposed for a class of linear discrete-time 
systems with unknown parameters. The self-triggered robust MPC has been designed for non- 
holonomic vehicle with coupled input constraint and bounded disturbances [22] . Compared 
with traditional robust MPC, the SMPC is capable of handling the stochastic noise by us- 
ing the distribution information [24] . In [25] , the authors have proposed a Lyapunov-based 
model predictive controller for nonlinear systems subject to stochastic uncertainty, and the 
stabilization in probability is established. In [26] , the stochastic Lyapunov-based economic 
model predictive control has been proposed for a broad class of stochastic nonlinear systems 
with input constraints. Despite the effectiveness of SMPC and the inherent disturbances in 
the attitude control of spacecrafts, there is no bridging research in literature. This paper is 
presented as the ﬁrst attempt to ﬁll the gap. 
Summarizing the above discussions, in this paper, we are endeavored to investigate the 
attitude control problem of the spacecraft subject to probabilistic state and input constraints as 
well as the multi-source disturbances including modeled/unmodeled disturbance and stochastic 
noise. To be more speciﬁc, The composite SMPC (C-SMPC) is designed which constitutes of 
the SMPC and the estimate provided by the CDO. The main contributions of our paper are 
highlighted as follows: 1) the CDO can not only get the estimate of the disturbance generated 
by the exogenous system, but also enables to get the estimate of unknown nonlinearities; 2) 
the noise-to-state stability in probability of the CDO is guaranteed by the proposed sufﬁcient 
conditions; and 3) the recursive feasibility and mean square stability of the closed-loop system 
are guaranteed under the proposed C-SMPC scheme. 
Notation : In this paper, Z ≥0 represent the natural number set. Z + represents the positive 
integer set. Z [ a, b] with a, b ∈ Z ≥0 represents the positive integer set { a, a + 1 , · · · , b} . R n 
denotes the n-dimensional Euclidean space. For any matrix A , A ∈ R n×m denotes the A is a 
n × m-dimensional matrix. A T denotes the transpose of matrix A . Denote ∥ x∥ as the Euclidean 
norm of x and ∥ x ∥ P ≜ 
√ 
x T P x as the P -weighted norm of x. 0 m×n represents the m × n
dimensional matrix full of 0. I m×n represents the m × n dimensional matrix full of 1. 1 + 
represents the right limit of 1. ∗represents the symmetric part in the matrix. 
2. Problem formulation and preliminaries 
2.1. System model 
Consider the attitude dynamics of the spacecraft in the body frame [39] : 
J s/c ˙ 
ω −(J s/c ω) × ω = u + d ext 
(1) 
where ω ∈ R 3 is the angular velocity; J s/c ∈ R 3 is the rotational inertial of the spacecraft; 
u ∈ R 3 and d ext ∈ R 3 are the control input and external disturbance, respectively. In actual 
practice, the change of J s/c is negligible, i.e., ˙ 
J s/c = 0. 
In this paper, the Modiﬁed Rodriguez Parameters (MRPs) are used to describe the orien- 
tation of the rigid body relative to the inertial frame [27] . Then, we have 
˙ q = Z ( q ) ω 
(2) 
3

## Page 4

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
where 
Z ( q ) = 1 
2 

I 3 ×3 
1 −q T q 
2 

+ q q T + S ( q ) 

with q = [ q 1 q 2 q 3 ] T and the skew-symmetric matrix function 
S ( q ) = 
⎡ 
⎣ 
0 
−q 3 
q 2 
q 3 
0 
−q 1 
−q 2 
q 1 
0 
⎤ 
⎦ 
According to Chung et al. [28] , based on (1) and (2) , the following Lagrangian formulation 
of attitude dynamics is obtained in terms of the MRPs: 
¨q = M −1 ( q ) 

−C ( q , ˙ q ) ˙ q + τext 

+ M −1 ( q ) τu 
(3) 
with 
τu = Z −T ( q ) u , τext = Z −T ( q ) d ext , M ( q ) = Z −T ( q ) J s/c Z −1 ( q ) 
C ( q , ˙ q ) = −M ( q ) ˙ 
Z ( q ) Z −1 ( q ) −Z −T ( q ) S (J s/c Z −1 ( q ) ˙ q ) Z −1 ( q ) 
To begin with, we consider the case that d ext is composed of three types of disturbances: 
the deterministic modeled disturbance d o (t) , stochastic noise d s (t) and a norm bounded dis- 
turbance d b (t) , i.e., d ext = d o (t) + d s (t) + d b (t) . We assume that d o (t) is generated by the 
following exogenous system: 
˙ 
w (t) = ˜ 
W w(t) + ˜ 
H η(t ) , d o (t ) = ˜ 
V w(t) 
(4) 
where w(t) ∈ R 3 is the auxiliary state of the exogenous system. According to Guo and 
Chen [4] , d o normally represents harmonic (or constant) disturbance and hence we suppose 
∥ w(t) ∥ 2 ≤¯w . The matrices ˜ 
W , ˜ 
H and ˜ 
V are known. η(t) ∈ R 6 represents the uncertainties 
in the exogenous system with η(t) ∈ l 2 [0, ∞ ) and we suppose ∥ η(t) ∥ 2 ≤¯η. Additionally, we 
take into consideration of the stochastic noise d s (t) satisfying 
Pr { d s,i (t) ≤ηs,i } = F s,i (ηs,i ) 
F s,i (ηs,i ) = 
 1 , 
for ηs,i ≥αs,i 
0, 
for ηs,i < −αs,i 
(5) 
where αs,i > 0, i ∈ { 1 , 2, 3 } . Denote d s,i (t) as the ith component of d s (t) . Note that d s, 1 (t) , 
d s, 2 (t) and d s, 3 (t) are mutually independent. The distribution function F s,i (·) is continuous 
on the right with only a ﬁnite number of discontinuities. The distribution rule (5) sug- 
gests that d s,i (t) lie in the orthotope, namely, d s,i (t) ∈ s,i = 

d s,i : | d s,i | ≤¯d s,i 

. In other 
words, we have ∥ d s (t) ∥ 2 = 
  3 
i=1 | d s,i | 2 ≤
  3 
i=1 ¯d s,i = ¯d s . Denote the expectation and 
variance of d s (t) as ˜ 
d s = [ ˜ 
d s, 1 ˜ 
d s, 2 ˜ 
d s, 3 ] T and ˘d s = [ ˘d s, 1 ˘d s, 2 ˘d s, 3 ] , respectively. d b (t) sat- 
isﬁes ∥ d b (t) ∥ 2 ≤¯d b . Denote x 1 = q 1 , x 2 = q 2 , x 3 = q 3 , x 4 = ˙ 
q 1 , x 5 = ˙ 
q 2 , x 6 = ˙ 
q 3 , d f = 
M −1 ( q ) 

−C ( q , ˙ q ) ˙ q + τext 

−d o −d s and u = Z ( q ) J −1 
s/c u . It is worth pointing out that d f (t) 
can be regarded as the unmodeled disturbance. According to Properties 1–4 in [29] , M −1 ( q ) , 
C ( q , ˙ q ) ˙ q , τext , d o and d s are all bounded. Therefore, d f (t) is bounded with ∥ d f (t) ∥ 2 ≤¯d f . 
System (3) can be rewritten compactly as: 
 ˙ 
x (t) 
= ˜ 
A x(t) + ˜ 
B u(t) + ˜ 
G d f (t) + ˜ 
G d o (t) + ˜ 
G d s (t) 
y(t) 
= ˜ 
C x(t) 
(6) 
4

## Page 5

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
where 
˜ 
A = 
 0 3 ×3 
I 3 ×3 
0 3 ×3 
0 3 ×3 

, ˜ 
B = ˜ 
G = 
 0 3 ×3 
I 3 ×3 

˜ 
C = 

 I 3 ×3 
0 3 ×3 

By discrediting (4) , we have 
w(k + 1) = W w(k) + H η(k ) , d o (k ) = V w(k) 
where W = e ˜ 
W T , H = 
 T 
0 ˜ 
H e ˜ 
W τdτ, V = ˜ 
V with T being the sampling interval. According 
to Chang [30] , if the sampling period T is small enough, we have ∥ d f (k + 1) −d f (k) ∥ 2 ≤
∥ O(T 2 ) ∥ 2 ≤δ f where δ f is a constant. Up to now, we could provide the discrete-time model 
for the spacecraft as follows: 
 x(k + 1) 
= Ax(k) + Bu(k) + G (d f (k) + d o (k) + d s (k) + O(T 2 )) 
y(k) 
= Cx(k) 
(7) 
where A = e ˜ 
A T , B = 
 T 
0 ˜ 
B e ˜ 
A τdτ, G = 
 T 
0 ˜ 
G e ˜ 
A τdτ, C = ˜ 
C . Considering the probabilistic con- 
straints, we have 
Pr { b T 
x x(k) ≥h x } ≤l x 
(8) 
Pr { b T 
u u(k) ≥h u } ≤l u 
(9) 
where b x , b u , h x and h u are given constant vectors with appropriate dimensions; l x and l u 
represent probabilities with l x ∈ [0, 1] and l u ∈ [0, 1] , respectively. 
Up to now, we are ready to present the design objectives of this paper: 1) design the CDO 
which could provide an estimate for both d o (k) and d f (k) ; 2) design the SMPC strategy to 
deal with d s (k) and probabilistic constraints; 3) design the composite SMPC strategy which 
includes SMPC and the estimates provided by the CDO; and 4) establish sufﬁcient conditions 
to guarantee the recursive feasibility and the stability of the overall closed-loop system. 
Remark 1. The analysis of the complicated characteristics of the lumped disturbance is shown 
as: 1) the nonlinearities in the paper contains the unexpected nonlinear signals, modeled 
disturbances and stochastic disturbances, which is difﬁcult to deal with by only using the 
disturbance observer; 2) though the extended state observer (ESO) can deal with these complex 
disturbances, the ESO cannot obtain the accurate estimations of them when the information 
of the disturbances is limited. Therefore, in this paper, the nonlinearities is divided into three 
parts: the unexpected nonlinear signals, modeled disturbances and stochastic disturbances; 3) 
by this step, the nonlinear system is converted to the linear system, which simpliﬁes the 
system form and classiﬁes the disturbances ﬁnely. 
Remark 2. The modeled disturbance d o (t) represents the elastic disturbance introduced by 
the ﬂexible devices on spacecraft such as spacecraft antenna and solar remake [31] . The 
norm bounded disturbance d b (t) represents the Gravity-gradient torque, solar radiation, Earth- 
magnetic torque (all could be assumed bounded), and aerodynamic torque [32] . The stochastic 
noise d s (t) represents the actuator noise of the spacecraft [33] . 
5

## Page 6

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
3. The design of the CDO 
In this part, we aim at designing the CDO so as to estimate the modeled disturbance d o (k) 
and unmodeled disturbance d f (k) . In the CDO, to estimate d o (k) , we have 
⎧ 
⎨ 
⎩ 
 
w (k) = 
v w (k) + L w x(k ) , ˆ 
d o (k ) = V  
w (k) 
v w (k + 1) = 
(W −L w GV )( v w (k) + L w x(k)) 
−L w (Ax(k) + Bu(k)) −L w G ˆ 
d f (k) 
Meanwhile, to estimate d f (k) , we have 
⎧ 
⎨ 
⎩ 
ˆ 
d f (k) = 
v f (k) + L f x(k) 
v f (k + 1) = 
( I 3 ×3 −L f G )( v f (k) + L f x(k)) 
−L f (Ax(k) + Bu(k)) −L f GV  
w (k) 
where L w and L f are observer parameters to be designed; v w (k) and v f (k) are auxiliary 
variables. Denoting e w (k) = w(k) −ˆ 
w (k) and e f (k) = d f (k) −ˆ 
d f (k) , we have 
e w f (k + 1) = e w f (k) + ˜ 
η1 (k) 
(10) 
where e w f (k) = [ e T 
w (k) e T 
f (k)] T and 
 = 
 W −L w GV 
−L w G 
−L f GV 
I 3 ×3 −L f G 

˜ 
η1 (k) = 
 −L w Gd s (k) −L w GO(T 2 ) + H η(k) 
−L f Gd s (k) + (I 3 ×3 −L f G ) O(T 2 ) 

Remark 3. In the CDO, the modeled disturbance d o (k) is estimated by using information from 
the exogenious system. On the other hand, the unmodeled disturbance d f (k) is estimated by 
only requiring that ∥ d f (k + 1) −d f (k) ∥ 2 ≤δ f . The structure of the CDO suggests that it has 
the following merits: 1) The CDO is more suitable for the multi-source disturbance including 
both d o and d f . 2) In comparison with traditional DO dedicated to unmodeled disturbance, 
the CDO makes full use of the information of the disturbance. 3) In comparison with the DO 
dedicated to modeled disturbance, the CDO could handle a more general class of disturbances 
which are not necessarily described by the exogenious system. 4) The CDO could boil down 
to the traditional modeled (or unmodeled) DO if only one type of disturbance ( d o (k) or d f (k) ) 
needs to be estimated. 
Remark 4. The reasons why we present the CDO are given as: 1) in practical control systems, 
disturbances can destroy the performance of the systems and there are many forms of distur- 
bances such as modeled disturbances, unmodeled disturbances, and stochastic disturbances; 2) 
the existing disturbance observers usually can estimate only one form of disturbance, and it 
is difﬁcult for these disturbance observers to obtain accurate estimates of multi-source distur- 
bances; 3) the presented CDO can make use of the characteristics of the modeled disturbances 
and the unmodeled disturbances to estimate these two kinds of disturbances accurately. 
Remark 5. The novelty of the proposed CDO is summarized as: 1) the proposed CDO can not 
only estimate the modeled disturbances but also the norm bounded nonlinear signals, which 
is of great signiﬁcance in practical engineering; 2) the noise-to-state stability in probability 
of the CDO is guaranteed by the proposed sufﬁcient conditions which are novel and less 
conservative. 
6

## Page 7

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Remark 6. The analysis of the effects on the observer accuracy is shown as: 1) the proposed 
CDO can estimate the unexpected nonlinearities and the modeled disturbances separately, 
which is more accurate than only using the ESO to estimate the total nonlinearities directly; 
2) the CDO combines the advantages of both the ESO and the DO. In the proposed CDO, the 
estimation of the nonlinearities is considered into the estimation of the modeled disturbance. 
Similarly, the estimation of the modeled disturbance is also considered into the estimation of 
the nonlinearities. Through this design, the estimation accuracy is greatly improved. 
Remark 7. The reason why not estimate d s (k) is given as follows: by setting the bandwidth 
of the CDO high enough, the information of d s (k) can be included in the observer. In this 
case, not only the information of d s (k) will be included, but also more noise information will 
be included, which will lead to the decline of the observation accuracy. Therefore, the CDO 
is designed to get ˆ 
d o (k) and ˆ 
d f (k) but not the estimation of d s (k) . 
Before proceeding, the following deﬁnition is presented which is instrumental subsequently. 
Deﬁnition 1. Jiao et al. [35] System 10 is said to be noise-to-state stable (NSS) in probability 
if for any 0 < ε < 1 , there exist a class KL function ˜ 
τ2 (·) and a class K function ˜ 
ς 2 (·) such 
that for any e w f (0) , there holds 
Pr {∥ e w f ∥ 2 
2 ≤˜ 
ς 2 (·) + ˜ 
τ2 (·) } ≥1 −ϵ
In the following, we provide sufﬁcient conditions to guarantee that the error dynamics 
(10) is NSS in probability. 
Theorem 1. Consider error dynamics (10) . If there exist positive deﬁnite matrices P w and P f 
such that the following linear matrix inequality 
⎡ 
⎢ 
⎢ 
⎣ 
−
1 
1+ λ2 P w 
0 3 ×3 
P w W −Q w GV 
Q w G 
−
1 
1+ λ2 P f 
Q f GV 
P f −Q f G 
∗
−P w 
0 3 ×3 
∗
∗
−P f 
⎤ 
⎥ 
⎥ 
⎦ < 0 
(11) 
holds, where λ2 > 0, then system (10) is NSS in probability satisfying 
Pr 

∥ e w f (k) ∥ 2 
2 ≤ζ2 (e w f (0) , k) + θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

≥1 −ϵ2 
with 
ζ2 (e w f (0) , k) = λmax (P w f ) 
ϵ2 λmin (P w f ) 

1 −

1 −1 
ρ2 

ˆ 
α3 
λmax (P w f ) 
k 
× ∥ e w f ( 0) ∥ 2 
2 
θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) = τ3 λmax (P w f ) 
ϵ2 ˆ 
α3 λmin (P w f ) φ1 

∥ ˜ 
η1 (k) ∥ 2 
∞ 

φ1 

∥ ˜ 
η1 (k) ∥ 2 
∞ 

= 

1 + 1 
λ2 

∥ E { ˜ 
ηT 
1 (k) ˜ 
η1 (k) }∥ ∞ 
∥ E { ˜ 
ηT 
1 (k) ˜ 
η1 (k) }∥ ∞ = λmax (G T L T 
w L w G + G T L T 
f L f G ) ¯d 2 
s 
+ λmax (2G T L T 
w L w G + G T L T 
f L f G ) ˜ 
d 2 
s + 3 λmax (H T H ) ¯η2 
+ λmax (3 G T L T 
w L w G + 2(I 3 ×3 −L f G ) T (I 3 ×3 −L f G )) δ2 
f 
0 < ˆ 
α3 ≤min 

ς 3 , λmax (P w f ) 

, ρ2 > 1 , 0 < ϵ2 < 1 , τ3 = λmax (P w f ) 
ς 3 = λmin (P w f −(1 + λ2 )T P w f ) 
7

## Page 8

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Furthermore, we have L w = P −1 
w Q w and L f = P −1 
f Q f . 
Proof. Deﬁne P w f = 

P w 
0 3 ×3 
0 3 ×3 
P f 

where P w and P f are both positive deﬁnite matrices. 
Select the Lyapunov function V w f (k) = e T 
w f (k) P w f e w f (k) . It is easy to obtain 
E { V w f (k + 1) } −E { V w f (k) } 
= E 

e T 
w f (k)T P w f e w f (k) + ˜ 
ηT 
1 (k ) P w f ˜ 
η1 (k ) + e T 
w f (k)T P w f ˜ 
η1 (k) 
+ ˜ 
ηT 
1 (k) P w f e w f (k) 

−E { V w f (k) } 
(12) 
By Young’s inequality [34] , the following inequality 
e T 
w f (k)T P w f ˜ 
η1 (k) + ˜ 
ηT 
1 (k) P w f e w f (k) 
≤λ2 e T 
w f (k)T P w f e w f (k ) + 1 
λ2 
˜ 
ηT 
1 (k ) P w f ˜ 
η1 (k ) 
holds for any λ2 > 0. Then, we have 
E { V w f (k + 1) } −E { V w f (k) } 
≤E { e T 
w f (k)((1 + λ2 )T P w f  −P w f ) e w f (k) } + 

1 + 1 
λ2 

E { ˜ 
ηT 
1 (k ) P w f ˜ 
η1 (k ) } 
≤−ς 3 E {∥ e w f (k) ∥ 2 
2 } + τ3 φ1 

∥ ˜ 
η1 (k) ∥ 2 
∞ 

According to Schur complement, if (11) holds, we have (1 + λ2 )T P w f  −P w f < 0. Fur- 
thermore, based on (12) , we have 
E { V w f (k + 1) } −E { V w f (k) } 
≤−
ˆ 
α3 
λmax (P w f ) E 

V w f (k) 

+ τ3 φ1 

∥ ˜ 
η1 (k) ∥ 2 
∞ 

where 0 < ˆ 
α3 ≤min 

ς 3 , λmax (P w f ) 

. Thus, we have 
E { V w f (k + 1) } ≤

1 −
ˆ 
α3 
λmax (P w f ) 

E 

V w f (k) 

+ τ3 φ1 

∥ ˜ 
η1 (k) ∥ 2 
∞ 

(13) 
For any ρ2 > 1 , we deﬁne 
B = 

e w f (k) : E { V w f (k) } ≤θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

in which θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) = λmax (P w f ) ρ2 τ3 
ˆ 
α3 
φ1 

∥ ˜ 
η1 (k) ∥ 2 
∞ 

. In the following, we aim to prove 
that, for any positive scalar ϵ2 ∈ (0, 1) , there exist functions ζ2 ∈ KL and θ2 ∈ K [35] such 
that 
Pr 

∥ e w f (k) ∥ 2 
2 ≤ζ2 (e w f (0) , k) + θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ )) 

≥1 −ϵ2 
To begin with, we consider the two mutually exclusive cases: Case 1: e w f (0) ∈ B and Case 
2: e w f (0) / 
∈ B. For Case 1, it follows from e w f (0) ∈ B that 
E { V w f (k) } ≤θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) 
(14) 
If follows from (13) and (14) that 
E { V w f (1) } ≤

1 −
ˆ 
α3 
λmax (P w f ) 

E 

V w f (0) 

8

## Page 9

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
+ τ3 φ1 

∥ ˜ 
η1 (k) ∥ 2 
∞ 

< θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) 
In virtue of the mathematical induction, one has, for any k ∈ Z + , E { V w f (1) } ≤
θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) . Applying Chebyshev’s inequality yields 
Pr 
 
V w f (k) ≥1 
ϵ2 θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) 
 
≤
E { V w f (k) } ϵ2 
θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) ≤ϵ2 
It is easy to obtain 
Pr 

λmin (P w f ) ∥ e w f (k ) ∥ 2 
2 ≥1 
ϵ2 
θ∗
2 (ρ2 , ∥ ˜ 
η1 (k ) ∥ 2 
∞ ) 

≤Pr 

V w f (k) ≥1 
ϵ2 
θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

≤ϵ2 
which indicates 
Pr 

∥ e w f (k) ∥ 2 
2 ≤
1 
λmin (P w f ) ϵ2 
θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

≥1 −ϵ2 
Letting ρ2 → 1 + , we have, for any k ∈ Z + , 
Pr 

∥ e w f (k) ∥ 2 
2 ≤θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

≥1 −ϵ2 
(15) 
where θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) = τ3 λmax (P w f ) 
ϵ2 ˆ 
α3 λmin (P w f ) φ1 

∥ ˜ 
η1 (k) ∥ 2 
∞ 

. Therefore, for any ζ2 ∈ KL [35] , we have 
Pr 

∥ e w f (k) ∥ 2 
2 ≤θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

≤Pr 

∥ e w f (k) ∥ 2 
2 ≤ζ2 (e w f (0) , k) + θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

(16) 
According to (15) and (16) , Case 1 can be proven. For Case 2, we have E { V w f (0) } > 
θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) . In what follows, two subcases are considered: Subcase 2.1: E { V w f (k) } > 
θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) for all k ∈ Z + ; Subcase 2.2: E { V w f (k) } > θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) for all k ∈ 
[1 , k ∗−1] and E { V w f (k) } ≤θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) for k ≥k ∗where 
k ∗= min 

k : E { V w f (k) } ≤θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

If Subcase 2.1 holds, then we have 
τ3 φ1 

∥ ˜ 
η1 (k) ∥ 2 
∞ 

< 1 
ρ2 
ˆ 
α3 
λmax (P w f ) E { V w f (k) } 
(17) 
for all k ∈ Z + . Substituting (17) into (13) , we have 
E 

V w f (k + 1) 

−E 

V w f (k) 

≤
 1 
ρ2 
−1 

ˆ 
α3 
λmax (P w f ) E { V w f (k) } 
Noting that ρ2 > 1 and applying the standard comparison lemma in [36] , we conclude that 
there exists a function ˆ 
ζ2 ∈ KL such that E { V w f (k)) } ≤ˆ 
ζ2 (V w f (0)) , k) where 
ˆ 
ζ2 (V w f (0) , k) = 

1 −

1 −1 
ρ2 

ˆ 
α3 
λmax (P w f ) 
k 
E { V w f (0) } 
for all k ∈ Z + . Resorting to Chebyshev’s inequality again, we have 
Pr 

V w f (k) ≥1 
ϵ2 
ˆ 
ζ2 (V w f (0) , k) 

≤E { V w f (k) } ϵ2 
ˆ 
ζ2 (V w f (0) , k) 
≤ϵ2 
9

## Page 10

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
It is easy to obtain 
Pr 

λmin (P w f ) ∥ e w f (k) ∥ 2 
2 ≥1 
ϵ2 
ˆ 
ζ2 (V w f (0) , k) 

≤Pr 

V w f (k) ≥1 
ϵ2 
ˆ 
ζ2 (V w f (0) , k) 

Since ˆ 
ζ2 is a KL -function [35] , we have 
Pr 
 
λmin (P w f ) ∥ e w f (k) ∥ 2 
2 ≥
ˆ 
ζ2 (λmax (P w f ) ∥ e w f (0) ∥ 2 
2 , k) 
ϵ2 
 
≤Pr 

λmin (P w f ) ∥ e w f (k) ∥ 2 
2 ≥1 
ϵ2 
ˆ 
ζ2 (V w f (0) , k) 

Therefore, one has 
Pr 
 
∥ e w f (k) ∥ 2 
2 ≥
ˆ 
ζ2 (λmax (P w f ) ∥ e w f (0) ∥ 2 
2 , k) 
ϵ2 λmin (P w f ) 
 
≤ϵ2 
for all k ∈ Z + . Denote 
ζ2 (e w f (0) , k) = λmax (P w f ) 
ϵ2 λmin (P w f ) 

1 −

1 −1 
ρ2 

ˆ 
α3 
λmax (P w f ) 
k 
∥ e w f (0) ∥ 2 
2 
Then, we have Pr 

∥ e w f (k) ∥ 2 
2 ≤ζ2 (e w f (0) , k) 

≥1 −ϵ2 which further results in 
Pr 

∥ e w f (k) ∥ 2 
2 ≤ζ2 (e w f (0) , k) + θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

≥1 −ϵ2 
(18) 
for all k ∈ Z + . On the other hand, if Subcase 2.2 holds, then we have E { V w f (k) } > 
θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) for all k ∈ [0, k ∗−1] , which leads to 
Pr 

∥ e w f (k) ∥ 2 
2 ≤ζ2 (e w f (0) , k) 

≥1 −ϵ2 
(19) 
When k = k ∗, it is readily obtained from the deﬁnition of k ∗
that E { V w f (k ∗) } ≤
θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) which is followed immediately by E { V w f (k) } ≤θ∗
2 (ρ2 , ∥ ˜ 
η1 (k) ∥ 2 
∞ ) for any 
k ≥k ∗by following the same procedure as (14) . Repeating the proof process of Case 1, we 
have 
Pr 

sup 
k ≥k ∗∥ e w f (k) ∥ 2 
2 ≤θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

> 1 −ϵ2 
(20) 
Combining (19) with (20) indicates that, for all k ∈ Z + , we have 
Pr 

∥ e w f (k) ∥ 2 
2 ≤ζ2 (e w f (0) , k) + θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) 

≥1 −ϵ2 
(21) 
According to (18) and (21) , Case 2 can be proven. The proof is complete. □
Remark 8. In Theorem 3.1, the CDO gain can be obtained by solving the LMI (12). Further- 
more, the noise-to-state stability in probability of the estimation error is established. The The 
noise-to-state stability in probability is a kind of stability from time zero to inﬁnity, which 
inﬂects transient performance and steady performance. From Theorem 3.1, it is easy to ﬁnd 
the transient performance ζ2 (e w f (0) , k) and steady performance θ2 (∥ ˜ 
η1 (k) ∥ 2 
∞ ) . As k → + ∞ , 
the transient part ζ2 (e w f (0) , k) → 0. 
10

## Page 11

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Remark 9. Disturbance observers have been widely studied because of their excellent perfor- 
mance [10,11,40–43] . Compared with these studies, the novelty of the CDO is clariﬁed as: 1) 
the CDO can not only observe the estimates of disturbances generated by exogenous systems, 
but also enables to observe the estimate of unknown nonlinearities; 2) the noise-to-state in 
probability of the proposed CDO is less conservative. 
4. Composite stochastic model predictive control scheme 
In this section, we propose the C-SMPC scheme to generate the input signal for system 
(7) . In the ﬁrst subsection, the composite control strategy is presented, and the probabilistic 
constraints are reformulated as the deterministic constraints. In the second subsection, the 
SMPC part is designed to generate the optimal control signal ¯u ∗(k) by solving an optimization 
problem. Finally, the feasibility and stability of system (7) under the proposed composite 
strategy are analyzed. 
4.1. Reformulation of the probabilistic constraints 
Consider the following nominal system of (7) as 
¯x (k + 1) = A ¯x (k) + B ¯u (k) 
(22) 
where ¯x (k) is the nominal state and ¯u (k) is the nominal input. Furthermore, the C-SMPC 
strategy is designed as 
u(k) = ¯u (k) + ˜ 
e u (k) 
(23) 
˜ e u (k) = K (x(k) −¯x (k)) −ˆ 
d f (k) −ˆ 
d o (k) 
(24) 
where ¯u (k) = ¯u ∗(k ) if x(k ) / 
∈ X f , and ¯u (k ) = K ¯x (k ) if x(k ) ∈ X f . Note that ¯u ∗(k) is obtained 
by solving an optimization problem shown subsequently. K is the controller parameter and 
X f is the terminal region. From (23) and (24) , it is obvious that the input consists of the tube 
MPC part: ¯u (k) + K (x(k) −¯x (k)) and the disturbances rejection part: −ˆ 
d f (k) −ˆ 
d o (k) . Note 
that ¯u (k) = ¯u ∗(k) is calculated by solving an optimization problem when x(k) / 
∈ X f to move 
the state x(k) along a tube whose center is ¯x (k) , while K (x(k) −¯x (k)) is used to keep the 
state x(k) within this tube. 
We rewrite system (7) as 
x(k) = ¯x (k) + ˜ 
e x (k) 
(25) 
˜ e x (k + 1) = A ˜ e x (k) + BK (x(k) −¯x (k)) + Be f (k) 
+ BVe w (k) + Gd s (k) + GO(T 2 ) 
(26) 
where ˜ e x (0) = 0 6 ×1 . According to (23) and (25) , we have E { x(k) } = ¯x (k) + E { ˜ e x (k) } 
and E { u(k) } = ¯u (k) + E { ˜ e u (k) } which implies x(k) −E { x(k) } = x(k) −¯x (k) −E { ˜ e x (k) } and 
u(k) −E { u(k) } = u(k) −¯u (k) −E { ˜ e u (k) } . Then, we have 
E 

(x(k) −E { x(k) } )(x(k) −E { x(k) } ) T 
= E 

(x(k) −¯x (k))(x(k) −¯x (k)) T 
−E { ˜ 
e x (k) } E 

˜ 
e T 
x (k) 

(27) 
11

## Page 12

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
E 

(u(k) −E { u(k) } )(u(k) −E { u(k) } ) T 
= E 

(u(k) −¯u (k))(u(k) −¯u (k)) T 
−E { ˜ e u (k) } E 

˜ e T 
u (k) 

(28) 
Deﬁning μx (k) = x(k) −¯x (k) , we have μx (k + 1) = x μx (k) + Ge f (k) + GVe w (k) + 
Gd s (k) + GO(T 2 ) with x = A + BK . Similarly, we have 
E { μx (k + 1) μT 
x (k + 1) } 
≤(1 + ˜ λ1 + ˜ λ2 + ˜ λ3 + ˜ λ4 )x E { μx (k) μT 
x (k) } T 
x 
+ G E { d s (k) d T 
s (k) } G T + (3 + 1 / ˜ λ4 ) ˜ 
d 2 
s GG T + (4 + 1 / ˜ λ3 ) δ2 
f GG T 
+ (4 + 1 / ˜ λ1 ) ∥ e w f (k) ∥ 2 
2 GG T + (4 + 1 / ˜ λ2 ) ∥ e w f (k) ∥ 2 
2 GV V T G T 
where 
E { d s (k) d T 
s (k) } = 
⎡ 
⎢ 
⎣ 
˘d s, 1 + ˜ 
d 2 
s, 1 
˜ 
d s, 1 ˜ 
d s, 2 
˜ 
d s, 1 ˜ 
d s, 3 
˜ 
d s, 2 ˜ 
d s, 1 
˘d s, 2 + ˜ 
d 2 
s, 2 
˜ 
d s, 2 ˜ 
d s, 3 
˜ 
d s, 3 ˜ 
d s, 1 
˜ 
d s, 3 ˜ 
d s, 2 
˘d s, 3 + ˜ 
d 2 
s, 3 
⎤ 
⎥ 
⎦ 
and ˜ λ1 > 0, ˜ λ2 > 0, ˜ λ2 > 0, ˜ λ4 > 0 are constants satisfying 
λ

(1 + ˜ λ1 + ˜ λ2 + ˜ λ3 + ˜ λ4 ) 0. 5 x 
 
∈ (−1 , 1) 
Denoting 
ˆ 
x (k + 1) = (1 + ˜ λ1 + ˜ λ2 + ˜ λ3 + ˜ λ4 )x E { μx (k) μT 
x (k) } T 
x 
+ G E { d s (k) d T 
s (k) } G T + (4 + 1 / ˜ λ1 ) ∥ e w f (k) ∥ 2 
2 GG T 
+ (4 + 1 / ˜ λ2 ) ∥ e w f (k) ∥ 2 
2 GV V T G T + (4 + 1 / ˜ λ3 ) δ2 
f GG T 
+ (3 + 1 / ˜ λ4 ) ˜ 
d 2 
s GG T + (4 + 1 / ˜ λ3 ) δ2 
f GG T + (4 + 1 / ˜ λ3 ) δ2 
f GG T 
with ˆ 
x (0) = 0 6 ×6 , we have E 

μx (k) μT 
x (k) 

≤ˆ 
x (k) which is 
E 

(x(k) −¯x (k))(x(k) −¯x (k)) T 
= E 

μx (k) μT 
x (k) 

≤ˆ 
x (k) 
From (27) , we have 
E 

(x(k) −E { x(k) } )(x(k) −E { x(k) } ) T 
≤ˆ 
x (k) −E { ˜ e x (k) } E 

˜ e T 
x (k) 

(29) 
It follows from (26) that E { ˜ e x (k) } =  k 
i=0 (A + BK ) i−1 ˜ 
ω x (i) with 
˜ 
ω x (k) = Be f (k) + BVe w (k) + G ˜ 
d s + GO(T 2 ) 
= ˜ 
B 1 e w f (k) + G ˜ 
d s + GO(T 2 ) 
˜ 
B 1 = [ BV B] 
Furthermore, we have 
E { (u(k) −¯u (k))(u(k) −¯u (k)) T } 
≤3 K ˆ 
x (k) K T + 6 ¯d 2 
f I 3 ×3 + 6 ∥ e w f (k) ∥ 2 
2 I 3 ×3 
12

## Page 13

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
+ 6 ∥ e w f (k) ∥ 2 
2 V V T + 6 ¯w 2 V V T 
Denoting 
ˆ 
u (k) = 3 K ˆ 
x (k) K T + 6 ¯d 2 
f I 3 ×3 + 6 ∥ e w f (k) ∥ 2 
2 I 3 ×3 
+ 6 ∥ e w f (k) ∥ 2 
2 V V T + 6 ¯w 2 V V T 
we have E { (u(k) −¯u (k))(u(k) −¯u (k)) T } ≤ˆ 
u (k) . According to (28) , we have 
E 

(u(k) −E { u(k) } )(u(k) −E { u(k) } ) T 
≤ˆ 
u (k) −E { ˜ 
e u (k) } E 

˜ e T 
u (k) 

(30) 
From the above steps, inequalities (29) and (30) are obtained. By these inequalities, proba- 
bilistic constraints (8) and (9) can be reformulated as deterministic constraints in the following 
lemma. 
Lemma 1. Consider system (7) with the probabilistic constraints (8) and (9) . The probabilistic 
constraints (8) and (9) can be reformulated as 
b T 
x ¯x (k) ≤h x −((1 −l x ) 
! 
1 /l x + 
! 
l x ) 
 
b T 
x ˆ 
x (k) b x 
(31a) 
b T 
u ¯u (k) ≤h u −((1 −l u ) 
! 
1 /l u + 
! 
l u ) 
 
b T 
u ˆ 
u (k) b u 
(31b) 
Proof. Denote X (k) = E 

(x(k) −E { x (k) } )(x (k) −E { x(k) } ) T 
. According to Cantelli’s in- 
equality [37] , we have 
Pr { b T 
x x(k) ≥h x } ≤Pr { b T 
x x(k) ≥b T 
x E { x(k) } + } ≤
b T 
x X (k) b x 
b T 
x X (k) b x + 2 
(32) 
Based on (29) and (32) , we have 
Pr { b T 
x x(k) ≥h x } ≤Pr 

b T 
x x(k) ≥
b T 
x X (k) b x 
b T 
x X (k) b x + 2 

≤
b T 
x 

ˆ 
x (k) −E { ˜ e (k) } E 

˜ e T (k) 
 
b x 
b T 
x 

ˆ 
x (k) −E { ˜ e (k) } E 

˜ e T (k) 
 
b x + 2 
If  ≥
 
b T 
x ( ˆ 
x (k) −E { ˜ e (k) } E 

˜ e T (k) 

) b x 
√ (1 −l x ) / l x holds, (8) holds. It follows from 
b T 
x E { x(k) } ≤h x − that 
b T 
x E { x(k) } ≤h x −
 
b T 
x ( ˆ 
x (k) −E { ˜ e (k) } E 

˜ e T (k) 

) b x 
! 
(1 −l x ) / l x 
which implies 
b T 
x ¯x (k) ≤−
 
b T 
x ( ˆ 
x (k) −E { ˜ e (k) } E 

˜ e T (k) 

) b x 
! 
(1 −l x ) / l x 
+ h x −b T 
x E { ˜ e (k) } 
Deﬁne the function 
F (b T 
x E { ˜ e (k) } ) = −
 
b T 
x ( ˆ 
x (k) −E { ˜ e (k) } E 

˜ e T (k) 

) b x 
! 
(1 −l x ) / l x 
13

## Page 14

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
−b T 
x E { ˜ e (k) } 
(33) 
For simplicity, we deﬁne a = b T 
x E { ˜ e (k) } , b = b T 
x ˆ 
x (k) b x and c = √ (1 −l x ) /l x . Then, (33) can 
be reformulated as F (a) = −c 
√ 
b −a 2 −a. It is easy to see that the function F (a) = 
−c 
√ 
b −a 2 −a achieves the minimum at a = 
! 
b/ (c 2 + 1) with the minimal value h x −((1 −
l x ) √ 1 /l x + √ l x ) 
 
b T 
x ˆ 
x (k) b x . Therefore, we have 
b T 
x ¯x (k) ≤h x −((1 −l x ) 
! 
1 /l x + 
! 
l x ) 
 
b T 
x ˆ 
x (k) b x 
≤−
 
b T 
x ( ˆ 
x (k) −E { ˜ e (k) } E 

˜ e T (k) 

) b x 
! 
(1 −l x ) / l x 
+ h x −b T 
x E { ˜ e (k) } 
Similarly, we have 
b T 
u ¯u (k) ≤h u −((1 −l u ) 
! 
1 /l u + 
! 
l u ) 
 
b T 
u ˆ 
u (k) b u 
≤−
 
b T 
u ( ˆ 
u (k) −E { e u (k) } E 

e T 
u (k) 

) b u 
! 
(1 −l u ) / l u 
+ h u −b T 
u E { e u (k) } 
The proof is complete. □
Remark 10. In Lemma 4.1, the probabilistic constraints (8) and (9) are reformulated as the 
deterministic constraints (31a) and (31b) , respectively. By substituting (31a) and (31b) with 
(8) and (9) in the optimization problem, we can obtain the optimal feedback input signal. 
Remark 11. The reasons why we present the MPC are given as: 1) state and input constraints 
exist widely in control systems, and MPC can handle these constraints effectively; 2) MPC 
is an optimization algorithm, which can help the system to achieve good performance. 
4.2. Stochastic model predictive control scheme 
In this subsection, the SMPC scheme is designed to generate input signal for the system 
(7) . Based on the knowledge (e.g., measurements or estimates) available at time k, the optimal 
input signal ¯u ∗(k) is calculated. The cost function to be minimized is 
J ( ¯x (k) , ¯u (k)) = 
N−1 
" 
i=0 

∥ ¯x (k + i| k) ∥ 2 
Q + ∥ ¯u (k + i| k) ∥ 2 
R 

+ ∥ ¯x (k + N | k) ∥ 2 
P 
(34) 
where ¯x (k + i| k) is the predicted state which is also the nominal state with ¯x (k | k ) = ¯x (k) ; 
¯u (k + i| k) is the predicted input which is also the input of the nominal system; N ∈ Z + 
is the prediction horizon; Q > 0, R > 0 and P > 0 are weighting matrices with appropriate 
dimensions. 
To guarantee recursive feasibility and stability, some terminal constraints must be consid- 
ered. In this paper, the terminal constraints are given by 
¯x (k + N ) ∈ X f 
(35a) 
14

## Page 15

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
ˆ 
x (k + N ) ≤¯xx 
(35b) 
where X f is a positively invariant set to be designed such that we have 
(A + BK ) ¯x ∈ X f , ∀ ¯x ∈ X f 
(36) 
Note that ¯xx is obtained by solving the following Lyapunov equation: 
¯xx = E 

μx μT 
x 

= (1 + ˜ λ1 + ˜ λ2 + ˜ λ3 + ˜ λ4 )x E { μx μT 
x } T 
x 
+ G E { d s (k) d T 
s (k) } G T + (4 + 1 / ˜ λ1 ) ∥ e w f (k) ∥ 2 
2 GG T 
+ (4 + 1 / ˜ λ2 ) ∥ e w f (k) ∥ 2 
2 GV V T G T 
+ (4 + 1 / ˜ λ3 ) δ2 
f GG T + (3 + 1 / ˜ λ4 ) ˜ 
d 2 
s GG T 
(37) 
¯uu = 3 K ¯xx K T + 6 ¯d 2 
f I 3 ×3 + 6 ∥ e w f (k) ∥ 2 
2 I 3 ×3 
+ 6 ∥ e w f (k) ∥ 2 
2 V V T + 6 ¯w 2 V V T 
In addition, according to (31), the following conditions should be satisﬁed 
b T 
x ¯x (k + N ) ≤h x −((1 −l x ) 
! 
1 /l x + 
! 
l x ) 
 
b T 
x ¯xx b x 
(38a) 
b T 
u ¯u (k + N ) ≤h u −((1 −l u ) 
! 
1 /l u + 
! 
l u ) 
 
b T 
u ¯uu b u 
(38b) 
for all ¯x ∈ X f . Considering these terminal constraints as well as constraints (31a) and (31b) , 
the SMPC problem is formulated as follows: 
Problem 1 : ¯u ∗(k + i| k) = arg min ¯u (k + i| k ) J ( ¯x (k + i| k) , ¯u (k + i| k)) subject to 
¯x (k + i + 1 | k) = A ¯x (k + i| k) + B ¯u (k + i| k) 
(39a) 
b T 
x ¯x (k + i| k) ≤h x −((1 −l x ) 
! 
1 /l x + 
! 
l x ) 
 
b T 
x ˆ 
x (k + i| k) b x 
(39b) 
b T 
u ¯u (k + i| k) ≤h u −((1 −l u ) 
! 
1 /l u + 
! 
l u ) 
 
b T 
u ˆ 
u (k + i| k) b u 
(39c) 
¯x (k + N | k) ∈ X f 
(39d) 
ˆ 
x (k + N | k) ≤¯xx 
(39e) 
In the following lemma, we provide sufﬁcient conditions to derive controller parameter K 
and guarantee that the terminal region X f is an invariant region for system (7) . 
Lemma 2. If ξx ≥λ1 / 2 
max (P)(∥ ˜ 
B 1 ∥ 2 ∥ e w f (0) ∥ 2 + ∥ G ∥ 2 ¯d s + ∥ G ∥ 2 δ f ) 
λmin ( ˆ 
Q p ) 
and 
⎡ 
⎢ 
⎢ 
⎣ 
−
A T + ϒB T 
ϒ

−
0 6 ×3 
0 6 ×6 
∗
−R −1 
0 3 ×6 
∗
∗
−Q −1 
⎤ 
⎥ 
⎥ 
⎦ < 0 
(40) 
15

## Page 16

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
hold at the same time, where  = P −1 , ϒ = K T , ˆ 
Q p = P −1 / 2 (Q + K T RK ) P −1 / 2 , ˜ 
B 1 = 
[ BV B] , then we have K = ϒT −1 and the terminal region X f = 

x (k) : x T (k) P x (k) ≤ξ 2 
x 

is an invariant region for system (7) , that is, x(k) will not depart from X f once x(k) enters 
X f . 
Proof. Consider the case where the states of system (7) have been driven into the terminal 
region X f under the input (23) , i.e., 
X f = 

x(k) : x T (k) P x(k) ≤ξ 2 
x 

, ξx > 0 
According to (23) , ¯u (k) = K ¯x (k) is applied so that u(k) = K ¯x (k) + K (x(k) −¯x (k)) −
ˆ 
d f (k) −ˆ 
d o (k) = K x(k) −ˆ 
d f (k) −ˆ 
d o (k) will be used once x(k) enters the terminal region 
X f . It is easy to obtain the closed-loop system x(k + 1) = x x(k) + ω x (k) with ω x (k) = 
Ge f (k) + GVe w (k) + Gd s (k) + GO(T 2 ) . 
Select the Lyapunov function as ˜ 
V (k) = x T (k ) P x(k ) where P is a positive deﬁnite matrix 
which is also used as the penalty matrix in the cost function (34) . We have ˜ 
V (k + 1) −˜ 
V (k) = 
x T (k)(T 
x P x −P ) x(k) + 2x T P ω x (k) . According to Schur complement, if (40) holds, we 
have T 
x P x −P ≤−Q −K T RK . Furthermore, we have 
˜ 
V (k + 1) −˜ 
V (k) ≤−x T (k)(Q + K T RK ) x(k) + 2x T P ω x (k) 
≤−x T (k)(Q + K T RK ) x(k) 
×
# 
1 −
! 
ω T 
x (k) P ω x (k) 
λmin ( ˆ 
Q p ) 
! 
x T (k) P x(k) 
$ 
where ˆ 
Q p = P −1 / 2 (Q + K T RK ) P −1 / 2 . Therefore, ˜ 
V (k + 1) ≤˜ 
V (k) holds if 
 
ω T 
x (k) P ω x (k) ≤λmin ( ˆ 
Q p ) 
! 
x T (k) P x(k) ≤λmin ( ˆ 
Q p ) ξx 
(41) 
On the other hand, we have 
 
ω T 
x (k) P ω x (k) ≤λ1 / 2 
max (P ) ∥ ω x (k) ∥ 2 
≤λ1 / 2 
max (P )(∥ ˜ 
B 1 ∥ 2 ∥ e w f (0) ∥ 2 + ∥ G ∥ 2 ¯d s + ∥ G ∥ 2 δ f ) 
If λ1 / 2 
max (P)(∥ ˜ 
B 1 ∥ 2 ∥ e w f (0) ∥ 2 + ∥ G ∥ 2 ¯d s + ∥ G ∥ 2 δ f ) 
λmin ( ˆ 
Q p ) 
holds for all k ∈ Z + , then x(k) will not depart from X f 
once x(k) enters the terminal region X f . The proof is complete. □
Remark 12. In Lemma 4.2, we give the invariant region of the SMPC scheme and the 
controller gain K . The invariant region X f suggests that x(k) will not depart from X f once 
x(k) enters X f . 
Remark 13. The advantages of the SMPC are shown as: 1) it is guaranteed that the constraints 
with random parameters can be satisﬁed with a certain probability on the optimal value; 2) 
compared with the robust model predictive control, the SMPC can deal with stochastic system 
parameters and stochastic uncertainties which are unbounded. 
4.3. Feasibility and stability analysis 
In the part, we provide the sufﬁcient conditions to guarantee the recursive feasibility and 
closed-loop stability of system (7) under the input (23) . 
16

## Page 17

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Theorem 2. If there exists a solution to Problem 1 at k = 0, then it is recursively feasible 
and the probabilistic constraints (8) and (9) are satisﬁed for all k ∈ Z + ∪ { 0} . Furthermore, 
the system (7) under the input (23) is exponentially ultimately bounded in the mean square 
sense [38] , i.e., E {∥ x(k) ∥ 2 
2 } ≤˜ 
ζ3 (x(0) , k) + ˜ 
θ3 where 
˜ 
ζ3 (x(0) , k) = 2 
β1 

1 −λmin (Q) 
β2 
k 
J ( ¯x ∗(0) , ¯u ∗(0)) 
˜ 
θ3 = 2(1 −β) −2 
N 
" 
i=0 
N 
" 
j=0 

˜ 
ω T 
1 x (i)(T 
x ) i−1 j−1 
x 
˜ 
ω 1 x ( j) 
+ ˜ 
ω T 
1 x (i)(T 
x ) i−1 j−1 
x G ˜ 
d s + ˜ 
d T 
s G T (T 
x ) i−1 (x ) j−1 ˜ 
ω T 
1 x ( j) 
 
+ 2(1 −β) −2 
N 
" 
i=0 
λmax (G T (T 
x ) i−1 i−1 
x G ) ¯d 2 
s 
+ 2(1 −β) −2 
N 
" 
i=0 
N 
" 
j =0,j ̸ = i 
˜ 
d T 
s G T (T 
x ) i−1 j−1 
x G ˜ 
d s 
˜ 
ω 1 x (k) = ˜ 
ω x (k) −G ˜ 
d s , ˜ 
ω x (k) = ˜ 
B 1 e w f (k) + G ˜ 
d s + GO(T 2 ) 
˜ 
B 1 = [ BV B] 
with ∀ β2 > λmin (Q) and β2 > β1 > 0. 
Proof. To begin with, we aim to prove the recursive feasibility of Problem 1. Assume that 
there exists a solution to Problem 1 at time k with the optimal input sequence { ¯u ∗(k | k ) , ¯u ∗(k + 
1 | k) , . . . , ¯u ∗(k + N −1 | k) } . Consider the following feasible control sequence as u f e (s| k + 
1) = ¯u ∗(s| k) for s ∈ [ k + 1 , k + N ) and u f e (s| k + 1) = K ¯x ∗(s| k) for s ∈ [ k + N, k + N + 1) . 
Because ¯u ∗(s| k ) , k ∈ [ k , k + N −1] is the solution to Problem 1, constraint (31a) is veriﬁed 
for all ¯x (s| k) for s ∈ [ k, k + N −1] . 
At time k + 1 , if the feasible control input u f e (s| k + 1) is used by system (7) , then con- 
straint (31a) naturally holds for s ∈ [ k + 1 , k + N −1] . For s = k + N , in view of (35a), 
(35b) and (38a) , we have b T 
x ¯x (k + N | k) ≤h x −((1 −l x ) √ 1 /l x + √ l x ) 
 
b T 
x ˆ 
x (k + N | k) b x 
such that constraint (31a) is veriﬁed for s ∈ [ k + 1 , k + N ] . Similarly, constraint (31b) is ver- 
iﬁed for all ¯u (s| k) for s ∈ [ k, k + N −1] at time k. Furthermore, in view of (35a), (35b) and 
(38b) , we have b T 
u K ¯x (k + N | k) ≤h u −((1 −l u ) √ 1 /l u + √ l u ) 
 
b T 
u ˆ 
u (k + N | k) b u such that 
constraint (31b) is veriﬁed for s ∈ [ k + 1 , k + N ] . According to (35a) and the invariant 
property (36) , we have ¯x (k + 1 + N | k) = x ¯x (k + N | k) ∈ X f . Furthermore, it follows from 
(35b) and (37) that 
ˆ 
x (k + N + 1 | k) 
≤(1 + ˜ λ1 + ˜ λ2 + ˜ λ3 + ˜ λ4 )x E { μx μT 
x } T 
x 
+ (4 + 1 / ˜ λ1 ) ∥ e w f (k + N −1) ∥ 2 
2 GG T + G E { d s (k ) d T 
s (k ) } G T 
+ (4 + 1 / ˜ λ2 ) ∥ e w f (k + N −1) ∥ 2 
2 GV V T G T 
+ (4 + 1 / ˜ λ3 ) δ2 
f GG T + (3 + 1 / ˜ λ4 ) ˜ 
d 2 
s GG T = ¯xx 
17

## Page 18

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Hence, the constraints (35a) and (35b) are both veriﬁed at time k + 1 . This completes the 
proof of recursive feasibility. 
Secondly, the stability of system (7) is shown. We ﬁrst prove that the nominal system 
converges to the origin. Then, we show the state of system (7) converges to an invariant set 
along a trajectory lying in the tube, whose center is the trajectory of the nominal system. 
Select the Lyapunov function for the nominal system as V (k) = J ( ¯x ∗(k ) , ¯u ∗(k )) . Then, we 
have 
J (x f e (k + 1) , u f e (k + 1)) −J ( ¯x ∗(k) , ¯u ∗(k)) 
= x T 
f e (k + N | k) 

Q + K T RK + T 
x P x −P 

x f e (k + N | k) 
−∥ ¯x ∗(k | k ) ∥ 2 
Q −∥ ¯u ∗(k | k ) ∥ 2 
R 
where x f e represents the feasible state. According to (40) in Lemma 2 , we have 
J (x f e (k + 1) , u f e (k + 1)) −J ( ¯x ∗(k) , ¯u ∗(k)) 
≤−∥ ¯x ∗(k | k ) ∥ 2 
Q −∥ ¯u ∗(k | k ) ∥ 2 
R 
According to the principle of optimality, we have J ( ¯x ∗(k + 1) , ¯u ∗(k + 1)) ≤J (x f e (k + 
1) , u f e (k + 1)) . Therefore, we have 
V (k + 1) −V (k) = J ( ¯x ∗(k + 1) , ¯u ∗(k + 1)) −J ( ¯x ∗(k) , ¯u ∗(k)) 
≤−∥ ¯x ∗(k | k ) ∥ 2 
Q −∥ ¯u ∗(k | k ) ∥ 2 
R 
which implies 
∞ 
" 
k=0 
(∥ ¯x ∗(k | k ) ∥ 2 
Q + ∥ ¯u ∗(k | k ) ∥ 2 
R ) ≤J ( ¯x ∗(0) , ¯u ∗(0)) −lim 
k→∞ J ( ¯x ∗(k ) , ¯u ∗(k )) 
In other words, we have lim k→∞ (∥ ¯x ∗(k | k ) ∥ 2 
Q + ∥ ¯u ∗(k | k ) ∥ 2 
R ) = 0, that is, the state of the 
nominal system asymptotically converges to the origin. Therefore, we have β1 ∥ ¯x ∗(k) ∥ 2 
2 ≤
J ( ¯x ∗(k) , ¯u ∗(k)) ≤β2 ∥ ¯x ∗(k) ∥ 2 
2 with β2 > β1 > 0. Because V (k + 1) −V (k) ≤−∥ ¯x ∗(k | k ) ∥ 2 
Q −
∥ ¯u ∗(k | k ) ∥ 2 
R , we have 
V (k + 1) −V (k) ≤−∥ ¯x ∗(k | k ) ∥ 2 
Q 
which indicates V (k + 1) ≤

1 −λmin (Q) 
β2 
 
V (k) . Selecting β2 > λmin (Q) , we have V (k) ≤

1 −λmin (Q) 
β2 
 k 
V (0) . From 
β1 ∥ ¯x ∗(k) ∥ 2 
2 ≤J ( ¯x ∗(k) , ¯u ∗(k)) ≤β2 ∥ ¯x ∗(k) ∥ 2 
2 
we have ∥ ¯x ∗(k) ∥ 2 
2 ≤
1 
β1 

1 −λmin (Q) 
β2 
 k 
J ( ¯x ∗(0) , ¯u ∗(0)) . Note that the input ¯u ∗(k) generated by 
the SMPC scheme is also the input used in the nominal system. Therefore, we have ¯x ∗(k) = 
¯x (k) . 
In what follows, we will show that the state of system (7) converges to an invariant set 
along a trajectory lying in the tube, whose center is the trajectory of the nominal system. 
From (25) , we have x(k) = ¯x (k) + ˜ e x (k) . It is easy to ﬁnd that ¯x (k) is center of the tube 
system while ˜ e x (k) is the ‘radius’ that state x(k) departs from the center ¯x (k) . Next, the 
convergence of x(k) is shown. Introduce a set W where ˜ 
ω x (k) −G ˜ 
d s + Gd s (k) = ω 1 (k) ∈ 
18

## Page 19

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
W with ˜ 
ω x (k) = ˜ 
B 1 e w f (k) + G ˜ 
d s + GO(T 2 ) and ˜ 
B 1 = [ BV B] . Furthermore, there exists a 
constant β = λmax (N 
x ) such that N 
x ω 1 (k) ∈ βW , ∀ ω 1 (k) ∈ W . It is easy to have 
˜ e x (∞ ) = ˜ 
e x (N ) + 
∞ 
" 
i= N+1 
i−1 
x ω 1 (i) 
= ˜ 
e x (N ) + N 
x ω 1 (N + 1) + x × N 
x ω 1 (N + 2) + · · ·
≤˜ 
e x (N ) + βω 1 (N + 1) + βx ω 1 (N + 2) + · · ·
= ˜ 
e (N ) + β ˜ 
e (∞ ) 
which implies ˜ e x (∞ ) ≤(1 −β) −1 ˜ e x (N ) . Subsequently, one has 
˜ e T 
x (∞ ) ˜ e x (∞ ) ≤(1 −β) −2 ˜ 
e T 
x (N ) ˜ e x (N ) 
≤(1 −β) −2 
N 
" 
i=0 
N 
" 
j=0 

ω T 
1 (i)(T 
x ) i−1 j−1 
x ω 1 ( j) 

Denoting ω 1 x (k) = ˜ 
ω x (k) −G ˜ 
d s where ˜ 
ω x (k) = ˜ 
B 1 e w f (k) + G ˜ 
d s + GO(T 2 ) and ˜ 
B 1 = [ BV B] 
yields ω 1 (k) = ω 1 x (k) + Gd s (k) . Then, we have 
E {∥ ˜ e x (∞ ) ∥ 2 
2 } ≤(1 −β) −2 
N 
" 
i=0 
N 
" 
j=0 

˜ 
ω T 
1 x (i)(T 
x ) i−1 j−1 
x 
˜ 
ω 1 x ( j) 
+ ˜ 
ω T 
1 x (i)(T 
x ) i−1 j−1 
x G ˜ 
d s + ˜ 
d T 
s G T (T 
x ) i−1 j−1 
x 
˜ 
ω T 
1 x ( j) 
 
+ (1 −β) −2 
N 
" 
i=0 
λmax (G T (T 
x ) i−1 i−1 
x G ) ¯d 2 
s 
+ (1 −β) −2 
N 
" 
i=0 
N 
" 
j =0,j ̸ = i 
˜ 
d T 
s G T (T 
x ) i−1 j−1 
x G ˜ 
d s 
According to (25) , we have 
x T (k) x(k) = ¯x T (k) ¯x (k) + ¯x T (k) ˜ e x (k) + ˜ 
e T 
x (k) ¯x (k) + ˜ e T (k) ˜ e (k) 
≤2 ¯x T (k) ¯x (k) + 2 ˜ e T 
x (∞ ) ˜ e x (∞ ) 
which implies 
E {∥ x(k) ∥ 2 
2 } ≤2∥ ¯x (k) ∥ 2 
2 + 2E {∥ ˜ e x (∞ ) ∥ 2 
2 } = ˜ 
ζ3 (x(0) , k) + ˜ 
θ3 
Therefore, system (7) is exponentially bounded in the mean square sense. The proof is 
complete. □
Remark 14. In Theorem 4.3, the recursive feasibility of the SMPC scheme and the exponen- 
tial boundedness in the mean square sense for system are proved. The exponential boundedness 
in the mean square sense contains the transient performance ˜ 
ζ3 (x(0) , k) and steady perfor- 
mance ˜ 
θ3 . As k → + ∞ , the transient performance ˜ 
ζ3 (x(0) , k) → 0 and E {∥ x(+ ∞ ) ∥ 2 
2 } ≤˜ 
θ3 , 
which suggests that E {∥ x(+ ∞ ) ∥ 2 
2 } converges to a bounded region. 
Remark 15. In this paper, we prove the NSS in probability of the CDO and the mean square 
stability of the closed-loop system separately due mainly to the separation principle. The 
proof of the separation principle can be easily got and it is omitted here. 
19

## Page 20

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Remark 16. In this paper, we propose the C-SMPC method to deal with modeled/unmodeled 
disturbances and state/input constraints for control systems. Though composite-disturbance- 
observer based controllers have been widely studied [40–43] , our paper has the following 
contributions: 1) the proposed C-SMPC can not only deal with multi-source disturbances, but 
also state and input constraints, which is meaningful in practice; 2) the NSS in probability 
is established for the proposed CDO; 3) sufﬁcient conditions are provided to guarantee the 
recursive feasibility and the mean square stability of the closed-loop system under C-SMPC. 
Remark 17. Though the results only give the case of the linear case, the results are still 
applicable to some nonlinear cases. For example, when the nonlinear part of the nonlinear 
system is differentiable and its derivative is bounded, the results of this paper are applicable. 
In this case, the nonlinear part can be extended as a new state such that the whole nonlinear 
system can be translated as a linear system. Then, we can design an extended state observer 
(ESO) to get the estimate of this linear system. By this step, we can use the similar procedure 
of this paper to deal with the obtained linear system and obtain similar results of this paper. 
5. Numerical example 
In this section, a numerical example on the attitude control of the spacecraft is provided 
to validate the proposed method [39] . The inertia matrix and the sampling period are selected 
as J s/c = diag { 17 , 12, 9 } and T = 0. 1s , respectively. The matrices of the exogenous system 
are given by 
˜ 
W = 
⎡ 
⎣ 
9 
0 
0 
0 
9 . 7 
0 
0 
0 
9 . 8 
⎤ 
⎦ , ˜ 
H = 
⎡ 
⎣ 
100 
0 
0 
0 
0 
0 
0 
100 
0 
0 
0 
0 
0 
0 
100 
0 
0 
0 
⎤ 
⎦ 
˜ 
V = 
⎡ 
⎣ 
1 
0 
0 
0 
1 
0 
0 
0 
1 
⎤ 
⎦ 
The distribution function for each component d s,i is obtained by truncating a normal 
distribution whose mean is ˜ 
d s,i = 0 and variance is ˘d s,i = 0. 25 . Set ¯d s,i = 0. 1 , ¯d b = 0. 1 , 
¯d f = 2, and ¯w = 2. 5 . The parameters of the probabilistic constraints are given by b x = 
0. 01 × [1 1 1 1 1 1] T , b u = 0. 01 × [1 1 1] T , h x = 10, h u = 10, l x = 0. 5 and l u = 0. 5 . By 
solving (11) , the parameters of the CDO are given as 
L w = 
⎡ 
⎣ 
0 
0 
0 
4. 3680 
0 
0 
0 
0 
0 
0 
4. 3680 
0 
0 
0 
0 
0 
0 
4. 3680 
⎤ 
⎦ 
L f = 
⎡ 
⎣ 
0 
0 
0 
5 . 1458 
0 
0 
0 
0 
0 
0 
5 . 0748 
0 
0 
0 
0 
0 
0 
5 . 0303 
⎤ 
⎦ 
By solving (40) , the controller parameter is obtained as K = [ −0. 1379 I 3 ×3 −0. 7787 I 3 ×3 ] . 
Furthermore, according to Lemma 2 , the terminal region is obtained as X f = { x(k) : 
x (k) T P x (k) ≤ξ 2 
x } with ξx = 0. 0092. The rest parameters are given as δ f = 0. 1 , λ1 = 
0. 5 , ˜ λ1 = ˜ λ2 = ˜ λ3 = ˜ λ4 = 0. 0034. Select the initial states as [1 5 −2 0. 5 0. 1 −0. 3] T . 
20

## Page 21

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Fig. 1. The state x CDO (k) of system (7) with the CDO. 
Fig. 2. The relative error e CDO (k) of system (7) with the CDO. 
Fig. 3. The relative error x e 
CDO (k) of system (7) with the CDO. 
The measurement noises are all considered as white Guassian noise with standard deviation 
0. 01 deg / s . Furthermore, the following comparative experiments are carried out: 1) system 
(7) with CDO; 2) system (7) with the DO; 3) system (7) with the ESO. 
Firstly, results of system (7) using the proposed CDO are shown in Figs. 1–3 . In the 
ﬁgures, x i, CDO (k) (i = 1 , 2, · · · , 6) represents the i-th component of x CDO (k) which is the 
state of the spacecraft system using the CDO. Similarly, e CDO (k) is the estimation error of 
the CDO. e i, CDO (k) is the i-th component of e CDO (k) . x e 
CDO (k) is the error between the actual 
system and the nominal system of the spacecraft system using the CDO. x e 
i, CDO (k) is the 
i-th component of x e 
CDO (k) with x e 
i, CDO (k) = x i, CDO (k) −¯x i (k ) where ¯x i (k ) (i = 1 , 2, · · · , 6) 
is the component of the nominal state ¯x (k) . Note that e i, CDO (k) can be used to verify the 
effectiveness of the CDO. From Figs. 1–3 , it is easy to ﬁnd that the state x CDO (k) and x e 
CDO (k) 
converge smoothly and rapidly. 
Secondly, results of system (7) using the DO are shown in Figs. 4–6 . x DO (k) , x i, DO (k) , 
e DO (k) , e i, DO (k) , x e 
DO (k) and x e 
i, DO (k) have the similar meaning as those in the results of the 
system using the CDO and hence are omitted. Furthermore, the DO is given as 
⎧ 
⎨ 
⎩ 
ˆ 
w (k) = 
v w (k) + L w x DO (k) 
v w (k + 1) = 
(W −L w GV )( v w (k) + L w x D O (k)) −L w (Ax DO (k) + Bu DO (k)) 
u DO (k) = 
¯u (k) + K (x DO (k) −¯x (k)) −ˆ 
d o (k) 
21

## Page 22

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Fig. 4. The state x DO (k) of system (7) with the DO. 
Fig. 5. The estimation error e DO (k) of system (7) with the DO. 
Fig. 6. The relative error x e 
DO (k) of system (7) with the DO. 
Fig. 7. The state x ESO (k) of system (7) with the ESO. 
Finally, results of system (7) using the ESO are shown in Figs. 7 and 8 . x ESO (k) , x i, ESO (k) , 
e ESO (k) , e i, ESO (k) , x e 
ESO (k) and x e 
i, ESO (k) have the similar meaning as those in the results of 
the system using the CDO and hence are omitted. The ESO is given as 
⎧ 
⎨ 
⎩ 
ˆ 
d f (k) = 
v f (k) + L f x(k) 
v f (k + 1) = 
( I 3 ×3 −L f G )( v f (k) + L f x ESO (k)) −L f (Ax ESO (k) + Bu ESO (k)) 
u ESO (k) = 
¯u (k) + K (x ESO (k) −¯x (k)) −ˆ 
d f (k) 
In the following, quantitative evaluations for different controllers are shown in Table 1 . 
In Table 1 , C-SMPC is the control scheme proposed in this paper. DOBC is the disturbance- 
observer-based control scheme using the DO. ADRC is the active disturbance rejection control 
scheme using the ESO. E { e (k) } represents the mean estimation error and ∥ E { e (k) }∥ represents 
the norm of the mean estimation error. ¯k represents the step that the state ﬁrst enters the 
22

## Page 23

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Fig. 8. The estimation error e ESO (k) of system (7) with the ESO. 
Fig. 9. The relative error x e 
ESO (k) of system (7) with the ESO. 
Table 1 
The quantitative evaluations for different controllers . 
C-SMPC 
DOBC 
ADRC 
∥ E { e (k) } ∥ 
0.2524 for d o (k)0. 9050 for d f (k) 
0.4854 for d o (k) 
1.3090 for d f (k) 
¯k 
90 
105 
108 
terminal domain X f . Note that ∥ E { e (k) }∥ can represent the estimation accuracy of observers. 
Furthermore, ¯k can represent the convergence rate of the system. From Table 1 , we can obtain 
that the proposed CDO improves 48 . 00% estimation accuracy in estimating d o (k) comparing 
with the DO. Besides, the proposed CDO improves 30. 86% estimation accuracy in estimating 
d f (k) comparing with the ESO. 
From the above examples, we can ﬁnd that the results of the system using the CDO are 
better than the results using the DO/ESO, which veriﬁes the effectiveness of the proposed 
method. 
6. Conclusion 
In this paper, the attitude control problem has been addressed for the spacecraft system 
in the simultaneous presence of the state/control constraint, modeled disturbance, unmodeled 
disturbance, and stochastic noise. To compensate for the multi-source disturbances, the CDO 
has been put forward and designed to provide an estimate for both modeled and unmodeled 
disturbances in an online manner. Then, based on the estimates provided by the CDO, the C- 
SMPC scheme has been designed which is capable of handling the multi-source disturbances 
and state/iput constraints simultaneously. Furthermore, the recursive feasibility of the C-SMPC 
method has been guaranteed by reformulating the state and input constraints, and the sufﬁcient 
conditions have been provided to guarantee the stability of the closed-loop system. Finally, a 
numerical simulation on the attitude control of the spacecraft has been conducted to verify 
the effectiveness of the proposed method. One of the challenging works for further research is 
how to design a disturbance observer to obtain the estimate of d s (k) by using its information. 
23

## Page 24

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
Declaration of Competing Interest 
The authors declare that they have no known competing ﬁnancial interests or personal 
relationships that could have appeared to inﬂuence the work reported in this paper. 
References 
[1] T. Wu , B. Flewelling , F. Leve , T. Lee , Spacecraft attitude-formation tracking using line-of-sight measurements, 
J. Guidance Control Dyn. 40 (10) (2017) 2616–2629 . 
[2] T.A.W. Dwyer , H. Siraramirez , Variable-structure control of spacecraft attitude maneuvers, J. Guidance Control 
Dyn. 11 (3) (1998) 262–270 . 
[3] P.K.C. Wang , F.Y. Hadaegh , K. Lau , Synchronized formation rotation and attitude control of multiple free-ﬂying 
spacecraft, J. Guidance Control Dyn.. 22 (1) (1999) 28–35 . 
[4] L. Guo , W. Chen , Disturbance attenuation and rejection for systems with nonlinearity via DOBC approach, Int. 
J. Robust Nonlinear Control 15 (3) (2005) 109–125 . 
[5] Y. Yuan , Z. Wang , L. Guo , Event-triggered strategy design for discrete-time nonlinear quadratic games with dis- 
turbance compensations: the noncooperative case, IEEE Trans. Syst. Man Cybernet. 48 (11) (2017) 1885–1896 . 
[6] S. Sun , X. Wei , H. Zhang , H.R. Karimi , J. Han , Composite fault-tolerant control with disturbance observer for 
stochastic systems with multiple disturbances, J. Franklin Inst. 355 (12) (2018) 4897–4915 . 
[7] T. Han , J. Li , Z. Guan , C. Cai , D. Zhang , D. He , Containment control of multi-agent systems via a disturbance 
observer-based approach, J. Franklin Inst. 356 (5) (2019) 2919–2933 . 
[8] H. Zhang, X. Wei, L. Zhang, M. Tang, Disturbance rejection for nonlinear systems with mismatched disturbances 
based on disturbance observer, 2017, J. Franklin Inst., 354, 11, 4404–4424. 
[9] X. Wei , L. Guo , Composite disturbance-observer-based control and terminal sliding mode control for non-linear 
systems with disturbances, Int. J. Control 82 (6) (2009) 1082–1098 . 
[10] X. Wei , L. Guo , Composite disturbance-observer-based control and h ∞ control for complex continuous models, 
Int. J. Robust Nonlinear Control 20 (1) (2010) 106–118 . 
[11] X. Wei , Z. Wu , H.R. Karimi , Disturbance observer-based disturbance attenuation control for a class of stochastic 
systems, Automatica. 63 (2016) 21–25 . 
[12] Y. Yuan , P. Zhang , Z. Wang , L. Guo , H. Yang , Active disturbance rejection control for the ranger neutral 
buoyancy vehicle: a delta operator approach, IEEE Trans. Ind. Electron. 64 (12) (2017) 9410–9420 . 
[13] Z. Pu , R. Yuan , J. Yi , X. Tan , A class of adaptive extended state observers for nonlinear disturbed systems, 
IEEE Trans. Ind. Electron. 62 (9) (2015) 5858–5869 . 
[14] B. Guo , Z. Wu , H. Zhou , Active disturbance rejection control approach to output-feedback stabilization of 
a class of uncertain nonlinear systems subject to stochastic disturbance, IEEE Trans. Automat. Contr. 61 (6) 
(2016) 1613–1618 . 
[15] M. Zheng , X. Lyu , X. Liang , F. Zhang , A generalized design method for learning-based disturbance observer, 
IEEE/ASME Trans. Mechatron. 26 (1) (2021) 45–54 . 
[16] B. Xu , F. Sun , Y. Pan , B. Chen , Disturbance observer based composite learning fuzzy control of nonlinear 
systems with unknown dead zone, IEEE Trans. Syst. Man Cybernet. 47 (8) (2017) 1854–1862 . 
[17] H. Sun , L. Guo , Neural network-based DOBC for a class of nonlinear systems with unmatched disturbances, 
IEEE Trans. Neural Netw. Learn. Syst. 28 (2) (2017) 482–489 . 
[18] B. Kouvaritakis , M. Cannon , P. Couchman , MPC as a tool for sustainable development integrated policy as- 
sessment, IEEE Trans. Automat. Contr. 51 (1) (2006) 145–149 . 
[19] A. Ellery , J. Kreisel , B. Sommer , The case for robotic on-orbit servicing of spacecraft: spacecraft reliability is 
a myth, Acta Astronaut. 63 (5) (2008) 632–648 . 
[20] L. Zhang , W. Xie , J. Wang , Robust distributed model predictive control of linear systems with structured 
time-varying uncertainties, Int. J. Control 90 (11) (2017) 2249–2460 . 
[21] Y. Song , K. Zhu , G. Wei , J. Wang , Distributed MPC-based adaptive control for linear systems with unknown 
parameters, J. Franklin Inst. 356 (5) (2019) 2606–2624 . 
[22] Q. Cao , Z. Sun , Y. Xia , L. Dai , Self-triggered MPC for trajectory tracking of unicycle-type robots with external 
disturbance, J. Franklin Inst. 356 (11) (2019) 5593–5610 . 
[23] J. Hu , B. Ding , Off-line output feedback robust MPC with general polyhedral and ellipsoidal true state bound, 
J. Franklin Inst. 357 (8) (2020) 4505–4523 . 
24

## Page 25

Y. Xu, Y. Yuan and D. Zhou 
Journal of the Franklin Institute xxx (xxxx) xxx 
ARTICLE IN PRESS 
JID: FI 
[m1+; September 5, 2021;23:52 ] 
[24] J.A. Paulso , E.A. Buehler , R.D. Braatz , A. Mesbah , Stochastic model predictive control with joint chance 
constraints, Int. J. Control 93 (2020) 126–139 . 
[25] M. Mahmood , P. Mhaskar , Lyapunov-based model predictive control of stochastic nonlinear systems, Automatica 
48 (9) (2012) 2271–2276 . 
[26] Z. Wu , J. Zhang , Z. Zhang , F. Albalawi , H. Durand , M. Mahmood , P. Mhaskar , Economic model predictive 
control of stochastic nonlinear systems, AlChE J. 64 (9) (2018) 3312–3322 . 
[27] M.D. Shuster , A survey of attitude representation, J. Aerosp. Sci. 41 (4) (1993) 439–517 . 
[28] S.J. Chung , U. Ahsun , J.J. Slotine , Application of synchronization to formation ﬂying spacecraft: Lagrangian 
approach, J. Guidance Control Dyn. 32 (2) (2009) 512–526 . 
[29] H. Min , S. Wang , F. Sun , Z. Gao , Y. Wang , Decentralized adaptive attitude synchronization of spacecraft 
formation, Syst. Control Lett. 61 (1) (2012) 238–246 . 
[30] J. Chang , Applying discrete-time proportional integral observers for state and disturbance estimations, IEEE 
Trans. Automat. Contr. 51 (5) (2006) 814–818 . 
[31] P.W. Likins , G.E. Fleischer , Results of ﬂexible spacecraft attitude control studies utilizing hybrid coordinates, 
J. Spacecr. Rocket. 8 (3) (1971) 264–273 . 
[32] J.M. Sidi , Spacecraft Dynamics and Control, Cambridge University Press, U.K., 1997, pp. 88–100 . 
[33] M.L. Delorenzo , Sensor and actuator selection for large space structure control, J. Guidance Control Dyn. 13 
(2) (1990) 249–257 . 
[34] H. Yang , Y. Xia , P. Shi , L. Zhao , Analysis and Synthesis of Delta Operator Systems, Springer-Verlag Berlin 
Heidelberg, 2012 . 
[35] T. Jiao , W. Xing , S. Xu , On stability of a class of switched nonlinear systems subject to random disturbances, 
IEEE Trans. Circuit. Syst.-I 63 (12) (2016) 2278–2289 . 
[36] Z.P. Jiang , Y. Wang , A converse lyapunov theorem for discretetime systems with disturbances, Syst. Control 
Lett. 45 (1) (2002) 49–58 . 
[37] L. Magni, D. Pala, R. Scattolini, Stochastic model predictive control of constrained linear systems with additive 
uncertainty, In Proceedings of the European Control Conference. Budapest Hungary (2009) 2235–2240. 
[38] T.J. Tarn , Y. Rasis , Observers for nonlinear stochastic systems, IEEE Trans. Automat. Contr. 21 (4) (1976) 
441–448 . 
[39] H. Yang , X. You , C. Hua , Attitude tracking control for spacecraft formation with time-varying delays and 
switching topology, Acta Astronaut. 126 (2016) 98–108 . 
[40] Y. Liu , H. Wang , L. Guo , Composite robust h ∞ control for uncertain stochastic nonlinear systems with state 
delay via a disturbance observer, IEEE Trans. Automat. Contr. 63 (12) (2018) 4345–4352 . 
[41] X. Yao , J.H. Park , L. Wu , L. Guo , Disturbance-observer-based composite hierarchical antidisturbance control 
for singular markovian jump systems, IEEE Trans. Automat. Contr. 64 (7) (2019) 2875–2885 . 
[42] J. Qiao , Z. Li , J. Xu , X. Yu , Composite nonsingular terminal sliding mode attitude controller for spacecraft with 
actuator dynamics under matched and mismatched disturbances, IEEE Trans. Ind. Inf. 16 (2) (2020) 1153–1162 . 
[43] K. Zhao , J. Zhang , D. Ma , Y. Xia , Composite disturbance rejection attitude control for quadrotor with unknown 
disturbance, IEEE Trans. Ind. Electron. 67 (8) (2020) 6894–6903 . 
25
