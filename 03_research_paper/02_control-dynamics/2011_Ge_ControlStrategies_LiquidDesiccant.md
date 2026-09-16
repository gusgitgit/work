# Control strategies for a liquid desiccant air-conditioning system

- **Authors**: Gaoming Ge, Fu Xiao, Xiaofeng Niu
- **Journal**: Energy and Buildings, Vol. 43, Issue 8, pp. 1957–1966
- **Publication Year**: 2011
- **DOI**: [10.1016/j.enbuild.2011.02.011](https://doi.org/10.1016/j.enbuild.2011.02.011)
- **Keywords / Tags**: #ControlStrategies #FeedbackControl #DecoupledControl #SensitivityAnalysis

---

### 1. Executive Summary (BLUF)
- Evaluates multivariable control strategies for liquid desiccant air-conditioning systems. Compares direct feedback control loops versus decoupled cascading control.
- Demonstrates that controlling solution temperature via cooling water delivers significantly faster settling times and higher stability than modulating solution flow rate.

### 2. Key Dynamic Insights
- **Control Pairing**: Solution inlet temperature has a strong, monotonic, and rapid effect on air outlet humidity. In contrast, solution flow rate displays nonlinear saturation once complete surface wetting is achieved.
- **Hunting Avoidance**: Throttling solution flow rate under low-load conditions causes flow channeling and severe control hunting.

### 3. Engineering Takeaways for CrecoPLUS DOAS
- Validates the architectural choice: Keep CrecoPLUS 5100C circulation flow constant and modulate the internal cooling water control valve for humidity regulation.
