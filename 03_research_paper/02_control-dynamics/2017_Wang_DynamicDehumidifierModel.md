# A dynamic dehumidifier model for simulations and control of liquid desiccant hybrid air conditioning systems

- **Authors**: Lingshi Wang, Fu Xiao, Xiaofeng Niu, Dian-ce Gao
- **Journal**: Energy and Buildings, Vol. 139, pp. 441–454
- **Publication Year**: 2017
- **DOI**: [10.1016/j.enbuild.2017.01.073](https://doi.org/10.1016/j.enbuild.2017.01.073)
- **Keywords / Tags**: #DynamicModel #LiquidHoldup #ControlLag #TimeConstant

---

### 1. Executive Summary (BLUF)
- Develops and validates a one-dimensional dynamic model of a packed-bed liquid desiccant dehumidifier explicitly accounting for the **thermal mass of packing material and the dynamic solution holdup ({sol}$)**.
- Demonstrates that static models fail during transients and proves that solution holdup creates significant phase lag and time constants in both outlet air humidity and temperature.

### 2. Key Dynamic & Control Insights
- **Holdup Effect**: The volume of desiccant liquid retained in the contactor ({holdup}$) acts as a dynamic capacitance. Larger liquid holdup directly increases the time constant ($\\tau \\approx M_{sol} / \\dot{m}_{sol}$).
- **Validation**: Simulation vs. experimental RMSE is within 0.2 g/kg for outlet air humidity and 0.2 °C for outlet air temperature.

### 3. Engineering Takeaways for CrecoPLUS DOAS
- With high-viscosity ionic liquids like CrecoPLUS 5100C, falling film thickness is substantially thicker ($\\delta \\propto \\mu^{1/3}$), increasing liquid holdup by 2-3x compared to LiCl.
- Controller tuning must incorporate this enlarged capacitance; standard PID tuning tuned for low-viscosity fluids will cause overshoot and hunting.
