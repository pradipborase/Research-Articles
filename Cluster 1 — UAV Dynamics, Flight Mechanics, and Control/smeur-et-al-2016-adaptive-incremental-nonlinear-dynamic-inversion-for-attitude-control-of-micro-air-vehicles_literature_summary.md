# Article Title
smeur-et-al-2016-adaptive-incremental-nonlinear-dynamic-inversion-for-attitude-control-of-micro-air-vehicles.pdf

# Source File
`Cluster 1 — UAV Dynamics, Flight Mechanics, and Control/smeur-et-al-2016-adaptive-incremental-nonlinear-dynamic-inversion-for-attitude-control-of-micro-air-vehicles.md`

# Novelties
- The main contributions of this article are 1) a proposed method to correctly take into account the delays occurring when deriving angular accelerations from angular rate measurements; 2) the introduction of adaptive incremental nonlinear dynamic inversion, which can estimate the controleffectivenessonline,eliminatingthe needfor manualp...
  - Evidence Section: `Method/Discussion context`
- Theoretically, this method can remove all nonlinearities from the system and create a linearizing control law.
  - Evidence Section: `Method/Discussion context`
- It has been described in the literature since the late 1990s [4,5], sometimes referred to as simplified [6] or enhanced [7] NDI.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- In the context of attitude control of micro air vehicles, incremental nonlinear dynamic inversion only uses a control effectiveness model and usesestimatesof the angularaccelerations toreplace therest of themodel.Thispaperprovidessolutionsfortwo major challenges of incremental nonlinear dynamic inversion control: how to deal with measu...
  - Evidence Section: `Method/Discussion context`
- However, NDI is very sensitive to model inaccuracies [3].
  - Evidence Section: `Method/Discussion context`
- This setup has some drawbacks because it is complex and the accelerometers are sensitive to structural vibrations.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
