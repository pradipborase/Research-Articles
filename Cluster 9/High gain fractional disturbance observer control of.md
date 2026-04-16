# High gain fractional disturbance observer control of.pdf

## Page 1

Available online at www.sciencedirect.com 
Journal of the Franklin Institute 358 (2021) 4793–4806 
www.elsevier.com/locate/jfranklin 
High-gain fractional disturbance observer control of 
uncertain dynamical systems 
Aldo Jonathan Muñoz-Vázquez a , ∗, Vicente Parra-Vega b , 
Anand Sánchez-Orta b , Oscar Martínez-Fuentes c 
a Department of Multidisciplinary Engineering, Texas A&M University, Higher Education Center, 6200 Tres Lagos 
Blvd, McAllen, TX 78504, USA 
b Robotics and Advanced Manufacturing Department, Center for Research and Advanced Studies – CINVESTAV, 
Saltillo 25900, Mexico 
c School of Engineering, Universidad Anáhuac-Veracruz, Campus Xalapa, Circuito Arco Sur s/n, Col. Lomas 
Verdes, Xalapa C.P. 91098, Veracruz, Mexico 
Received 11 December 2019; received in revised form 9 December 2020; accepted 6 April 2021 
Available online 15 April 2021 
Abstract 
Disturbance observer-based control allows to compensate unknown inputs, however, in most cases, 
requiring their integer-order differentiability. In this paper, a novel disturbance observer-based state 
feedback controller is proposed to compensate a more general class of fractional-, but not necessar- 
ily integer-order, differentiable unknown inputs. The proposed fractional PI-like structure yields precise 
conditions for feedback gain tuning. Remarkably, the resulting controller rejects non-differentiable dis- 
turbances with a smooth controller, guaranteeing robustness, an outstanding features for tracking tasks, 
under a prescribed practical stability regimen. A comparison to a fractional sliding mode observer is 
conducted via simulations to highlight the reliability of the proposed scheme. 
© 2021 The Franklin Institute. Published by Elsevier Ltd. All rights reserved. 
1. Introduction 
The high-gain concept was pioneered in [1–3] addressing observer design, assuring precise 
and fast state estimation, later extended into high-gain observer-based control in [4–9] . These 
∗Corresponding author. 
E-mail addresses: aldo.munoz-vazquez@tamu.edu (A.J. Muñoz-Vázquez), vparra@cinvestav.mx (V. Parra-Vega), 
anand.sanchez@cinvestav.mx (A. Sánchez-Orta), oscar.martinezfu@anahuac.mx (O. Martínez-Fuentes). 
https://doi.org/10.1016/j.jfranklin.2021.04.020 
0016-0032/© 2021 The Franklin Institute. Published by Elsevier Ltd. All rights reserved.

## Page 2

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
schemes arose as viable options for robust and fast estimation throughout increasing the feed- 
back gains, as long as the controller remains within admissible bounds. Although high-gain 
controllers induce only practical stability [10] , they facilitate implementation and tuning effort, 
in contrast to sound robust controllers, such as variable structure and model-based schemes, 
in which the theoretical asymptotic and ﬁnite-time stability are not achievable in practice. 
Disturbance observer-based control is considered in [11,12] based on a system nominal 
model without uncertainties nor disturbances. Frequency domain-based designs for linear sys- 
tems have shown advantages in practice since relevant performance can be set, including band- 
width constraints. For nonlinear disturbance observers, lumped disturbances are considered as 
a typical approach [13,14] . Recently, high-gain disturbance observers have been proposed for 
integer-order systems [15–18] , guaranteeing prescribed tracking. All these results assume that 
the unknown lumped disturbance is Lipschitz continuous, which for some advanced appli- 
cations, could be a limitation. In response to this issue, fractional sliding mode control has 
been considered with a disturbance observer [19] . However, there remains a question on how 
to deal with simpler control structures with fractional disturbance observers. In this direction, 
Martínez-Fuentes and Martínez-Guerra [20] proposed a Mittag–Lefﬂer stable state observer 
for fractional-order systems. 
The contribution of this paper is then, the formulation of [20] in the realm of [21,22] to 
provide a smooth controller able to precisely compensate continuous but not necessarily dif- 
ferentiable disturbances. 
Fractional calculus constitutes an important and emerging tool to address advanced and 
complex phenomena [23] , including a large variety of engineering systems subject to a 
wider class of dynamic effects [24] . Fractional-order controllers have been widely considered 
since they signiﬁcantly enhance the dynamical performance of their integer-order counter- 
parts [25,26] . In [21,22] , sliding mode-based disturbance observers are studied to account for 
lumped Hölder continuous disturbances, that is, not necessarily integer-order differentiable 
functions, which possess well-posed fractional-order derivatives. Later Muñoz-Vázquez et al. 
[27] extended this idea to provide a theoretically ﬁnite-time exact estimation of Hölder con- 
tinuous disturbances, nonetheless, the unavoidable chattering phenomenon affects the tracking 
precision, as well as the integrity of the system components in real-time applications. Other 
approaches have combined disturbance observers and fractional-order tools [28–34] . 
In contrast to the outstanding and inspiring mentioned contributions, the approach proposed 
in this paper stands for: A high-gain smooth PI-like structure to observe continuous but 
not necessarily differentiable disturbances, whose tracking precision can be adjusted with a 
single control parameter. In this sense, the proposed scheme provides a methodology that 
modulates constant gains through adjusting the ultimate upper bound of the tracking errors, 
thus providing further insights on the tuning procedure. 
The rest of this paper is organized as follows. Section 2 presents basic preliminaries on 
fractional-order systems and stability analysis. Section 3 introduces the system deﬁnition and 
the high-gain observer based control design. Section 4 presents a simulation study. Finally, 
conclusive discussions are presented in Section 5 . 
2. Preliminaries 
2.1. On fractional-order systems 
Fractional calculus deals with differentiation and integration of non-integer orders by 
means of differintegral operators. For x : t → R n a real-valued vector function and t ⊂
4794

## Page 3

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
R a compact set, the differintegral operators of order α ∈ (0, 1) are deﬁned as follows 
[23,35,36] : 
• Riemann–Liouville integral 
I αx (t) = 
1 
(α) 
 t 
0 
x (τ ) 
(t −τ ) 1 −α dτ
(1) 
• Marchaud derivative 
M D αx (t) = 
x (t) 
(1 −α)(t −t 0 ) α + 
α
( 1 −α) 
 t 
0 
x ( t) −x (τ ) 
( t −τ ) α+1 dτ
(2) 
• Extended Caputo derivative 
D αx (t) = 
x (t) −x (0) 
( 1 −α)(t −t 0 ) α + 
α
( 1 −α) 
 t 
0 
x ( t) −x (τ ) 
( t −τ ) α+1 dτ
(3) 
where (ς) = 
 ∞ 
0 z ς−1 e −z dz is the Gamma function; accordingly, it follows that 
D αx (t) = M D α[ x (t) −x (0)] . 
(4) 
Furthermore, in the case of x (t) is weakly integer-order differentiable, one has that 
Eqs. (2) and (3) become 
M D αx (t) = RL D αx (t) = d 
dt I 1 −αx (t) , 
D αx (t) = C D αx (t) = I 1 −α ˙ x (t) , 
(5) 
where RL D αx (t) and C D αx (t) are the classical Riemann–Liouville and Caputo derivatives, and 
integration by parts of Eqs. (2) and (3) is used. It is worth noticing that the Marchaud operator 
does not require the use of an integer-order derivative in its deﬁnition. However, Marchaud 
and Riemann–Liouville derivatives coincide for sufﬁciently good functions. Besides, it has 
been proved that [27,35] , 
M D αI αx (t) = x (t) , 
I αD αx (t) = x (t) −x (0) . 
(6) 
for sufﬁciently good, but not necessarily integer-order differentiable, real-valued vector func- 
tion x (t) . 
For two real-valued and Lebesgue integrable functions x(t) and y(t) , with x(t) ≤y(t) for 
almost all t ≥0, one has that 
I αx(t) ≤I αy(t) ∀ t ≥0, whenever α > 0. 
(7) 
The following deﬁnition from [37] is also of preponderant interest. 
Deﬁnition 1. The constant vector x ∗∈ R n is an equilibrium point for D αx = f (t, x ) if 
D αx ∗= f (t, x ∗) for all t ≥0. 
Since the extended Caputo derivative of a constant is null, x ∗is an equilibrium if and only 
if f (t, x ∗) = 0 for all t ≥0. Therefore, y (t) = 0 is an equilibrium for D αy (t) = ¯f (t , y (t )) , 
with y (t) = x (t) −x ∗and ¯f (t , y (t )) = f (t , y (t ) + x ∗) . 
The Mittag–Lefﬂer stability generalizes the exponential stability of the integer-order case 
to the more general fractional-order case. Thus, consider the following deﬁnition [37] . 
4795

## Page 4

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
Deﬁnition 2. The solution of D αx (t) = f (t , x (t )) is Mittag–Lefﬂer stable if 
∥ x (t) ∥ ≤

m( x (0)) E β(−at β) 
b 
for all t ≥0, where m( x ) ≥0 is a locally Lipschitz continuous function on x with m( 0 ) = 0, 
for β ∈ (0, 1) and some real numbers a, b > 0, where 
E α,β(z) = 
∞ 
 
k=0 
z k 
(αk + β) 
(8) 
is the two-parameters Mittag–Lefﬂer function, with α, β > 0. Besides, one has that e z = 
E 1 , 1 (z) is the exponential function, and E α, 1 (z) = E α(z) is the one-parameter Mittag–Lefﬂer 
function. 
The stability of fractional-order nonlinear systems has been studied in [8] , and the Mittag–
Lefﬂer stability of a fractional-order differintegral inequality was proved in [38,39] for 
quadratic functions. More recently, Muñoz-Vázquez et al. [36] demonstrated that the same 
inequality of [38,39] is valid for operator (3) , and the validity of such inequality in the case 
of nonsmooth convex functions was demonstrated [40] . Thus, consider the following. 
Deﬁnition 3 (Deﬁnition 3.1.1 of [41] , p. 112) . A function V : x ⊂R n → R is convex if x 
is convex and ∀ x , y ∈ x , the following inequality holds for all λ ∈ [0, 1] , 
V (λx + (1 −λ) y ) ≤λV ( x ) + (1 −λ) V ( y ) . 
(9) 
Deﬁnition 4 (Corollary 2.6 of [42] , p. 35) . Let V : x ⊂R n → R be a convex function. The 
set-valued map 
∂V ( x ) = 

ζ ∈ R n : V ( y ) −V ( x ) −ζT ( y −x ) ≥0, ∀ y ∈ x 

(10) 
is the proximal subdifferential of V at x ∈ x , and ζ( x ) ∈ ∂V ( x ) is a proximal subgradient 
of V at x . 
In the case of V is differentiable at x , one has that ∂V ( x ) = {∇V ( x ) } , and thus, Eq. (10) be- 
comes 
∇V ( x ) T ( y −x ) ≤V ( y ) −V ( x ) 
(11) 
The following Lemma and Theorem of [40] are of interest for the control methods proposed 
in this paper. 
Lemma 1. Let V ( x (t)) be a real-valued function that is Lipschitz continuous on x , with 
convex domain x ⊆R n , and let x ∈ x be a real-valued vector function whose entries are 
continuous functions with well-posed fractional derivatives of at least some order α ∈ (0, 1) . 
If V ( x (t)) is convex, then 
D αV ( x (t)) ≤
inf 
ζ( x ) ∈ ∂V ( x ) ζ( x (t )) T D αx (t ) . 
(12) 
Theorem 1. Let V ( x (t)) be a positive deﬁnite real-valued function, which is Lipschitz con- 
tinuous and convex in x , and 0 ∈ ∂V ( 0 ) . If 
inf 
ζ( x ) ∈ ∂V ( x ) ζ( x (t)) T D αx (t) ≤−γV ( x (t)) q 
(13) 
for almost all t ≥0, γ > 0, and q ∈ (0, 1] , then V ( x (t)) is Mittag–Lefﬂer stable. If in 
addition V ( x (t)) = ∥ x (t) ∥ b for some b > 0, then ∥ x (t) ∥ is also Mittag–Lefﬂer stable. 
4796

## Page 5

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
3. Controller design 
3.1. System deﬁnition 
Consider the following linear time invariant (LTI) system subject to a wide class of not 
necessarily integer-order differentiable disturbances, non-linearities and dynamic uncertainties, 
˙ x (t) = A x (t) + B u (t) + E d (t) 
(14) 
where x ∈ R n is the state, which is assumed available for control purposes, u ∈ R n u is the 
control input, A ∈ R n×n and B ∈ R n×n u are constant matrices, d ∈ R n d is an unknown but 
continuous disturbance, with E ∈ R n×n d a constant matrix, and, without loss of generality, 
consider that n u , n d ≤n. The following standard assumptions on system (14) are considered 
[43] , 
• Assumption 1. The pair (A, B) is controllable. 
• Assumption 2. The matrix B has full-column rank. 
• Assumption 3. The disturbance is matched, that is, E = B. 
• Assumption 4. The disturbance d satisﬁes sup ∥ D αd ∥ < ∞ for α ∈ (0, αc ) , and αc > 0
the critical order of d . 
The family of disturbances is fully characterized by Assumption 4, this means that impul- 
sive or very high frequency disturbances are not considered. The scalar components of those 
real-valued vector functions that satisfy Assumption 4 can be characterized by the Hölder 
condition [44,45] , that is, f (t) is αc -Hölder continuous on  if there exists a constant H 
such that | f (t 2 ) −f (t 1 ) | ≤H | t 2 −t 2 | αc , for some αc ∈ (0, 1) . In this sense, f (t) posses uni- 
formly continuous derivatives of any order α ∈ (0, αc ) . It is worth to comment that Hölder 
continuity is less restrictive than Lipschitz condition, which only considers the case of αc = 1 . 
In addition, Lipschitz continuity is commonly assumed during control design [7] . 
3.2. Disturbance observer-based control design 
In accordance to Assumption 1, there is a matrix K ∈ R n×n u , such that the eigenvalues of 
¯A = A −BK are located in the open left-half plane. Therefore, the ideal controller 
u 0 (t) = −K x (t) 
(15) 
produces x → 0 when t → ∞ , in the case of d = 0 and u = u 0 . Thus, the controller is 
proposed as u (t) = u 0 (t) −ˆ d (t) , this is, 
u (t) = −K x (t) −ˆ d (t) 
(16) 
for ˆ d (t) an observer of disturbance d (t) . Moreover, by considering the controller (16) , As- 
sumption 3 implies that system (14) can be rewritten as 
˙ x (t) = ¯A x (t) + B 

−ˆ d (t) + d (t) 

. 
(17) 
Consider the integral auxiliary variable 
σ0 (t) = B + 
	
x (t) −x (0) −
 t 
0 
¯A x (τ ) dτ

(18) 
4797

## Page 6

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
whose ﬁrst-order derivative complies with 
˙ σ0 (t) = −ˆ d (t) + d (t) . 
(19) 
In addition, let σ be a differintegral variable deﬁned as 
σ(t) = D 1 −ασ0 (t) . 
(20) 
In virtue of σ0 (0) = 0 , the operator D 1 −α can be either the extended Caputo or the Marchaud 
derivative. Furthermore, the differentiability of σ0 implies that 
D ασ(t) = ˙ σ0 (t) , 
= −ˆ d (t) + d (t) . 
(21) 
Thus, taking into account the fractional-order differentiability of the disturbance, the observer 
is proposed as the high-gain fractional PI 
ˆ d (t) = k p 
ε σ(t) + k i 
ε 2 I ασ(t) . 
(22) 
for k p and k i positive scalar feedback gains, which satisfy that, the roots of the polyno- 
mial ρ(s) = s 2 + k p s + k i = 0 are located in the open left-half plane, this is k p , k i > 0. The 
parameter ε is designed to adjust the precision of ˆ d → d . 
The change of variables 
ξ1 = σ
ε 
ξ2 = −k i 
ε 2 I ασ + d 
(23) 
produces 
εD αξ1 (t) = −k p ξ1 (t) + ξ2 (t) . 
εD αξ2 (t) = −k i ξ1 (t) + εD αd (t) , 
(24) 
or in a condensed form 
εD αξ(t) = ξ(t) + ε δ(t) 
(25) 
with ξT = [ ξT 
1 ξT 
2 ] ,  = 
−k p I 
I 
−k i I 
0 

, and δT = [ 0 T D αd T ] . 
3.3. Stability analysis 
Since the scalar components of the differential equations that conform system (24) are 
completely decoupled, consider without loss of generality that n u = 1 , that is, ξ = [ ξ1 ξ2 ] T , 
 = 
−k p 
1 
−k i 
0 

, and δ = [0 D αd] T . Thus, the stability properties of system (25) are 
analyzed in the following main result. 
Theorem 2. Consider the fractional-order system (25) . Then, for k p , k i and ε > 0, the dis- 
turbance estimation error d = d −ˆ 
d converges inside an open ball centered at the origin, 
whose radius is proportional to ε. 
4798

## Page 7

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
Proof. Since  is a Hurwitz matrix, there exists symmetric and positive deﬁnite matrices 
P, Q ∈ R 2×2 such that 
2Q + P  + T P = 0. 
(26) 
Now, consider the candidate Lyapunov function 
V = ε ∥ P 0 ξ∥ 
(27) 
where P 0 satisﬁes P = P T 
0 P 0 , and || · || is the conventional Euclidean vector norm. Then, the 
fractional derivative of V complies to 
D αV ≤ε ξT P 
∥ P 0 ξ∥ D αξ
= 
1 
∥ P 0 ξ∥ 

−ξT Q ξ + ε ξT P δ

≤
1 
∥ P 0 ξ∥ 

−λm (Q) ∥ ξ∥ 2 + ε ∥ P 0 ξ∥ λM (P 0 ) ∥ δ∥ 
= −λm (Q) ∥ ξ∥ 2 
∥ P 0 ξ∥ 
+ ελ1 / 2 
M (P ) ∥ δ∥ 
(28) 
for λm (·) and λM (·) the minimum and maximum singular value operators. 
Now, considering that ∥ P 0 ξ∥ 2 = ξT P ξ, one has that λm (P ) ∥ ξ∥ 2 ≤∥ P 0 ξ∥ 2 ≤λM (P ) ∥ ξ∥ 2 , 
consequently one obtains 
D αV ≤−γV + ελ1 / 2 
M (P ) k δ. 
(29) 
where γ = λm (Q) 
ελM (P ) and k δ > ∥ δ∥ . Then, integrating Eq. (29) leads to 
V (t) ≤V (0) E α(−γt α) + ελ1 / 2 
M (P ) k δ
 t 
0 
τ α−1 E α,α(−γ τ α) dτ. 
(30) 
Evaluating the integral in the above inequality leads to 
 t 
0 
τ α−1 E α,α(−γ τ α) dτ = 
 t 
0 
∞ 
 
k=0 
(−γ ) k τ (k+1) α−1 
((k + 1) α) dτ
= 
∞ 
 
k=0 
(−γ ) k t (k+1) α
((k + 1) α + 1) 
= (−γ ) −1 
∞ 
 
k=1 
(−γ ) k t kα
(kα + 1) 
= (−γ ) −1 
 ∞ 
 
k=0 
(−γ ) k t kα
(kα + 1) −1 
 
= γ −1 
1 −E α(−γt α) 

≤γ −1 
(31) 
where the term E α(−γt α) vanishes and is completely monotonic, Theorem 4.4 of [46] , p. 71. 
Therefore 
V (t) ≤V (0) E α(−γt α) + ελ1 / 2 
M (P ) k δ
γ
4799

## Page 8

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
= V (0) E α(−γt α) + ε 2 k δλ3 / 2 
M (P ) 
λm (Q) 
. 
(32) 
Now, using 
ελ1 / 2 
m (P ) ∥ ξ(t) ∥ ≤V (t) ≤ελ1 / 2 
M (P ) ∥ ξ(t) ∥ , 
(33) 
one has that 
∥ ξ(t) ∥ ≤λ1 / 2 
M (P ) 
λ1 / 2 
m (P ) 
∥ ξ(0) ∥ E α(−γt α) + ε 

k δλ3 / 2 
M (P ) 
λ1 / 2 
m (P ) λm (Q) 

, 
(34) 
and considering that E α(−γt α) → 0, one has that 
lim 
t→∞ ∥ ξ(t) ∥ ≤ε 

k δλ3 / 2 
M (P ) 
λ1 / 2 
m (P ) λm (Q) 

, 
(35) 
establishing that the parameter ε modulates the radius of the domain of attraction for lim t→∞ ξ. 
At this point, since one has that 
ˆ 
d = [ k p −1] ξ + d, 
from Eqs. (22) to (23) , it results 
lim 
t→∞ | ˆ 
d −d| ≤max (1 , k p ) lim 
t→∞ || ξ|| 
≤ε · max (1 , k p ) 
 
k δλ3 / 2 
M (P ) 
λ1 / 2 
m (P ) λm (Q) 
 
(36) 
proving the assertion of the theorem. □
Remark 1. It is worth to comment that the peaking phenomenon, inherent to any high- 
gain scheme, is alleviated by means of the integral error deﬁnition of σ(t) since σ(0) = 
0 . Besides, note that in the controller u = −K x −ˆ d , only the disturbance observer term ˆ d 
depends explicitly on 1 /ε, and note also that ˆ d (0) = 0. Thus, the peaking phenomena reduced 
since u (0) = −K x (0) , without any dependence on 1 /ε. However, a very small ε could be 
catastrophic due to a limited sampling rate implementation and high-frequency noisy effects. 
Theorem 2 implies that the observer ˆ d estimates the disturbance d with a precision that 
can be modulated by means of ε. In addition, the precision of the convergence x → 0 can be 
directly adjusted by decreasing the value of ε, as it is stated in the following result. 
Theorem 3. Consider system (17) with the disturbance observer (22) . Then, x converges 
inside an open vicinity of the origin, whose radius is proportional to ε. 
Proof. From Eq. (21) , one has that D ασ = −ˆ d + d = d , and from Eqs. (22) to (23) , one 
gets D ασ = [ −k p 1] ξ, then d = [ −k p 1] ξ. Therefore Theorem 2 implies that d converges 
inside a vicinity of the origin, whose radius is proportional to ε. Thus, the precision of the 
approximation ˆ d → d is directly proportional to ε. 
The closed-loop system using the controller u = −K x −ˆ d is 
˙ x (t) = ¯A x (t) + Bd (t) 
(37) 
whose solution becomes 
x (t) = e ¯A t x (0) + 
 t 
0 
e ¯A (t−τ ) Bd (τ ) dτ
(38) 
4800

## Page 9

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
whose behavior is directly related to the term d (τ ) , which converges from the beginning 
to a compact vicinity of the origin. This means that is not possible for x (t) to escape in 
ﬁnite-time, and assuming the opposite leads to an absurd. In addition, since ¯A is a Hurwitz 
matrix, there are symmetric and positive deﬁnite matrices ¯P , ¯Q ∈ R n×n , such that 
2 ¯Q + ¯P ¯A + ¯A T ¯P = 0, 
(39) 
and the candidate Lyapunov function ¯V = 1 
2 x T ¯P x yields the following time derivative, 
˙ ¯V = −x T ¯Q x + x T ¯P Bd 
(40) 
Therefore, it is clear that 
∥ x ∥ ≥λM ( ¯P ) λM (B) 
λm ( ¯Q ) 
∥ d ∥ ⇒ ˙ ¯V ≤0. 
(41) 
From the expressions (35) and (36) , for any η > 0, there is a ﬁnite time instant t η ≥0, 
such that || d || < (1 + η) κε, with κ = n max (1 , k p ) 

k δλ3 / 2 
M (P) 
λ1 / 2 
m (P) λm (Q) 

. Hence, for any t ≥t η, one 
has that 
∥ x ∥ ≥ε · (1 + η) n max (1 , k p ) 
λM ( ¯P ) λM (B) 
λm ( ¯Q ) 
·
k δλ3 / 2 
M (P ) 
λ1 / 2 
m (P ) λm (Q) 

⇒ ˙ ¯V ≤0, 
(42) 
as a consequence, x converges inside an open vicinity of the origin, whose radius is propor- 
tional to ε. This produces that, by virtue of the action of the disturbance observer ˆ d , the state 
x evolves with a negligible effect of d . Thus, the precision of the convergence of x → 0 , 
via u 0 = −K x , can be directly adjusted by decreasing the value of ε. □
Remark 2. Note that the proposed controller u = u 0 −ˆ d results as 
u = −K x −¯k p σ −¯k i I ασ, 
(43) 
which consists of a state feedback plus a fractional PI-like controller, with the proportional 
and integral feedback gains given by ¯k p = k p 
ε and ¯k i = k i 
ε 2 . 
4. Simulations 
A numerical study is programmed in Simulnk in Matlab, based on the Euler integrator 
running at 0.1 ms. The CRONE method was used with a transfer function of 10-order for a 
frequency range of [10 −3 , 10 3 ] rad/s [47] . 
Since the purpose of this simulation is to assess the reliability of the proposed disturbance 
observer, consider the simple but representative nonlinear pendulum system, 
ml 2 ¨q = T −mgl sin (q) + ϕ, 
(44) 
where l = 0. 5 m is the length, m = 0. 5 kg is the mass, g = 9 . 81 m / s 2 is the gravity, T 
is the control torque and ϕ is the unknown disturbance. For simulation purposes, consider 
d = ϕ/ (ml 2 ) = sin (2t) + sin (4t) + noise , with noise = I βrnd(ζ ) for β = 0. 8 , and rnd a 
random function within [ −100, 100] with sampling of 0.001 s, see Fig. 1 . 
The objective is to regulate at q(t) = 0 for any initial condition, even in the presence 
of the unknown disturbance d. After the change of variables x 1 = q, and x 2 = ˙ 
q , system 
4801

## Page 10

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
Fig. 1. Non-differentiable Hölder disturbance. 
Fig. 2. Disturbance observers. 
(44) renders system (14) with A = 
0 
1 
0 
0 

and B = 
0 
1 

. The initial condition q(0) = 2
and ˙ 
q (0) = 0 is considered. 
It is evident that in the case of d = 0, the system is stabilised by means of the ideal 
controller u 0 = −k 1 x 1 −k 2 x 2 , therefore, the integral error variable becomes 
σ0 (t) = x 2 (t) −x 2 (0) + 
 t 
0 
	
k 1 x 1 (τ ) + k 2 x 2 (τ ) 

dτ
(45) 
and σ (t) = D 1 −ασ0 (t) is the fractional deviation variable used to design the disturbance 
observer. The ideal control gains are set at k 1 = 4 and k 2 = 4, and those of the disturbance 
observer at k p = 2 and k i = 1 . 
Numerical results are shown for ε = 0. 002 and α = 0. 5 . Besides, the fractional sliding 
mode disturbance observer ˆ 
d = −k d I αsign (σ0 ) , with k d = 25 is considered for comparison 
purposes. It is worth noticing that the case α = 1 is not considered since the studied distur- 
bances are not assumed to be integer-order differentiable. The parameter ε of the high-gain 
observer was tuned by gradually reducing it to an allowable value in accordance with the 
4802

## Page 11

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
Fig. 3. Simulation results. 
4803

## Page 12

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
numerical stability of the simulator. On the other hand, gain k d of the sliding mode observer 
was increased to achieve a good performance with small chattering. 
Fig. 2 highlights the efﬁcacy of both fractional-order disturbance observers, the high-gain 
linear and the sliding mode based schemes. A slightly improvement can be realized in the 
case of the high-gain approach. 
In Fig. 3 one can appreciate that both, the high-gain and the sliding mode disturbance 
observer-based controllers yield acceptable performances since the variable q is regulated to 
the origin, with a high degree of precision. Nonetheless, the smoothness of the high-gain based 
controller produces a precise estimation, without any chattering effect, and consequently, a 
better closed-loop performance is obtained, as it can be ﬁgured out by observing the dynamics 
of σ0 . 
5. Conclusion 
This study constitutes an evidence that robust control tools in combination with fractional- 
order techniques furnish high-end structures to address a large class of physical phenomena 
in uncertain dynamical systems. It is shown that high-gain schemes outperform non-smooth 
techniques, such as sliding mode ones, through the capacity of modulating the convergence 
accuracy by means of a smooth controller. In addition, it is worth to comment that the peaking 
phenomenon, inherent to any high-gain scheme, is alleviated by means of the integral error, 
which, in the case of feedback systems, allows to account for the initial condition. Future 
studies consider the application of the proposed scheme in the control of uncertain dynamical 
systems, such as electromechanical servo-actuators design, robust robot control, stabilization 
of aerodynamical and underwater vehicles, and renewable energy systems, to name a few. 
Declaration of Competing Interest 
We authors declare that we have no interest conﬂict regarding the publication of this paper. 
References 
[1] I.R. Petersen , C.V. Hollot , High-gain observer approach to disturbance attenuation using measurement feedback, 
Int. J. Control 48 (6) (1988) 2453–2464 . 
[2] I.R. Petersen , C.V. Hollot , High gain observers applied to problems in the stabilization of uncertain linear 
systems, disturbance attenuation and N ∞ optimization, Int. J. Adapt. Control Signal Process. 2 (4) (1988) 
347–369 . 
[3] S. Nicosia , A. Tornambè, High-gain observers in the state and parameter estimation of robots having elastic 
joints, Syst. Control Lett. 13 (4) (1989) 331–337 . 
[4] S. Oh , H.K. Khalil , Nonlinear output-feedback tracking using high-gain observer and variable structure control, 
Automatica 33 (10) (1997) 1845–1856 . 
[5] K.W. Lee , H.K. Khalil , Adaptive output feedback control of robot manipulators using high-gain observer, Int. 
J. Control 67 (6) (1997) 869–886 . 
[6] A.M. Dabroom , H.K. Khalil , Output feedback sampled-data control of nonlinear systems using high-gain ob- 
servers, IEEE Trans. Autom. Control 46 (11) (2001) 1712–1725 . 
[7] H.K. Khalil , L. Praly , High-gain observers in nonlinear feedback control, Int. J. Robust Nonlinear Control 24 
(6) (2014) 993–1015 . 
[8] H. Liu , H.K. Khalil , Output feedback stabilization using super-twisting control and high-gain observer, Int. J. 
Robust Nonlinear Control 29 (3) (2019) 601–617 . 
[9] T. Ma , Y. Liu , C. Shih , C. Cao , Handling of nonlinear systems using ﬁltered high-gain output feedback controller, 
Int. J. Robust Nonlinear Control 28 (18) (2018) 6070–6086 . 
4804

## Page 13

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
[10] X.S. Yang , Practical stability in dynamical systems, Chaos Solitons Fractals 11 (7) (2000) 1087–1092 . 
[11] S. Katsura , K. Irie , K. Ohishi , Wideband force control by position-acceleration integrated disturbance observer, 
IEEE Trans. Ind. Electron. 55 (4) (2008) 1699–1706 . 
[12] W.H. Chen , J. Yang , L. Guo , S. Li , Disturbance-observer-based control and related methods – an overview, 
IEEE Trans. Ind. Electron. 63 (2) (2015) 1083–1095 . 
[13] X. Chen , S. Komada , T. Fukuda , Design of a nonlinear disturbance observer, IEEE Trans. Ind. Electron. 47 (2) 
(2000) 429–437 . 
[14] W.H. Chen , Disturbance observer based control for nonlinear systems, IEEE/ASME Trans. Mechatron. 9 (4) 
(2004) 706–710 . 
[15] D. Won , W. Kim , D. Shin , C.C. Chung , High-gain disturbance observer-based backstepping control with out- 
put tracking error constraint for electro-hydraulic systems, IEEE Trans. Control Syst. Technol. 23 (2) (2014) 
787–795 . 
[16] C.J. Kempf , S. Kobayashi , Disturbance observer and feedforward design for a high-speed direct-drive positioning 
table, IEEE Trans. Control Syst. Technol. 7 (5) (1999) 513–526 . 
[17] Y. Liu , D. Söffker , Variable high-gain disturbance observer design with online adaption of observer gains 
embedded in numerical integration, Math. Comput. Simul. 82 (5) (2012) 847–857 . 
[18] Y. Liu , D. Söffker , Robust control approach for input–output linearizable nonlinear systems using high-gain 
disturbance observer, Int. J. Robust Nonlinear Control 24 (2) (2014) 326–339 . 
[19] J. Wang , C. Shao , Y.Q. Chen , Fractional order sliding mode control via disturbance observer for a class of 
fractional order systems with mismatched disturbance, Mechatronics 53 (2018) 8–19 . 
[20] O. Martínez-Fuentes , R. Martínez-Guerra , A high-gain observer with Mittag–Lefﬂer rate of convergence for a 
class of nonlinear fractional-order systems, Commun. Nonlinear Sci. Numer. Simul. 79 (2019) 104909 . 
[21] A.J. Muñoz-Vázquez , V. Parra-Vega , A. Sánchez-Orta , Fractional-order nonlinear disturbance observer based 
control of fractional-order systems, J. Comput. Nonlinear Dyn. 13 (7) (2018) 071007 . 
[22] A.J. Muñoz-Vázquez , V. Parra-Vega , A. Sánchez-Orta , G. Romero-Galván , Finite-time disturbance observer via 
continuous fractional sliding modes, Trans. Inst. Meas. Control 40 (14) (2018) 3953–3963 . 
[23] I. Podlubny , Fractional Differential Equations: An Introduction to Fractional Derivatives, Fractional Differential 
Equations, to Methods of Their Solution and Some of Their Applications, 198, Elsevier, 1998 . 
[24] D. Baleanu , J.A.T. Machado , A.C. Luo , Fractional Dynamics and Control, Springer Science & Business Media, 
2011 . 
[25] B. Yang , T. Yu , H. Shu , D. Zhu , F. Zeng , Y. Sang , L. Jiang , Perturbation observer based fractional-order PID 
control of photovoltaics inverters for solar energy harvesting via yin-yang-pair optimization, Energy Convers. 
Manag. 171 (2018) 170–187 . 
[26] B. Yang , T. Yu , H. Shu , Y. Han , P. Cao , L. Jiang , Adaptive fractional-order PID control of PMSG-based wind 
energy conversion system for MPPT using linear observers, Int. Trans. Electr. Energy Syst. 29 (1) (2019) e2697 . 
[27] A.J. Muñoz-Vázquez , V. Parra-Vega , A. Sánchez-Orta , G. Romero-Galván , D. Lara-Alabazares , Robust control 
of wind turbines based on fractional nonlinear disturbance observer, Asian J. Control 22 (5) (2019) 1801–i810 . 
[28] W. Li , Y. Hori , Vibration suppression using single neuron-based pi fuzzy controller and fractional-order distur- 
bance observer, IEEE Trans. Ind. Electron. 54 (1) (2007) 117–126 . 
[29] Y. Chen , B.M. Vinagre , I. Podlubny , Fractional order disturbance observer for robust vibration suppression, 
Nonlinear Dyn. 38 (1–4) (2004) 355–367 . 
[30] Y.Q. Chen , B.M. Vinagre , I. Podlubny , On fractional order disturbance observer, in: Proceedings of the ASME 
International Design Engineering Technical Conferences and Computers and Information in Engineering Con- 
ference, American Society of Mechanical Engineers Digital Collection, 2003, pp. 617–624 . 
[31] S. Pashaei , M. Badamchizadeh , A new fractional-order sliding mode controller via a nonlinear disturbance 
observer for a class of dynamical systems with mismatched disturbances, ISA Trans. 63 (2016) 39–48 . 
[32] C. Ma , Y. Hori , Backlash vibration suppression in torsional system based on the fractional order q-ﬁlter of 
disturbance observer, in: Proceedings of the IEEE International Workshop on Advanced Motion Control., IEEE, 
2004, pp. 577–582 . 
[33] S. Shao , M. Chen , S. Chen , Q. Wu , Adaptive neural control for an uncertain fractional-order rotational me- 
chanical system using disturbance observer, IET Control Theory Appl. 10 (16) (2016) 1972–1980 . 
[34] M. Chen , S.-Y. Shao , P. Shi , Y. Shi , Disturbance-observer-based robust synchronization control for a class of 
fractional-order chaotic systems, IEEE Trans. Circuits Syst. II Exp. Briefs 64 (4) (2016) 417–421 . 
[35] S.G. Samko , A.A. Kilbas , O.I. Marichev , et al. , Fractional integrals and derivatives, 1993, Gordon and Breach 
Science Publishers, Yverdon Yverdon-les-Bains, Switzerland, 1993 . 
4805

## Page 14

A.J. Muñoz-Vázquez, V. Parra-Vega, A. Sánchez-Orta et al. Journal of the Franklin Institute 358 (2021) 4793–4806 
[36] A.J. Muñoz-Vázquez , V. Parra-Vega , A. Sánchez-Orta , G. Romero-Galván , Quadratic Lyapunov functions for 
stability analysis in fractional-order systems with not necessarily differentiable solutions, Syst. Control Lett. 116 
(2018) 15–19 . 
[37] Y. Li , Y. Chen , I. Podlubny , Mittag–Lefﬂer stability of fractional order nonlinear dynamic systems, Automatica 
45 (8) (2009) 1965–1969 . 
[38] N. Aguila-Camacho , M.A. Duarte-Mermoud , J.A. Gallegos , Lyapunov functions for fractional order systems, 
Commun. Nonlinear Sci. Numer. Simul. 19 (9) (2014) 2951–2957 . 
[39] M.A. Duarte-Mermoud , N. Aguila-Camacho , J.A. Gallegos , R. Castro-Linares , Using general quadratic Lyapunov 
functions to prove Lyapunov uniform stability for fractional order systems, Commun. Nonlinear Sci. Numer. 
Simul. 22 (1–3) (2015) 650–659 . 
[40] A.J. Muñoz-Vázquez , V. Parra-Vega , A. Sánchez-Orta , Non-smooth convex Lyapunov functions for stability 
analysis of fractional-order systems, Trans. Inst. Meas. Control 41 (6) (2019) 1627–1639 . 
[41] Y. Nesterov , Introductory Lectures on Convex Optimization, Kluwer Academic Publishers, Norwell, MA, 2004 . 
[42] F. Clarke , Y. Ledyaev , R. Stern , P. Wolenski , Control Theory and Nonsmooth Analysis, Springer Verlag, New 
York, 1998 . 
[43] C.T. Chen , Linear System Theory and Design, Oxford University Press, Inc., 1998 . 
[44] A.J. Muñoz-Vázquez , V. Parra-Vega , A. Sánchez-Orta , G. Romero-Galván , Finite-time disturbance observer via 
continuous fractional sliding modes, Trans. Inst. Meas. Control 40 (14) (2018) 3953–3963 . 
[45] A.J. Muñoz-Vázquez , H. Ramírez-Rodríguez , V. Parra-Vega , A. Sánchez-Orta , Fractional sliding mode control 
of underwater ROVs subject to non-differentiable disturbances, Int. J. Control Autom. Syst. 15 (3) (2017) 
1314–1321 . 
[46] K. Diethelm , The Analysis of fractional Differential Equations: An Application-Oriented Exposition Using 
Differential Operators of Caputo Type, Springer Science & Business Media, 2010 . 
[47] A. Oustaloup , P. Melchior , P. Lanusse , O. Cois , F. Dancla , The crone toolbox for Matlab, in: Proceedings of 
the IEEE International Symposium on Computer-Aided Control System Design, CACSD (Cat. No. 00TH8537), 
IEEE, 2000, pp. 190–195 . 
4806
