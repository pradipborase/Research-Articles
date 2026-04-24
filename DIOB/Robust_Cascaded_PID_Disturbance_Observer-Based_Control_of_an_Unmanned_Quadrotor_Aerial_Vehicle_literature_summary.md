# Article Title
Robust_Cascaded_PID_Disturbance_Observer-Based_Control_of_an_Unmanned_Quadrotor_Aerial_Vehicle.pdf

# Source File
`DIOB/Robust_Cascaded_PID_Disturbance_Observer-Based_Control_of_an_Unmanned_Quadrotor_Aerial_Vehicle.md`

# Novelties
- # Robust_Cascaded_PID_Disturbance_Observer-Based_Control_of_an_Unmanned_Quadrotor_Aerial_Vehicle.pdf ## Page 1 Robust cascaded PID disturbance observer-based control of an unmanned quadrotor aerial vehicle Mohammed Hany Mohamed Elsayd Ayman El-Badawy Mechatronics Engineering Department Mechatronics Engineering Department Mechatronics E...
  - Evidence Section: `Method/Discussion context`
- Simulation studies with trajectories subject to Dryden wind disturbances demonstrate that the DOB-enhanced controller achieves superior tracking accuracy compared to the conventional cascaded PID controller achieving reductions in position standard deviation of 26.47%, 39.5%, and 59.7% along the X, Y, and Z axes, respectively.
  - Evidence Section: `Method/Discussion context`
- For the translational motion, the following equations were derived: m¨x = T cos ϕ sin θ −Ax ˙x m¨y = −T sin ϕ −Ay ˙y m¨z = T cos ϕ cos θ −mg −Az ˙z (1) where m is the mass of the quadrotor, g is the acceleration due to gravity, ϕ, θ and ψ are the roll, pitch and yaw angles respectively, Ax, Ay and Az represent the drag coefficients in ...
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- There are two types of disturbances: external disturbances caused by the environment like wind disturbances and input signal fluctuations [14], and internal disturbances caused by uncertainties like modeling errors, parameter changes and sensor noise [15].
  - Evidence Section: `Method/Discussion context`
- Dryden wind modeling In the used model, disturbances are modeled using the Dryden wind model where the gust component of the wind is modeled using the following transfer functions[22]: Hu(s) = ud(s) ηu(s) = σu r 2Va πLu 1 s + Va Lu Hv(s) = vd(s) ηv(s) = σv r 3Va πLv (s + Va √ 3Lv ) (s + Va Lv )2 Hw(s) = wd(s) ηw(s) = σw r 3Va πLw (s + ...
  - Evidence Section: `Method/Discussion context`
- For each operating point, the nominal plant transfer function between one of the three positions (X, Y and Z) and its corresponding desired acceleration (Xd, Yd and Zd) that is produced by the PID controller in the outer loop of the control system was computed to be: Pn(s) =      X(s) Xd(s) = 0.06901s3+52.71s2+3438s+763.8 s5+764.3...
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
