# Nonlinear Complementary Filters on the Special Orthogonal Group.pdf

## Page 1

IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 53, NO. 5, JUNE 2008
1203
Nonlinear Complementary Filters on the
Special Orthogonal Group
Robert Mahony, Senior Member, IEEE, Tarek Hamel, Member, IEEE, and Jean-Michel Pﬂimlin
Abstract—This paper considers the problem of obtaining good
attitude estimates from measurements obtained from typical low
cost inertial measurement units. The outputs of such systems are
characterized by high noise levels and time varying additive bi-
ases. We formulate the ﬁltering problem as deterministic observer
kinematics posed directly on the special orthogonal group
(3)
driven by reconstructed attitude and angular velocity measure-
ments. Lyapunov analysis results for the proposed observers are
derived that ensure almost global stability of the observer error.
The approach taken leads to an observer that we term the direct
complementary ﬁlter. By exploiting the geometry of the special or-
thogonal group a related observer, termed the passive complemen-
tary ﬁlter, is derived that decouples the gyro measurements from
the reconstructed attitude in the observer inputs. Both the direct
and passive ﬁlters can be extended to estimate gyro bias online. The
passive ﬁlter is further developed to provide a formulation in terms
of the measurement error that avoids any algebraic reconstruction
of the attitude. This leads to an observer on
(3), termed the
explicit complementary ﬁlter, that requires only accelerometer and
gyro outputs; is suitable for implementation on embedded hard-
ware; and provides good attitude estimates as well as estimating the
gyro biases online. The performance of the observers are demon-
strated with a set of experiments performed on a robotic test-bed
and a radio controlled unmanned aerial vehicle.
Index Terms—Attitude estimates, complementary ﬁlter, non-
linear observer, special orthogonal group.
I. INTRODUCTION
T
HE recent proliferation of microelectromechanical sys-
tems (MEMS) components has lead to the development of
a range of low cost and light weight inertial measurement units.
The low power, light weight and potential for low cost manu-
facture of these units opens up a wide range of applications in
areas such as virtual reality and gaming systems, robotic toys,
and low cost mini-aerial-vehicles (MAVs) such as the Hovereye
(Fig. 1). The signal output of low cost IMU systems, however,
is characterized by low-resolution signals subject to high noise
levels as well as general time-varying bias terms. The raw sig-
nals must be processed to reconstruct smoothed attitude esti-
mates and bias-corrected angular velocity measurements. For
many of the low cost applications considered the algorithms
Manuscript received November 8, 2006; revised August 3, 2007. Published
August 27, 2008 (projected). Recommended by Associate Editor S. Celikovsky.
R. Mahony is with Department of Engineering, Australian National Univer-
sity, ACT, 0200, Australia (e-mail: Robert.Mahony@anu.edu.au).
T. Hamel is with the I3S-CNRS, 06903 Sophia Antipolis, France (e-mail:
thamel@i3s.unice.fr).
J.-M. Pﬂimlin is with the Department of Navigation, Dassault Aviation,
92210 Saint Cloud, Paris, France (e-mail: Jean-Michel.Pﬂimlin@dassault-avi-
ation.com).
Color versions of one or more of the ﬁgures in this paper are available online
at http://ieeexplore.ieee.org.
Digital Object Identiﬁer 10.1109/TAC.2008.923738
need to run on embedded processors with low memory and pro-
cessing resources.
There is a considerable body of work on attitude reconstruc-
tionforroboticsandcontrolapplications(forexample[1]–[4]).A
standard approach is to use extended stochastic linear estimation
techniques [5], [6]. An alternative is to use deterministic comple-
mentary ﬁlter and nonlinear observer design techniques [7]–[9].
Recent work has focused on some of the issues encountered for
low cost IMU systems [10]–[12] as well as observer design for
partial attitude estimation [13]–[15]. It is also worth mentioning
therelatedproblemoffusingIMUandvisiondatathatisreceiving
recent attention [16]–[19] and the problem of fusing IMU and
GPS data [20], [9]. Parallel to the work in robotics and control
there is a signiﬁcant literature on attitude heading reference sys-
tems (AHRS) for aerospace applications [21]. An excellent re-
view of attitude ﬁlters is given by Crassidis et al. [22]. The re-
cent interest in small low-cost aerial robotic vehicles has lead to
a renewed interest in lightweight embedded IMU systems [8],
[23][24].Forthelow-costlight-weightsystemsconsidered,linear
ﬁltering techniques have proved extremely difﬁcult to apply ro-
bustly [25] and linear single-input single-output complementary
ﬁlters are often used in practice [24], [26]. A key issue is online
identiﬁcation of gyro bias terms. This problem is also important
in IMU callibration for satellite systems [5], [21], [27]–[30]. An
important development that came from early work on estimation
and control of satellites was the use of the quaternion representa-
tionfortheattitudekinematics[31],[32],[29],[33].Thenonlinear
observer designs that are based on this work have strong robust-
ness properties and deal well with the bias estimation problem
[9],[29].However,apartfromtheearlierworkoftheauthors[14],
[34], [35] and some recent work on invariant observers [36], [37]
there appearsto be almost no workthat considers the formulation
of nonlinear attitude observers directly on the matrix Lie-group
representation of
.
In this paper we study the design of nonlinear attitude ob-
servers on
in a general setting. We term the proposed
observers complementary ﬁlters because of the similarity of
the architecture to that of linear complementary ﬁlters (cf.
Appendix A), although, for the nonlinear case we do not have
a frequency domain interpretation. A general formulation of
the error criterion and observer structure is proposed based on
the Lie-group structure of
. This formulation leads us to
propose two nonlinear observers on
, termed the direct
complementary ﬁlter and passive complementary ﬁlter. The
direct complementary ﬁlter is closely related to recent work
on invariant observers [36], [37] and corresponds (up to some
minor technical differences) to nonlinear observers proposed
using the quaternion representation [9], [29], [31]. We do not
know of a prior reference for the passive complementary ﬁlter.
The passive complementary ﬁlter has several practical advan-
tages associated with implementation and low-sensitivity to
noise. In particular, we show that the ﬁlter can be reformulated
0018-9286/$25.00 © 2008 IEEE
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

1204
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 53, NO. 5, JUNE 2008
Fig. 1. VTOL MAV HoverEye of Bertin Technologies.
in terms of vectorial direction measurements such as those ob-
tained directly from an IMU system; a formulation that we term
the explicit complementary ﬁlter. The explicit complementary
ﬁlter does not require online algebraic reconstruction of atti-
tude, an implicit weakness in prior work on nonlinear attitude
observers [22] due to the computational overhead of the calcula-
tion and poor error characterization of the constructed attitude.
As a result the observer is ideally suited for implementation
on embedded hardware platforms. Furthermore, the relative
contribution of different data can be preferentially weighted
in the observer response, a property that allows the designer
to adjust for application speciﬁc noise characteristics. Finally,
the explicit complementary ﬁlter remains well deﬁned even if
the data provided is insufﬁcient to algebraically reconstruct the
attitude. This is the case, for example, for an IMU with only
accelerometer and rate gyro sensors. A comprehensive stability
analysis is provided for all three observers that proves local
exponential and almost global stability of the observer error
dynamics, that is, a stable linearization for zero error along
with global convergence of the observer error for all initial con-
ditions and system trajectories other than on a set of measure
zero. Although the principal results of the paper are presented
in the matrix Lie group representation of
, the equivalent
quaternion representation of the observers are presented in
an Appendix. The authors recommend that the quaternion
representations are used for hardware implementation.
The body of paper consists of ﬁve sections followed by a
conclusion and two Appendices. Section II provides a quick
overview of the sensor model, geometry of
and intro-
duces the notation used. Section III details the derivation of the
direct and passive complementary ﬁlters. The development here
is deliberately kept simple to be clear. Section IV integrates on-
line bias estimation into the observer design and provides a de-
tailed stability analysis. Section V develops the explicit comple-
mentary ﬁlter, a reformulation of the passive complementary
ﬁlter directly in terms of error measurements. A suite of ex-
perimental results, obtained during ﬂight tests of the Hovereye
(Fig. 1), are provided in Section VI that demonstrate the perfor-
mance of the proposed observers. In addition to the conclusion
(Section VII) there is a short Appendix on linear complementary
ﬁlter design and a second Appendix that provides the equivalent
quaternion formulation of the proposed observers.
II. PROBLEM FORMULATION AND NOTATION
A. Notation and Mathematical Identities
The special orthogonal group is denoted
. The associ-
ated Lie-algebra is the set of anti-symmetric matrices
For any two matrices
then the Lie-bracket (or
matrix commutator) is
. Let
then
we deﬁne
For any
then
is the vector cross product.
The operator
denotes the inverse of the
operator
For any two matrices
the Euclidean matrix
inner product and Frobenius norm are deﬁned
The following identities are used in the paper:
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

MAHONY et al.: NONLINEAR COMPLEMENTARY FILTERS ON THE SPECIAL ORTHOGONAL GROUP
1205
The following notation for frames of reference is used:
•
denotes an inertial (ﬁxed) frame of reference;
•
denotes a body-ﬁxed-frame of reference;
•
denotes the estimator frame of reference.
Let
denote, respectively, the anti-symmetric and sym-
metric projection operators in square matrix space
Let
denote the angle axis coordinates of
. One has [38]
For any
then
. If
then
in angle axis coordinates and
. If
then
has real eigenvalues
, and there exists an
orthogonal diagonalizing transformation
such that
.
For any two signals
are
termed asymptotically dependent if there exists a nondegenerate
function
and a time
such that for any
By the term nondegenerate we mean that the Hessian of
at
any point
is full rank. The two signals are termed asymp-
totically independent if they are not asymptotically dependent.
B. Measurements
The measurements available from a typical inertial measure-
ment unit are 3 axis rate gyros, 3 axis accelerometers and 3 axis
magnetometers. The reference frame of the strap down IMU is
termed the body-ﬁxed-frame
. The inertial frame is denoted
. The rotation
denotes the relative orientation of
with respect to
.
Rate Gyros: The rate gyro measures angular velocity of
relative to
expressed in the body-ﬁxed-frame of
reference
. The error model used in this paper is
where
denotes the true value,
denotes additive
measurement noise and
denotes a constant (or slowly
time-varying) gyro bias.
Accelerometer: Denote the instantaneous linear accelera-
tion of
relative to
, expressed in
, by
. An
ideal accelerometer, ‘strapped down’ to the body-ﬁxed-
frame
, measures the instantaneous linear accelera-
tion of
minus the (conservative) gravitational accel-
eration ﬁeld
(where we consider
expressed in the in-
ertial frame
), and provides a measurement expressed
in the body-ﬁxed-frame
. In practice, the output
from
a MEMS component accelerometer has added bias and
noise,
where
is a bias term and
denotes additive measure-
ment noise. Normally, the gravitational ﬁeld
where
dominates the value of
for sufﬁciently
low frequency response. Thus, it is common to use
as a low-frequency estimate of the inertial
axis expressed
in the body-ﬁxed-frame.
Magnetometer: The magnetometers provide measure-
ments of the magnetic ﬁeld
where
is the Earths magnetic ﬁeld (expressed in the in-
ertial frame),
is a body-ﬁxed-frame expression for the
local magnetic disturbance and
denotes measurement
noise. The noise
is usually quite low for magnetometer
readings, however, the local magnetic disturbance can be
very signiﬁcant, especially if the IMU is strapped down
to an MAV with electric motors. Only the direction of the
magnetometer output is relevant for attitude estimation and
we will use a vectorial measurement
in the following development.
The measured vectors
and
can be used to construct an
instantaneous algebraic measurement,
, of the rotation
where
is the inertial direction of the magnetic ﬁeld in the
locality where data is acquired. The weights
and
are
chosen depending on the relative conﬁdence in the sensor
outputs. Due to the computational complexity of solving an
optimization problem the reconstructed rotation is often ob-
tained in a suboptimal manner where the constraints are applied
in sequence; that is, two degrees of freedom in the rotation
matrix are resolved using the accelerometer readings and the
ﬁnal degree of freedom is resolved using the magnetometer.
As a consequence, the error properties of the reconstructed
attitude
can be difﬁcult to characterize. Moreover, if either
magnetometer or accelerometer readings are unavailable (due
to local magnetic disturbance or high acceleration manoeuvres)
then it is impossible to resolve the vectorial measurements into
a unique instantaneous algebraic measurement of attitude.
C. Error Criteria for Estimation on
Let
denote an estimate of the body-ﬁxed rotation matrix
. The rotation
can be considered as coordinates for
the estimator frame of reference
. It is also associated with
the frame transformation
The goal of attitude estimate is to drive
. The estimation
error used is the relative rotation from body-ﬁxed-frame
to
the estimator frame
(1)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

1206
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 53, NO. 5, JUNE 2008
The proposed observer design is based on Lyapunov stability
analysis. The Lyapunov functions used are inspired by the cost
function
(2)
One has that
(3)
where
is the angle associated with the rotation from
to
frame
. Thus, driving (2) to zero ensures that
.
III. COMPLEMENTARY FILTERS ON
In this section, a general framework for nonlinear comple-
mentary ﬁltering on the special orthogonal group is introduced.
The theory is ﬁrst developed for the idealized case where
and
are assumed to be known and used to drive the ﬁlter
dynamics. Filter design for real world signals is considered in
later sections.
The goal of attitude estimation is to provide a set of dynamics
for an estimate
to drive the error rotation (1)
. The kinematics of the true system are
(4)
where
. The proposed observer equation is posed
directly as a kinematic system for an attitude estimate
on
. The observer kinematics include a prediction term
based on the
measurement and an innovation or correction
term
derived from the error
. The general form
proposed for the observer is
(5)
where
is a positive gain. The term
is expressed in the inertial frame. The body-ﬁxed-frame angular
velocity is mapped back into the inertial frame
. If no
correction term is used
then the error rotation
is
constant
(6)
The correction term
is considered to be in the
estimator frame of reference. It can be thought of as a nonlinear
approximation of the error between
and
as measured from
the frame of reference associated with
. In practice, it will be
implemented as an error between a measured estimate
of
and the estimate
.
The goal of the observer design is to ﬁnd a simple expression
for
that leads to robust convergence of
. In prior work
[34], [35] the authors introduced the following correction term
(7)
Fig. 2. Block diagram of the general form of a complementary ﬁlter on SO(3).
This choice leads to an elegant Lyapunov analysis of the ﬁlter
stability. Differentiating the storage function (2) along trajecto-
ries of (5) yields
(8)
In Mahony et al. [34] a local stability analysis of the ﬁlter dy-
namics (5) is provided based on this derivation. In Section IV a
global stability analysis for these dynamics is provided.
We term the ﬁlter (5) a complementary ﬁlter on
since
it recaptures the block diagram structure of a classical comple-
mentary ﬁlter (cf. Appendix A). In Fig. 2: The “
” operation
is an inverse operation on
and is equivalent to a “-” op-
eration for a linear complementary ﬁlter. The “
” oper-
ation is equivalent to generating the error term “
”. The
two operations
and
are maps from error space
and velocity space into the tangent space of
; operations
that are unnecessary on Euclidean space due to the identiﬁcation
. The kinematic model is the Lie-group equivalent
of a ﬁrst order integrator.
To implement the complementary ﬁlter it is necessary to map
the body-ﬁxed-frame velocity
into the inertial frame. In prac-
tice, the “true” rotation
is not available and an estimate of the
rotation must be used. Two possibilities are considered.
Direct Complementary Filter: The constructed attitude
is used to map the velocity into the inertial frame
A block diagram of this ﬁlter design is shown in Fig. 3. This
approach can be linked to observers documented in earlier work
[31], [29] (cf. Appendix B). The approach has the advantage that
it does not introduce an additional feedback loop in the ﬁlter
dynamics, however, high frequency noise in the reconstructed
attitude
will enter into the feed-forward term of the ﬁlter.
Passive Complementary Filter: The ﬁltered attitude
is
used in the predictive velocity term
(9)
A block diagram of this architecture is shown in Fig. 4. The
advantage lies in avoiding corrupting the predictive angular ve-
locity term with the noise in the reconstructed pose. However,
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

MAHONY et al.: NONLINEAR COMPLEMENTARY FILTERS ON THE SPECIAL ORTHOGONAL GROUP
1207
Fig. 3. Block diagram of the direct complementary ﬁlter on SO(3).
Fig. 4. Block diagram of the passive complementary ﬁlter on SO(3).
the approach introduces a secondary feedback loop in the ﬁlter
and stability needs to be proved.
A key observation is that the Lyapunov stability analysis in
(8) is still valid for (9), since
using the fact that the trace of a commutator is zero,
. The ﬁlter is termed a passive compli-
mentary ﬁlter since the cross coupling between
and
does
not contribute to the derivative of the Lyapunov function. A
global stability analysis is provided in Section IV.
There is no particular theoretical advantage to either the direct
or the passive ﬁlter architecture in the case where exact measure-
ments are assumed. However, it is straightforward to see that the
passive ﬁlter (9) can be written
(10)
This formulation suppresses entirely the requirement to repre-
sent
and
in the inertial frame and leads to
the architecture shown in Fig. 5. The passive complementary
ﬁlter avoids coupling the reconstructed attitude noise into the
predictive velocity term of the observer, has a strong Lyapunov
stability analysis, and provides a simple and elegant realization
that will lead to the results in Section V.
IV. STABILITY ANALYSIS
In this section, the direct and passive complementary ﬁlters
on
are extended to provide online estimation of time-
varying bias terms in the gyroscope measurements and global
stability results are derived. Preliminary results were published
in [34] and [35].
Fig. 5. Block diagram of the simpliﬁed form of the passive complementary
ﬁlter.
For the following work it is assumed that a reconstructed ro-
tation
and a biased measure of angular velocity
are avail-
able
valid for low frequencies
(11a)
for constant bias
(11b)
The approach taken is to add an integrator to the compensator
term in the feedback equation of the complementary ﬁlter.
Let
be positive gains and deﬁne
Direct Complementary Filter With Bias Correction:
(12a)
(12b)
(12c)
Passive Complementary Filter With Bias Correction:
(13a)
(13b)
(13c)
The nonlinear stability analysis is based on the idea of an adap-
tive estimate for the unknown bias value.
Theorem 4.1 [Direct Complementary Filter With Bias
Correction]:
Consider the rotation kinematics (4) for a
time-varying
and with measurements given by
(11). Let
denote the solution of (12). Deﬁne error
variables
and
. Deﬁne
by
(14)
Then:
1) The set
is forward invariant and unstable with respect to
the dynamic system (12).
2) The error
is locally exponentially stable to
.
3) For almost all initial conditions
the trajectory
converges to the trajectory
.
Proof: Substituting for the error model (11), (12a) becomes
Differentiating
it is straightforward to verify that
(15)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

1208
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 53, NO. 5, JUNE 2008
Deﬁne a candidate Lyapunov function by
(16)
Differentiating
one obtains
Substituting for
and
[(12b) and (12c)] one obtains
(17)
Lyapunov’s direct method ensures that
converges asymptoti-
cally to zero [39]. Recalling that
, where
denotes the angle axis coordinates of
. It follows that
implies either
, or
for
. In
the second case one has the condition
. Note that
is also equivalent to requiring
to be symmetric.
It is easily veriﬁed that
is an isolated equilibrium of the
error dynamics (18).
From the deﬁnition of
one has that
on
. We will
prove that
is forward invariant under the ﬁlter dynamics (12).
Setting
in (15) and (12b) yields
(18)
For initial conditions
the solution of
(18) is given by
(19)
We verify that (19) is also a general solution of (15) and (12b).
Differentiating
yields
where the second line follows since
commutes with
and the ﬁnal equality is due to the fact that
, a
consequence of the choice of initial conditions
.
It follows that
on solution of (19) and hence
. Classical uniqueness results verify that (19) is a solution
of (15) and (12b). It remains to show that such solutions remain
in
for all time. The condition on
is proved above. To see
that
we compute
as
. This proves that
is forward invariant.
Applying LaSalle’s principle to the solutions of (12) it fol-
lows that either
asymptotically or
where
is a solution of (18).
To determine the local stability properties of the invariant
sets we compute the linearization of the error dynamics. We
will prove exponential stability of the isolated equilibrium point
ﬁrst and then return to prove instability of the set
. De-
ﬁne
as the ﬁrst order approximations of
and
around
(20a)
(20b)
The sign change in (20b) simpliﬁes the analysis of the lineariza-
tion. Substituting into (15), computing and discarding all terms
of quadratic or higher order in
yields
(21)
For positive gains
the linearized error system is
strictly stable. This proves part ii) of the theorem statement.
To prove that
is unstable, we use the quaternion formula-
tion (see Appendix B). Using (49), the error dynamics of the
quaternion
associated to the rotation
is given by
(22a)
(22b)
(22c)
It is straightforward to verify that the invariant set associated to
the error dynamics is characterized by
Deﬁne
, then an equivalent characterization of
is
given by
. We study the stability properties of the
equilibrium
of
evolving under the ﬁlter dynamics
(12). Combining (22a) and (22c), one obtains the following dy-
namics for
:
Linearizing around small values of
one obtains
Since
and
are positive gains it follows that the lineariza-
tion is unstable around the point
and this completes the
proof of part i).
The linearization of the dynamics around the unstable set is
either strongly unstable (for large values of
) or hyperbolic
(both positive and negative eigenvalues). Since
depends on
the initial condition then there will be trajectories that converge
to
along the stable center manifold [39] associated with the
stable direction of the linearization. From classical center mani-
fold theory it is known that such trajectories are measure zero in
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

MAHONY et al.: NONLINEAR COMPLEMENTARY FILTERS ON THE SPECIAL ORTHOGONAL GROUP
1209
the overall space. Observing in addition that
is measure zero
in
proves part iii) and the full proof is complete.
The direct complimentary ﬁlter is closely related to quater-
nion based attitude ﬁlters published over the last ﬁfteen years
[31], [9], [29]. Details of the similarities and differences is given
in Appendix B where we present quaternion versions of the
ﬁlters we propose in this paper. Apart from the formulation
directly on
, the present paper extends earlier work by
proposing globally deﬁned observer dynamics and a full global
analysis. To the authors best understanding, all prior published
algorithms depend on a
term that is discontinuous on
(14). Given that the observers are not well deﬁned on the set
the analysis for prior work is necessarily nonglobal. However,
having noted this, the recent work of Thienel et al. [29] pro-
vides an elegant powerful analysis that transforms the observer
error dynamics into a linear time-varying system (the transfor-
mation is only valid on a domain on
) for which
global asymptotic stability is proved. This analysis provides a
global exponential stability under the assumption that the ob-
server error trajectory does not intersect
. In all practical situ-
ations the two approaches are equivalent.
The remainder of the section is devoted to proving an
analogous result to Theorem 4.1 for the passive complemen-
tary ﬁlter dynamics. In this case, it is necessary to deal with
nonautonomous terms in the error dynamics due to passive
coupling of the driving term
into the ﬁlter error dynamics.
Interestingly, the nonautonomous term acts in our favour to
disturb the forward invariance properties of the set
(14) and
reduce the size of the unstable invariant set.
Theorem 4.2 [Passive complementary ﬁlter with bias
correction]:
Consider the rotation kinematics (4) for a
time-varying
and with measurements given
by (11). Let
denote the solution of (13). Deﬁne
error variables
and
. Assume that
is a bounded, absolutely continuous signal and that the
pair of signals
are asymptotically independent (see
Section II-A). Deﬁne
by
(23)
Then:
1) The set
is forward invariant and unstable with respect
to the dynamic system 13.
2) The error
is locally exponentially stable to
.
3) For almost all initial conditions
the trajec-
tory
converges to the trajectory
.
Proof: Substituting for the error model (11) in (13) and
differentiating
, it is straightforward to verify that
(24a)
(24b)
The proof proceeds by differentiating the Lyapunov-like func-
tion (16) for solutions of (13). Following an analogous deriva-
tion to that in Theorem 4.1, but additionally exploiting the can-
cellation
, it may be veriﬁed that
where
is given by (24). This bounds
, and it fol-
lows is bounded. LaSalle’s principle cannot be applied directly
since the dynamics (24a) are not autonomous. The function
is uniformly continuous since the derivative
is uniformly bounded. Applying Barbalat’s lemma proves
asymptotic convergence of
to zero.
Direct substitution shows that
is an equilib-
rium point of (24). Note that
(14) and hence
on
(Th. 4.1). For
the error dynamics (24) become
The solution of this ordinary differential equation is given by
Since
is anti-symmetric for all time then
is
orthogonal and since
it follows
is symmetric for all time. It follows that
is forward in-
variant under the ﬁlter dynamics (13). We prove by contradic-
tion that
is the largest forward invariant set of the
closed-loop dynamics (13) such that
. Assume that there
exits
such that
remains in
for
all time. One has that
on this trajectory. Conse-
quently,
(25)
where we have used
(26)
several times in simplifying expressions. Since
are
asymptotically independent then the relationship (25) must be
degenerate. This implies that there exists a time
such that for
all
then
and contradicts the assumption.
It follows that either
asymptotically or
.
Analogously to Theorem 4.1 the linearization of the error dy-
namics (24) at
is computed. Let
and
for
. The linearized dynamics are the time-varying
linear system
Let
denote the magnitude bound on
and choose
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

1210
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 53, NO. 5, JUNE 2008
Set
to be matrices
(27)
It is straightforward to verify that
and
are positive def-
inite matrices given the constraints on
. Consider
the cost function
, with
. Differ-
entiating
yields
(28)
It is straightforward to verify that
This proves exponential stability of the linearized system at
.
The linearization of the error dynamics on a trajectory in
are also time varying and it is not possible to use the argu-
ment from Theorem 4.1 to prove instability. However, note that
for all
. Moreover, any neigh-
borhood of a point
within the set
contains points
such the
. Trajectories with
these initial conditions cannot converge to
due to the de-
crease condition derived earlier, and it follows that
is un-
stable. Analogous to Theorem 4.1 it is still possible that a set of
measure zero initial conditions, along with very speciﬁc trajec-
tories
, such that the resulting trajectories converge to
.
This proves part iii) and completes the proof.
Apart from the expected conditions inherited from Theorem
4.1 the key assumption in Theorem 4.2 is the independence of
from the error signal
. The perturbation of the passive
dynamics by the independent driving term
provides a distur-
bance that ensures that the adaptive bias estimate converges to
the true gyroscopes’ bias, a particularly useful property in prac-
tical applications.
V. EXPLICIT ERROR FORMULATION OF THE PASSIVE
COMPLEMENTARY FILTER
A weakness of the formulation of both the direct and pas-
sive and complementary ﬁlters is the requirement to reconstruct
an estimate of the attitude,
, to use as the driving term for
the error dynamics. The reconstruction cannot be avoided in the
direct ﬁlter implementation because the reconstructed attitude
is also used to map the velocity into the inertial frame. In this
section, we show how the passive complementary ﬁlter may be
reformulated in terms of direct measurements from the inertial
unit.
Let
, denote a set of
known inertial
directions. The measurements considered are body-ﬁxed-frame
observations of the ﬁxed inertial directions
(29)
where
is a noise process. Since only the direction of the mea-
surement is relevant to the observer we assume that
and normalize all measurements to ensure
.
Let
be an estimate of
. Deﬁne
to be the associated estimate of
. For a single direction
, the
error considered is
which yields
For multiple measures
the following cost function is consid-
ered
(30)
where
(31)
Assume linearly independent inertial direction
then the
matrix
is positive deﬁnite
if
. For
then
is positive semi-deﬁnite with one eigenvalue zero. The
weights
are chosen depending on the relative conﬁdence
in the measurements
. For technical reasons in the proof of
Theorem 5.1 we assume additionally that the weights
are
chosen such that
has three distinct eigenvalues
.
Theorem 5.1 [Explicit complementary ﬁlter with bias
correction]:
Consider the rotation kinematics (4) for a
time-varying
and with measurements given by
(29) and (11b). Assume that there are two or more,
vectorial measurements
available. Choose
such that
(deﬁned by (31)) has three distinct eigenvalues. Consider
the ﬁlter kinematics given by
(32a)
(32b)
(32c)
and let
denote the solution of (32). Assume that
is a bounded, absolutely continuous signal and that the
pair of signals
are asymptotically independent (see
Section II-A). Then:
1) There are three unstable equilibria of the ﬁlter character-
ized by
where
and
are diagonal matrices with entries
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

MAHONY et al.: NONLINEAR COMPLEMENTARY FILTERS ON THE SPECIAL ORTHOGONAL GROUP
1211
as shown and
such that
where
is a diagonal matrix.
2) The error
is locally exponentially stable to
.
3) For almost all initial conditions
, the trajectory
converges to the trajec-
tory
.
Proof: Deﬁne a candidate Lyapunov-like function by
The derivative of
is given by
Recalling that the trace of a commutator is zero, the derivative
of the candidate Lyapunov function can be simpliﬁed to obtain
(33)
Recalling the identities in Section II-A, one may write
as
(34)
Introducing the expressions of
into the time derivative
of the Lyapunov-like function
, (33), one obtains
The Lyapunov-like function derivative is negative semi-deﬁnite
ensuring that
is bounded. Analogous to the proof of The-
orem 4.2, Barbalat’s lemma is invoked to show that
tends to zero asymptotically. Thus, for
one has
(35)
We prove next (35) implies either
or
.
Since
is a real matrix, the eigenvalues and eigenvectors of
verify
and
(36)
where
(for
) represents the complex conjugate of
the eigenvalue
and
represents the Hermitian transpose of
the eigenvector
associated to
. Combining (35) and (36),
one obtains
Note that for
is positive deﬁnite and
. One has
for all
. In the case
when
, it is simple to verify that two of the three eigen-
values are real. It follows that all three eigenvalues of
are
real since complex eigenvalues must come in complex conju-
gate pairs. The eigenvalues of an orthogonal matrix are of the
form
where
is the angle from the angle axis representation. Given
that all the eigenvalues are real it follows that
or
.
The ﬁrst possibility is the desired case
. The
second possibility is the case where
.
When
then (32) and (13) lead to identical error dy-
namics. Thus, we use the same argument as in Theorem 4.2 to
prove that
on the invariant set. To see that the only forward
invariant subsets are the unstable equilibria as characterized in
part i) of the theorem statement we introduce
. Ob-
serve that
Analogous to (35), this implies
or
on the
set
and
. Set
. Then
As
has three distinct eigenvalues, it follows that
for all
and thus
is diagonal. Therefore, there are
four isolated equilibrium points
(where
are speciﬁed in part i) of the theorem statement)
and
that satisfy the condition
. The case
(where
) corresponds to the equi-
librium
while we will show that the other three
equilibria are unstable.
We proceed by computing the dynamics of the ﬁlter in the
new
variable and using these dynamics to prove the stability
properties of the equilibria. The dynamics associated to
are
Setting
, one obtains
(37)
The dynamics of the new estimation error on the bias
are
(38)
The dynamics of
(37) and (38) are an alternative formu-
lation of the error dynamics to
.
Consider a ﬁrst order approximation of
(37) and (38)
around an equilibrium point
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

1212
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 53, NO. 5, JUNE 2008
The linearization of (37) is given by
and thus
and ﬁnally
for
and where
is speciﬁed in part i) of the theorem
statement. Deﬁne
Setting
and
one may write the lineariza-
tion (37) as
We continue by computing the linearization of . Equation
(37) may be approximated to a ﬁrst order by
and thus
Finally, for
Rewriting in terms of the variables
and setting
one obtains
for
The combined error dynamic linearization in the primed coor-
dinates is
(39)
To complete the proof of part i) of the theorem statement we
will prove that the three equilibria associated with
for
are unstable. The demonstration is analogous
to the proof of the Chetaev’s Theorem (see [39, pp. 111–112]).
Consider the following cost function:
It is straightforward to verify that its time derivative is always
positive
Note that for
then
has at least one element of
the diagonal positive. For each
and
, deﬁne
and note that
is non-null for all
. Let
such
that
. A trajectory
initialized at
will
diverge from the compact set
since
on
. How-
ever, the trajectory cannot exit
through the surface
since
along the trajectory. Restricting
such
that the linearization is valid, then the trajectory must exit
through the sphere
. Consequently, trajectories initially
arbitrarily close to
will diverge. This proves that the point
is locally unstable.
To prove local exponential stability of
we
consider the linearization (39) for
. Note that
and
. Set
and
. Then
are positive deﬁnite and (39) may be written as
Consider a cost function
with
given by (27).
Analogous to (28), the time derivative of
is given by
Once again, it is straightforward to verify that
where
is deﬁned in (27) and this proves local exponential
stability of
.
The ﬁnal statement of the theorem follows directly from the
above results along with classical dynamical systems theory and
the proof is complete.
Remark: If
, the weights
, and the measured
directions are orthogonal
then
.
The cost function
becomes
In this case, the explicit complementary ﬁlter (32) and the pas-
sive complementary ﬁlter (13) are identical.
Remark: It is possible to weaken the assumptions in Theorem
5.1 to allow any choice of gains
and any structure of the ma-
trix
and obtain analogous results. The case where all three
eigenvalues of
are equal is equivalent to the passive comple-
mentary ﬁlter scaled by a constant. The only other case, where
, has
for
. (Note that the situation where
is
considered in Corollary 5.2.) It can be shown that any sym-
metry
with
satisﬁes
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

MAHONY et al.: NONLINEAR COMPLEMENTARY FILTERS ON THE SPECIAL ORTHOGONAL GROUP
1213
and it is relatively straightforward to verify that this
set is forward invariant under the closed-loop ﬁlter dynamics.
This invalidates part i) of Theorem 5.1 as stated, however, it
can be shown that the new forward invariant points are unstable
as expected. To see this, note that any
in this set cor-
responds to the minimal cost of
on
. Consequently,
any neighborhood of
contains points
such that
and the Lyapunov decrease condition en-
sures instability. There is still a separate isolated unstable equi-
librium in
, and the stable equilibrium, that must be treated
in the same manner as undertaken in the formal proof of The-
orem 5.1. Following through the proof yields analogous results
to Theorem 5.1 for arbitrary choice of gains
.
The two typical measurements obtained from an IMU unit are
estimates of the gravitational, , and magnetic,
, vector ﬁelds
In this case, the cost function
becomes
The weights
and
are introduced to weight the conﬁdence
in each measure. In situations where the IMU is subject to high
magnitude accelerations (such as during takeoff or landing ma-
noeuvres) it may be wise to reduce the relative weighting of the
accelerometer data
compared to the magnetometer
data. Conversely, in many applications the IMU is mounted in
the proximity to powerful electric motors and their power supply
busses leading to low conﬁdence in the magnetometer readings
(choose
). This is a very common situation in the case
of mini aerial vehicles with electric motors. In extreme cases
the magnetometer data is unusable and provides motivation for
a ﬁlter based solely on accelerometer data.
A. Estimation From the Measurements of a Single Direction
Let
be a measured body ﬁxed frame direction associated
with a single inertial direction
. Let
be an
estimate
. The error considered is
Corollary 5.2: Consider the rotation kinematics (4) for a
time-varying
and with measurements given
by (29) (for a single measurement
) and (11b). Let
denote the solution of (32). Assume that
is
a bounded, absolutely continuous signal and
are
asymptotically independent (see Section II-A). Deﬁne
Then:
1) The set
is forward invariant and unstable under the
closed-loop ﬁlter dynamics.
2) The estimate
is locally exponentially stable to
.
3) For almost all initial conditions
then
converges to the trajectory
.
Proof: The dynamics of
are given by
(40)
Deﬁne the following storage function:
The derivative of
is given by
The Lyapunov-like function
derivative is negative semi-def-
inite ensuring that
is bounded and
. The set
is characterized by
and thus
Consider a trajectory
that satisﬁes the ﬁlter dy-
namics and for which
for all time. One has
Differentiating this expression again one obtains
Since the signals
and
are asymptotically independent it
follows that the functional expression on the left-hand side is
degenerate. This can only hold if
. For
, this
set of trajectories is characterized by the deﬁnition of
. It is
straightforward to adapt the arguments in Theorems 4.1 and 4.2
to see that this set is forward invariant. Note that for
then
. It is direct to see that
lies on a local
maximum of
and that any neighborhood contains points
such that the full Lyapunov function
is strictly less than its
value on the set
. This proves instability of
and completes
part i) of the corollary.
The proof of part ii) and part iii) is analogous to the proof of
Theorem 5.1 (see also [15]).
An important aspect of Corollary 5.2 is the convergence of
the bias terms in all degrees of freedom. This ensures that, for
a real world system, the drift in the attitude estimate around the
unmeasured axis
will be driven asymptotically by a zero
mean noise process rather than a constant bias term. This makes
the proposed ﬁlter a practical algorithm for a wide range of MAV
applications.
VI. EXPERIMENTAL RESULTS
In this section, we present experimental results to demon-
strate the performance of the proposed observers.
Experiments were undertaken on two real platforms to
demonstrate the convergence of the attitude and gyro bias
estimates.
1) The ﬁrst experiment was undertaken on a robotic ma-
nipulator with an IMU mounted on the end effector and
supplied with synthetic estimates of the magnetic ﬁeld
measurement. The robotic manipulator was programmed
to simulate the movement of a ﬂying vehicle in hov-
ering ﬂight regime. The ﬁlter estimates are compared to
orientation measurements computed from the forward
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

1214
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 53, NO. 5, JUNE 2008
Fig. 6. Euler angles from direct and passive complementary ﬁlters.
kinematics of the manipulator. Only the passive and direct
complimentary ﬁlters were run on this test bed.
2) The second experiment was undertaken on the VTOL MAV
HoverEye developed by Bertin Technologies (Fig. 1). The
VTOL belongs to the class of “sit on tail” ducted fan
VTOL MAV, like the iSTAR9 and Kestrel developed
respectively by Allied Aerospace [40] and Honeywell
[41]. It was equipped with a low-cost IMU that consists
of three axis accelerometers and three axis gyroscopes.
Magnetometers were not integrated in the MAV due to
perturbations caused by electrical motors. The explicit
complementary ﬁlter was used in this experiment.
For both experiments the gains of the proposed ﬁlters were
chosen to be:
and
. The iner-
tial data was acquired at rates of 25 Hz for the ﬁrst experiment
and 50 Hz for the second experiment. The quaternion version of
the ﬁlters (Appendix B) were implemented with ﬁrst order Euler
numerical integration followed by rescaling to preserve the unit
norm condition.
Experimental results for the direct and passive versions of the
ﬁlter are shown in Figs. 6 and 7. In Fig. 6, the only signiﬁcant
difference between the two responses lies in the initial transient
responses. This is to be expected, since both ﬁlters will have the
same theoretical asymptotic performance. In practice, however,
the increased sensitivity of the direct ﬁlter to noise introduced
in the computation of the measured rotation
is expected to
contribute to slightly higher noise in this ﬁlter compared to the
passive.
The response of the bias estimates is shown in Fig. 7. Once
again the asymptotic performance of the ﬁlters is similar after
an initial transient. From this ﬁgure it is clear that the passive
Fig. 7. Bias estimation from direct and passive complementary ﬁlters.
Fig. 8. Estimation results of the Pitch and roll angles.
ﬁlter displays slightly less noise in the bias estimates than for
the direct ﬁlter (note the different scales in the -axis).
Figs. 8 and 9 relate to the second experiment. The experi-
mental ﬂight of the MAV was undertaken under remote control
by an operator. The experimental ﬂight plan used was: First,
the vehicle was located on the ground, initially headed toward
. After take off, the vehicle was stabilized in hovering
condition, around a ﬁxed heading which remains close the initial
heading of the vehicle on the ground. Then, the operator engages
a
90 -left turn manoeuvre, returns to the initial heading, and
follows with a
90 -right turn manoeuvre, before returning to
the initial heading and landing the vehicle. After landing, the
vehicle is placed by hand at its initial pose such that ﬁnal and
initial attitudes are the identical.
Fig. 8 plots the pitch and roll angles
estimated di-
rectly from the accelerometer measurements against the esti-
mated values from the explicit complementary ﬁlter. Note the
large amounts of high frequency noise in the raw attitude esti-
mates. The plots demonstrate that the ﬁlter is highly successful
in reconstructing the pitch and roll estimates.
Fig. 9 presents the gyros bias estimation verses the pre-
dicted yaw angle
based on open loop integration of the
gyroscopes. Note that the explicit complementary ﬁlter here is
based solely on estimation of the gravitational direction. Con-
sequently, the yaw angle is the indeterminate angle that is not
directly stabilized in Corollary 5.2. Fig. 9 demonstrates that the
proposed ﬁlter has successfully identiﬁed the bias of the yaw
axis gyro. The ﬁnal error in yaw orientation of the microdrone
after landing is less than 5 over a two minute ﬂight. Much of
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

MAHONY et al.: NONLINEAR COMPLEMENTARY FILTERS ON THE SPECIAL ORTHOGONAL GROUP
1215
Fig. 9. Gyros bias estimation and inﬂuence of the observer on yaw angle.
this error would be due to the initial transient when the bias
estimate was converging. Note that the second part of the ﬁgure
indicates that the bias estimates are not constant. Although
some of this effect may be numerical, it is also to be expected
that the gyro bias on low cost IMU systems are highly suscep-
tible to vibration effects and changes in temperature. Under
ﬂight conditions changing engine speeds and aerodynamic
conditions can cause quite fast changes in gyro bias.
VII. CONCLUSION
This paper presents a general analysis of attitude observer de-
sign posed directly on the special orthogonal group. Three non-
linear observers, ensuring almost global stability of the observer
error, are proposed:
Direct Complementary Filter: A nonlinear observer posed
on
that is related to previously published nonlinear ob-
servers derived using the quaternion representation of
.
Passive Complementary Filter: A nonlinear ﬁlter equation
that takes advantage of the symmetry of
to avoid trans-
formation of the predictive angular velocity term into the esti-
mator frame of reference. The resulting observer kinematics are
considerably simpliﬁed and avoid coupling of constructed atti-
tude error into the predictive velocity update.
Explicit Complementary Filter: A reformulation of the pas-
sive complementary ﬁlter in terms of direct vectorial measure-
ments, such as gravitational or magnetic ﬁeld directions ob-
tained for an IMU. This observer does not require online al-
gebraic reconstruction of attitude and is ideally suited for im-
plementation on embedded hardware platforms. Moreover, the
ﬁlter remains well conditioned in the case where only a single
vector direction is measured.
The performance of the observers was demonstrated in a suite
of experiments. The explicit complementary ﬁlter is now im-
plemented as the primary attitude estimation system on several
MAV vehicles world wide.
APPENDIX A
A REVIEW OF COMPLEMENTARY FILTERING
Complementary ﬁlters provide a means to fuse multiple inde-
pendent noisy measurements of the same signal that have com-
plementary spectral characteristics [11]. For example, consider
two measurements
and
of a signal
where
is predominantly high frequency noise and
is a pre-
dominantly low frequency disturbance. Choosing a pair of com-
plementary transfer functions
with
low pass and
high pass, the ﬁltered estimate is given by
The signal
is all pass in the ﬁlter output while noise com-
ponents are high and low pass ﬁltered as desired. This type of
ﬁlter is also known as distorsionless ﬁltering since the signal
is not distorted by the ﬁlter [42]. Complementary ﬁlters
are particularly well suited to fusing low bandwidth position
measurements with high band width rate measurements for ﬁrst
order kinematic systems. Consider the linear kinematics
(41)
with typical measurement characteristics
(42)
where
is low pass ﬁlter associated with sensor character-
istics,
represents noise in both measurements and
is a
deterministic perturbation that is dominated by low-frequency
content. Normally the low pass ﬁlter
over the fre-
quency range on which the measurement
is of interest. The
rate measurement is integrated
to obtain an estimate of
the state and the noise and bias characteristics of the integrated
signal are dominantly low frequency effects. Choosing
with
all pass such that
over the bandwidth
of
. Then
Note that even though
is high pass the noise
is low pass ﬁltered. In practice, the ﬁlter structure is imple-
mented by exploiting the complementary sensitivity structure of
a linear feedback system subject to load disturbance. Consider
the block diagram in Fig. 10. The output
can be written
where
is the sensitivity function of the closed-loop system
and
is the complementary sensitivity. This architecture is
easy to implement efﬁciently and allows one to use classical
control design techniques for
in the ﬁlter design. The sim-
plest choice is a proportional feedback
. In this case
the closed-loop dynamics of the ﬁlter are given by
(43)
The
frequency
domain
complementary
ﬁlters
associ-
ated with this choice are
and
. Note that the crossover frequency for
the ﬁlter is at
. The gain
is typically chosen
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 14

1216
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 53, NO. 5, JUNE 2008
Fig. 10. Block diagram of a classical complementary ﬁlter.
based on the low pass characteristics of
and the low fre-
quency noise characteristics of
to choose the best crossover
frequency to tradeoff between the two measurements. If the rate
measurement bias,
, is a constant then it is natural to
add an integrator to the compensator to make the system type I
(44)
A type I system will reject the constant load disturbance
from the output. Gain design for
and
is typically based
on classical frequency design methods. The nonlinear develop-
ment in the body of the paper requires a Lyapunov analysis of
closed-loop system (43). Applying the PI compensator, (44),
one obtains state space ﬁlter with dynamics
The negative sign in the integrator state is introduced to indicate
that the state
will cancel the bias in
. Consider the Lyapunov
function
Abusing notation for the noise processes, and using
,
and
, one has
In the absence of noise one may apply Lyapunov’s direct
method to prove convergence of the state estimate. LaSalle’s
principal of invariance may be used to show that
. When
the underlying system is linear, then the linear form of the
feedback and adaptation law ensure that the closed-loop system
is linear and stability implies exponential stability.
APPENDIX B
QUATERNION REPRESENTATIONS OF OBSERVERS
The unit quaternion representation of rotations is commonly
used for the realization of algorithms on
since it of-
fers considerable efﬁciency in code implementation. The set of
quaternions is denoted
.
The set
is a group under the operation
with identity element
. The group of quaternions
are homomorphic to
via the map
This map is a two to one mapping of
onto
with kernel
, thus,
is locally isomorphic to
via
. Given
such that
then
Let
de-
note a body-ﬁxed frame velocity, then the pure quaternion
is associated with a quaternion velocity. Con-
sider the rotation kinematics on
Equation (4), then the
associated quaternion kinematics are given by
(45)
Let
be a low frequency measure of , and
(for
constant bias ) be the angular velocity measure. Let
denote
the observer estimate and quaternion error
Note that
where
is the angle axis representation of
.
The quaternion representations of the observers proposed in this
paper are as follows.
Direct Complementary Filter (12):
(46a)
(46b)
Passive Complementary Filter (13):
(47a)
(47b)
Explicit Complementary Filter (32):
(48a)
(48b)
(48c)
The error dynamics associated with the direct ﬁlter expressed in
the quaternion formulation are
(49)
The error dynamics associated with the passive ﬁlter are
(50)
There is a 15-year history of using the quaternion representation
and Lyapunov design methodology for ﬁltering on
(for
example, cf. [9], [29], and [31]). To the authors’ knowledge the
Lyapunov analysis in all cases has been based around the cost
function
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 15

MAHONY et al.: NONLINEAR COMPLEMENTARY FILTERS ON THE SPECIAL ORTHOGONAL GROUP
1217
Due to the unit norm condition it is straightforward to show that
The cost function proposed in this paper is
(3). It is straightforward to see that the quadratic approximation
of both cost functions around the point
is the quadratic
. The quaternion cost function
, however, is nondiffer-
entiable at the point
while the cost
has a
smooth local maxima at this point. To the authors understanding,
all quaternion ﬁlters in the published literature have a similar
ﬂavour that dates back to the seminal work of Salcudean [31].
The closest published work to that undertaken in the present
paper was published by Thienel in her doctoral dissertation [43]
and transactions paper [29]. The ﬁlter considered by Thienel et
al. is given by
(51a)
(51b)
The
term enters naturally in the ﬁlter design from the
differential,
, of the absolute value term in
the cost function
, during the Lyapunov design process. Con-
sider the observer obtained by replacing
in (51) by
.
Note that with this substitution, (51b) is transformed into (46b).
To show that (51a) transforms to (46a) it is sufﬁcient to show
that
. This is straightforward from
This demonstrates that the quaternion ﬁlter (51) is obtained from
the standard form of the complimentary ﬁlter proposed (12) with
the correction term (12c) replaced by
Note that the correction term deﬁned in (12c) can be written
. It follows that
The correction term for the two ﬁlters varies only by the posi-
tive scaling factor
. The quaternion correction term
is not well deﬁned for
(where
) and these
points are not well deﬁned in the ﬁlter dynamics (51). It should
be noted, however, that
is bounded at
and, apart from
possible switching behavior, the ﬁlter can still be implemented
on the remainder of
. An argument for the use of the
correction term
is that the resulting error dynamics strongly
force the estimate away from the unstable set
[cf. (14)]. An
argument against its use is that, in practice, such situations will
only occur due to extreme transients that would overwhelm the
bounded correction term
in any case, and cause the numer-
ical implementation of the ﬁlter to deal with a discontinuous
argument. In practice, it is an issue of little signiﬁcance since
the ﬁlter will general work sufﬁciently well to avoid any issues
with the unstable set
. For
, corresponding to
,
the correction term
scales to a factor of
the correction
term
. A simple scaling factor like this is compensated for the
in choice of ﬁlter gains
and
and makes no difference to
the performance of the ﬁlter.
REFERENCES
[1] J. Vaganay, M. Aldon, and A. Fournier, “Mobile robot attitude esti-
mation by fusion of inertial data,” in Proc. IEEE Int. Conf. Robotics
Automation (ICRA), 1993, vol. 1, pp. 277–282.
[2] E. Foxlin, M. Harrington, and Y. Altshuler, “Miniature 6-DOF iner-
tial system for tracking HMD,” in Proc. SPIE, Orlando, FL, 1998, vol.
3362, pp. 214–228.
[3] J. Balaram, “Kinematic observers for articulated robers,” in Proc. IEEE
Int. Conf. Robotics Automation, 2000, pp. 2597–2604.
[4] J. L. Marins, X. Yun, E. R. Backmann, R. B. McGhee, and M. Zyda,
“An extended kalman ﬁlter for quaternion-based orientation estimation
using marg sensors,” in IEEE/RSJ Int. Conf. Intelligent Robots Systems,
2001, pp. 2003–2011.
[5] E. Lefferts, F. Markley, and M. Shuster, “Kalman ﬁltering for space-
craft attitude estimation,” AIAA J. Guidance, Control, Navig., vol. 5,
no. 5, pp. 417–429, Sep. 1982.
[6] B. Barshan and H. Durrant-Whyte, “Inertial navigation systems for mo-
bile robots,” IEEE Trans. Robot. Autom., vol. 44, no. 4, pp. 751–760,
1995.
[7] M. Zimmerman and W. Sulzer, “High bandwidth orientation measure-
ment and control based on complementary ﬁltering,” presented at the
Symp. Robotics Control (SYROCO), Vienna, Austria, 1991.
[8] A.-J. Baerveldt and R. Klang, “A low-cost and low-weight attitude esti-
mation system for an autonomous helicopter,” in Proc. IEEE Int. Conf.
Intell. Eng. Syst., 1997, pp. 391–395.
[9] B. Vik and T. Fossen, “A nonlinear observer for GPS and ins integra-
tion,” in Proc. IEEE Conf. Decision and Control, Orlando, FL, Dec.
2001, pp. 2956–2961.
[10] H. Rehbinder and X. Hu, “Nonlinear state estimation for rigid body
motion with low-pass sensors,” Syst. Control Lett., vol. 40, no. 3, pp.
183–190, 2000.
[11] E. R. Bachmann, J. L. Marins, M. J. Zyda, R. B. Mcghee, and X. Yun,
“An extended Kalman ﬁlter for quaternion-based orientation estima-
tion using MARG sensors,” in Proc. IEEE/RSJ Intelligent Robots and
Systems, Maoui, HI, 2001, pp. 2003–2011, .
[12] J.-M. Pﬂimlin, T. Hamel, P. Soueeres, and N. Metni, “Nonlinear atti-
tude and gyroscoples bias estimation for a VTOL UAV,” in Proc. IFAC
World Congr., 2005.
[13] H. Rehbinder and X. Hu, “Drift-free attitude estimation for accelerated
rigid bodies,” Automatica, 2004.
[14] N. Metni, J.-M. Pﬂimlin, T. Hamel, and P. Soueeres, “Attitude and
gyro bias estimation for a ﬂying UAV,” in Proc. IEEE/RSJ Int. Conf.
Intelligent Robots Systems, Aug. 2005, pp. 295–301.
[15] N. Metni, J.-M. Pﬂimlin, T. Hamel, and P. Soueeres, “Attitude and gyro
bias estimation for a VTOL UAV,” Control Eng. Practice, vol. 14, no.
12, pp. 1511–1520, 2006.
[16] J. Lobo and J. Dias, “Vision and inertial sensor cooperation using
gravity as a vertical reference,” IEEE Trans. Pattern Anal. Mach.
Intell., vol. 25, no. 12, pp. 1597–1608, Dec. 2003.
[17] H. Rehbinder and B. Ghosh, “Pose estimation using line-based dy-
namic vision and inertial sensors,” IEEE Trans. Autom. Control, vol.
48, no. 2, pp. 186–199, Feb. 2003.
[18] J.-H. Kim and S. Sukkarieh, “Airborne simultaneous localisation and
map building,” in Proc. IEEE Int. Conf. Robotics Automation, Taipei,
Taiwan, R.O.C., Sep. 2003, pp. 406–411.
[19] P. Corke, J. Dias, M. Vincze, and J. Lobo, “Integration of vision and
inertial sensors,” presented at the IEEE Int. Conf. Robotics Automation
(ICRA), Barcelona, Spain, Apr. 2004, ser. W-M04 full-day workshop.
[20] R. Phillips and G. Schmidt, in System Implications and Innovative Ap-
plications of Satellite Navigation, 1996, vol. 207, pp. 0.1–0.18 [On-
line]. Available: help@sti.nasa.gov, ser. AGARD Lecture Series 207,
NASA Center for Aerospace Information ch. GPS/INS Integration
[21] D. Gebre-Egziabher, R. Hayward, and J. Powell, “Design of multi-
sensor attitude determination systems,” IEEE Trans. Aerosp. Electron.
Syst., vol. 40, no. 2, pp. 627–649, Apr. 2004.
[22] J. L. Crassidis, F. L. Markley, and Y. Cheng, “Nonlinear attitude ﬁl-
tering methods,” J. Guidance, Control, Dynam., vol. 30, no. 1, pp.
12–28, Jan. 2007.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 16

1218
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 53, NO. 5, JUNE 2008
[23] M. Jun, S. Roumeliotis, and G. Sukhatme, “State estimation of an au-
tonomous helicopter using Kalman ﬁltering,” in Proc. IEEE/RSJ Int.
Conf. Intelligent Robots and Systems, Kyongju, Korea, Oct. 17–21,
1999, pp. 1346–1353.
[24] G. S. Sukhatme, G. Buskey, J. M. Roberts, P. I. Corke, and S. Saripalli,
“A tale of two helicopters,” in Proc. IEEE/RSJ Int. Robots Systems, Las
Vegas, NV, Oct. 2003, pp. 805–810 [Online]. Available: http://www-
robotics.usc.edu/srik/papers/iros2003.pdf
[25] J. M. Roberts, P. I. Corke, and G. Buskey, “Low-cost ﬂight control
system for small autonomous helicopter,” in Proc. Australian Conf.
Robotics Automation, Auckland, New Zealand, Nov. 27–29, 2002, pp.
71–76.
[26] P. Corke, “An inertial and visual sensing system for a small au-
tonomous helicopter,” J. Robot. Syst., vol. 21, no. 2, pp. 43–51, Feb.
2004.
[27] G. Creamer, “Spacecraft attitude determination using gyros and quater-
nion measurements,” J. Astronaut. Sci., vol. 44, no. 3, pp. 357–371, Jul.
1996.
[28] D. Bayard, “Fast observers for spacecraft pointing control,” in Proc.
IEEE Conf. Decision Control, Tampa, FL, 1998, pp. 4702–4707.
[29] J. Thienel and R. M. Sanner, “A coupled nonlinear spacecraft attitude
controller and observer with an unknow constant gyro bias and gyro
noise,” IEEE Trans. Autom. Control, vol. 48, no. 11, pp. 2011–2015,
Nov. 2003.
[30] G.-F. Ma and X.-Y. Jiang, “Spacecraft attitude estimation from vector
measurements using particle ﬁlter,” in Proc. 4th Int. Conf. Machine
Learning Cybernetics, Guangzhou, China, Aug. 2005, pp. 682–687.
[31] S. Salcudean, “A globally convergent angular velocity observer for
rigid body motion,” IEEE Trans. Autom. Cont., vol. 36, no. 12, pp.
1493–1497, Dec. 1991.
[32] O. Egland and J. Godhaven, “Passivity-based adaptive attitude con-
trol of a rigid spacecraft,” IEEE Trans. Autom. Control, vol. 39, pp.
842–846, Apr. 1994.
[33] A. Tayebi and S. McGilvray, “Attitude stabilization of a four-rotor
aerial robot: Theory and experiments,” IEEE Trans. Control Syst.
Technol., vol. 14, no. 3, pp. 562–571, May 2006.
[34] R. Mahony, T. Hamel, and J.-M. Pﬂimlin, “Complimentary ﬁlter design
on the special orthogonal group SO(3),” presented at the IEEE Conf.
Decision Control (CDC), Seville, Spain, Dec. 2005.
[35] T. Hamel and R. Mahony, “Attitude estimation on SO(3) based on di-
rect inertial measurements,” in Proc. Int. Conf. Robotics Automation
(ICRA), Orlando, FL, 2006, pp. 2170–2175.
[36] S. Bonnabel and P. Rouchon, Control and Observer Design for Non-
linear Finite and Inﬁnite Dimensional Systems.
New York: Springer-
Verlag, 2005, pp. 53–67, Vol. 322 ch. On Invariant Observers ser. Lec-
ture Notes in Control and Information Sciences.
[37] S. Bonnabel, P. Martin, and P. Rouchon, “A non-linear symmetry-pre-
serving observer for velocity-aided inertial navigation,” in Proc. Amer.
Control Conf., Jun. 2006, pp. 2910–2914.
[38] R. Murray, Z. Li, and S. Sastry, A Mathematical Introduction to Robotic
Manipulation.
Boca Raton, FL: CRC Press, 1994.
[39] H. Khalil, Nonlinear Systems, 2nd ed.
Englewood Cliffs, NJ: Pren-
tice-Hall, 1996.
[40] L. Lipera, J. Colbourne, M. Tischler, M. Mansur, M. Rotkowitz, and
P. Patangui, “The micro craft istar micro-air vehicle: Control system
design and testing,” in Proc. 57th Annu. Forum Amer. Helicopter Soc.,
Washington, DC, May 2001, pp. 1–11.
[41] J. Fleming, T. Jones, P. Gelhausen, and D. Enns, “Improving control
system effectiveness for ducted fan VTOL UAVs operating in cross-
winds,” in Proc. AIAA 2nd “Unmanned Unlimited” System, San Diego,
CA, Sep. 2003.
[42] R. G. Brown and P. Y. C. Hwang, Introduction to Random Signals and
Applied Kalman Filtering, 2nd ed.
New York, NY: Wiley, 1992.
[43] J. Thienel, “Nonlinear observer/controller designs for spacecraft atti-
tude control systems with uncalibrated gyros,” Ph.D. dissertation, Dept.
Aerosp. Eng., Faculty of the Graduate School, Univ. of Maryland, MD,
2004.
Robert Mahony (S’92–M’95–SM’08) received the
B.Sc. degree in applied mathematics and geology and
the Ph.D. degree in systems engineering both from
the Australian National University (ANU) in 1989
and 1995, respectively.
He worked as a marine seismic geophysicist and an
industrial research scientist before completing a two-
year postdoctoral fellowship in France and a two-year
Logan Fellowship at Monash University, Australia.
He is currently a Reader in the Department of En-
gineering at the Australian National University. His
research interests are in nonlinear control theory with applications in robotics
and geometric optimization techniques.
Tarek Hamel (M’07) received the B.Eng. degree
from the University of Annaba, Algeria, in 1991 and
the Ph.D. degree in robotics from the University of
Technology Compiégne (UTC), France, in 1995.
After two years as a Research Assistant at the
UTC, he joined the Centre d’Etudes de Mècanique
d’Iles de France in 1997 as an Associate Pro-
fessor. Since 2003, he has been a Professor at the
I3S UNSA-CNRS laboratory of the University of
Nice-Sophia Antipolis, France. His research interests
include nonlinear control theory, estimation and
vision-based control with applications to unmanned aerial vehicles and mobile
robots.
Jean-Michel Pﬂimlin received the B.Eng. degree
from Supaero, the French Engineering school in
Aeronautics and Space, in 2003 and the Ph.D.
degree in automatic control from Supaero in 2006.
His Ph.D. research was conducted at the Labo-
ratory for Analysis and Architecture of Systems,
LAAS-CNRS, Toulouse, France.
He is currently working at the Navigation De-
partment of Dassault Aviation, Saint Cloud, Paris,
France. His research interests include nonlinear
control and ﬁltering, advanced navigation systems,
and their applications to unmanned aerial vehicles.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 07:18:14 UTC from IEEE Xplore.  Restrictions apply.
