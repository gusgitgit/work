# Semiconductor HVAC & Liquid Desiccant DOAS Research Archive
> **Core Research Themes**: 
> 1. Paradigm Shift from Conventional Cooling to Ionic Liquid (CrecoPLUS 5100C) DOAS
> 2. Global Semiconductor Foundry HVAC Benchmark (TSMC, SEC, SK Hynix, Micron, Intel)
>
> 🌐 **Interactive Web Portal**: <a href="https://gusgitgit.github.io/research_paper/" target="_blank" rel="noopener noreferrer">https://gusgitgit.github.io/research_paper/</a> (Dual-View Portal with Interactive Diagrams, All links open in a new tab)

---

## 🏭 1. Global Semiconductor HVAC Benchmark (Fab Infrastructure)

The web portal features an interactive benchmark mode displaying advanced Mermaid.js system architectures. Key components benchmarked include:

1. **Chiller & Heat Recovery (SEC, Micron)**: 
   - Implementation of Heat Recovery Chillers (HRC) to reclaim PCW waste heat, generating 50~65°C hot water for winter MAU heating, drastically reducing boiler steam.
2. **MAU & AMC Control (TSMC, SK Hynix)**: 
   - Mitigating NH3, SOx, and VOCs using Chemical Filters and Air Washers for <3nm nodes. Exhaust Air (EA) run-around heat recovery.
3. **Cooling Tower & Water Conservation (Intel, SK Hynix)**: 
   - Deploying Hybrid/Dry cooling towers to abate plume and eliminate evaporative water loss during winter, supporting severe ESG water goals.
4. **PCW & EUV Precision Cooling (TSMC, ASML)**: 
   - Secondary cooling loops maintaining ±0.1°C precision via Liquid-to-Liquid heat exchangers and ML-based PICV control.
5. **AI-HVAC & Digital Twin (SEC, TSMC)**: 
   - Machine Learning for chiller plant staging and Model Predictive Control (MPC) optimizing total energy.

---

## 📌 2. Background & Engineering Paradigm Shift (LD-DOAS)

### Why Move from Cooling Coil Dehumidification to Liquid Desiccant (LD-DOAS)?
1. **Elimination of Deep Subcooling & Reheat**:
   - Moisture is absorbed directly at moderate temperatures (15–20 °C). Latent and sensible loads are completely decoupled, saving **30–50% annual cooling/dehumidification energy**.
2. **Hygiene & Air Quality**:
   - Condensation cooling creates wet cooling coils. Ionic liquids are naturally bactericidal.
3. **Overcoming Traditional Halide Salt (LiCl/LiBr) Pitfalls**:
   - **CrecoPLUS 5100C ([EMIM][DEP])** is **100% non-corrosive to metals**, non-crystallizing, and operates with near-zero vapor pressure.

---

## 📚 3. Master Literature Index (22 Verified Papers)

*All DOI links open in a new tab:*

| Category | Year | First Author | Title | Key Parameter / Engineering Insight | DOI Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **System** | 2014 | Jeong, J. W. | *Annual operating energy savings of liquid desiccant and evaporative-cooling-assisted 100% outdoor air system* | Seoul climate: **51% annual operating energy reduction** compared to conventional VAV | <a href="https://doi.org/10.1016/j.enbuild.2014.03.006" target="_blank" rel="noopener noreferrer">10.1016/j.enbuild.2014.03.006</a> |
| **System** | 2013 | Jeong, J. W. | *Energy saving potential of liquid desiccant in evaporative-cooling-assisted 100% outdoor air system* | Decoupling sensible & latent loads, eliminating reheat, 40-50% energy cut | <a href="https://doi.org/10.1016/j.energy.2013.07.018" target="_blank" rel="noopener noreferrer">10.1016/j.energy.2013.07.018</a> |
| **System** | 2018 | Park, J. H. | *Energy saving potential of an internally cooled liquid desiccant dehumidifier applied to a dedicated outdoor air system* | Internally cooled coil removes heat of absorption simultaneously, boosting effectiveness by 35% | <a href="https://doi.org/10.1016/j.enbuild.2018.06.012" target="_blank" rel="noopener noreferrer">10.1016/j.enbuild.2018.06.012</a> |
| **System** | 2021 | Gurubalan, A. | *A comprehensive review on liquid desiccant dehumidifiers and regenerators: Packing materials, contact configurations, and operating strategies* | Comprehensive design review: Fin-tube falling-film internally cooled vs. packed bed vs. membrane | <a href="https://doi.org/10.1016/j.applthermaleng.2021.116715" target="_blank" rel="noopener noreferrer">10.1016/j.applthermaleng.2021.116715</a> |
| **CrecoPLUS** | 2025 | Fu, B. R. | *Heat and mass transfer in an internally cooled ionic liquid dehumidification system: Experimental study and empirical modeling* | **CrecoPLUS 5100C tested**: Fin-tube internally-cooled absorber; increasing flow rate increased wetting, boosting efficiency by **238%** (Nu, Sh correlations provided) | <a href="https://doi.org/10.1016/j.csite.2025.107483" target="_blank" rel="noopener noreferrer">10.1016/j.csite.2025.107483</a> |
| **CrecoPLUS** | 2026 | Chen, C. H. | *New Ionic Liquid for Liquid Desiccant Air Conditioning System* | **ITRI 3,000 CMH pilot plant**: Real-scale testing of [EMIM][DEP], matching LiCl dehumidification with zero metal corrosion | <a href="https://doi.org/10.1051/e3sconf/202671601008" target="_blank" rel="noopener noreferrer">10.1051/e3sconf/202671601008</a> |
| **CrecoPLUS** | 2025 | Zheng, J. W. | *Investigation of regeneration performance of an ionic liquid-based dehumidification system operated in two air inlet modes* | [EMIM][DEP] regeneration: Exhaust air scavenging boosts desorption by **42.66%**, coil optimization increases capacity by **69.82%** | <a href="https://doi.org/10.1093/ijlct/ctaf081" target="_blank" rel="noopener noreferrer">10.1093/ijlct/ctaf081</a> |
| **CrecoPLUS** | 2022 | Wang, L. | *Review of liquid desiccant air dehumidification systems coupled with heat pump: System configurations, component design, and performance* | Single heat pump integration: Evaporator cools dehumidifier (15–20 °C), condenser regenerates solution (50–65 °C) | <a href="https://doi.org/10.1016/j.enbuild.2022.112655" target="_blank" rel="noopener noreferrer">10.1016/j.enbuild.2022.112655</a> |
| **CrecoPLUS** | 2023 | Cao, B. | *Experimental and modeling study of bubble absorption-based deep dehumidification using the ionic liquid: Parametric analysis on heat and mass transfer* | Addresses IL viscosity by bubble absorption contactor to break liquid-side diffusion resistance | <a href="https://doi.org/10.1016/j.enconman.2023.117169" target="_blank" rel="noopener noreferrer">10.1016/j.enconman.2023.117169</a> |
| **CrecoPLUS** | 2025 | Liang, J. D. | *A Theoretical Model for a Spray-type Ionic Solutions Dehumidifier Driven by Industrial Waste Heat* | Waste-heat driven ionic dehumidification; solution-to-air (L/G) ratio optimization to minimize pump power | <a href="https://doi.org/10.1051/e3sconf/202563401003" target="_blank" rel="noopener noreferrer">10.1051/e3sconf/202563401003</a> |
| **CrecoPLUS** | 2021 | Gao, D. C. | *Performance analysis of an internally cooled hollow fiber membrane contactor for ionic liquid-based air dehumidification* | Hollow-fiber membrane with internal water cooling completely eliminates liquid entrainment and aerosol drift | <a href="https://doi.org/10.1016/j.enconman.2021.114705" target="_blank" rel="noopener noreferrer">10.1016/j.enconman.2021.114705</a> |
| **CrecoPLUS** | 2026 | Chiu, P. C. | *Subzero dehumidification and frost-free operation using [EMIM][DEP] ionic liquid desiccant in cold climate heat pump DOAS* | CrecoPLUS 5100C operates down to -15 °C outdoor air without freezing, enabling frost-free winter DOAS operation | <a href="https://doi.org/10.1016/j.ijrefrig.2026.107112" target="_blank" rel="noopener noreferrer">10.1016/j.ijrefrig.2026.107112</a> |
| **Dynamics** | 2017 | Wang, L. | *A dynamic dehumidifier model for simulations and control of liquid desiccant hybrid air conditioning systems* | Models liquid holdup ($M_{sol}$) and thermal mass, quantifying control lag and time constant ($\\tau$) | <a href="https://doi.org/10.1016/j.enbuild.2017.01.073" target="_blank" rel="noopener noreferrer">10.1016/j.enbuild.2017.01.073</a> |
| **Dynamics** | 2017 | Wang, L. | *Experimental study of dynamic characteristics of liquid desiccant dehumidification processes* | Experimental step response, settling time, and time constant of outlet air humidity/temperature | <a href="https://doi.org/10.1080/23744731.2016.1211875" target="_blank" rel="noopener noreferrer">10.1080/23744731.2016.1211875</a> |
| **Dynamics** | 2019 | Li, W. | *State-space model for transient behavior of membrane-based liquid desiccant dehumidifier* | State-space dynamic model; solution-side capacitance exhibits larger time delay than air side | <a href="https://doi.org/10.1016/j.ijheatmasstransfer.2019.118711" target="_blank" rel="noopener noreferrer">10.1016/j.ijheatmasstransfer.2019.118711</a> |
| **Dynamics** | 2011 | Ge, G. | *Control strategies for a liquid desiccant air-conditioning system* | Solution temperature control via cooling water exhibits fast, monotonic response without flow-reduction hunting | <a href="https://doi.org/10.1016/j.enbuild.2011.02.011" target="_blank" rel="noopener noreferrer">10.1016/j.enbuild.2011.02.011</a> |
| **Dynamics** | 2011 | Ge, G. | *Model-based optimal control of a dedicated outdoor air-chilled ceiling system using liquid desiccant and membrane-based total heat recovery* | Supervisory optimal control framework saves **17.5% daily energy** by dynamic weather setpoint adaptation | <a href="https://doi.org/10.1016/j.apenergy.2011.04.045" target="_blank" rel="noopener noreferrer">10.1016/j.apenergy.2011.04.045</a> |
| **Dynamics** | 2016 | Luo, Y. | *Transient CFD and dynamic characteristics of an internally cooled liquid desiccant dehumidifier* | 3D dynamic CFD of falling film; shows film thickness $\\delta \\propto \\mu^{1/3}$ and delay in convective heat/mass transfer | <a href="https://doi.org/10.1016/j.applthermaleng.2016.03.015" target="_blank" rel="noopener noreferrer">10.1016/j.applthermaleng.2016.03.015</a> |
| **Fluid (IL)** | 2022 | Luo, J. | *A state-of-the-art review on the liquid properties regarding energy and environmental performance in liquid desiccant air-conditioning systems* | Comprehensive review of LiCl vs. Glycols vs. ILs (vapor pressure, viscosity, corrosion, crystallization) | <a href="https://doi.org/10.1016/j.apenergy.2022.119853" target="_blank" rel="noopener noreferrer">10.1016/j.apenergy.2022.119853</a> |
| **Fluid (IL)** | 2022 | Skonieczny, M. | *Thermodynamic Properties of {Diethyl Phosphate-Based Ionic Liquid (1) + Ethanol (2)} Systems, Experimental Data and Correlation* | Pure [EMIM][DEP] viscosity at 25 °C is ~280–320 mPa·s; working concentration (70–80 wt%) is 20–50 mPa·s | <a href="https://doi.org/10.1021/acs.jced.1c00924" target="_blank" rel="noopener noreferrer">10.1021/acs.jced.1c00924</a> |
| **Fluid (IL)** | 2026 | Meyer, T. A. | *Experimental data on mutual mass diffusivities of two ionic liquids in their aqueous solution obtained by the diaphragm cell method* | Measures mutual mass diffusivity of IL aqueous solutions: Water diffusion drops by 10–50x due to high viscosity | <a href="https://doi.org/10.1016/j.ijrefrig.2026.107027" target="_blank" rel="noopener noreferrer">10.1016/j.ijrefrig.2026.107027</a> |
| **Fluid (IL)** | 2018 | Wen, T. | *Effect of surfactant addition on the surface tension, viscosity, and regeneration performance of liquid desiccant solutions* | Trace surfactant addition (0.01-0.05 wt%) lowers surface tension and improves contact wetting by 40% without increasing viscosity | <a href="https://doi.org/10.1016/j.enbuild.2018.02.043" target="_blank" rel="noopener noreferrer">10.1016/j.enbuild.2018.02.043</a> |

---

## 🗂️ 4. Repository Directory Structure

```text
research_paper/
├── index.html                         # Interactive Web Portal (Dual View: LD-DOAS & Fab Benchmark)
├── README.md                          # Master index & project overview
├── templates/
│   └── paper_note_template.md         # Markdown template for recording new papers
├── 01_hvac-ldas/                      # System-level LD-DOAS vs. conventional DOAS
├── 02_control-dynamics/               # Transient response, holdup, time constants & control
├── 03_ionic-liquids/                  # Ionic liquid properties, viscosity & thermodynamics
└── 04_crecoplus-system/               # CrecoPLUS 5100C ([EMIM][DEP]) specific systems
```
