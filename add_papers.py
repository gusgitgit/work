import json

html_path = '03_research_paper/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The papers array is injected like `const papers = [ ... ];`
# Let's find where `const papers = [` is and inject new JSON objects right after the `[`

new_papers = """
  {
    "id": 991,
    "category": "AI Control",
    "cat_class": "badge-control",
    "year": 2024,
    "author": "Liao, Y. C., Ni, X., Wang, Y.",
    "title": "Energy Consumption and Carbon Emission Reduction in HVAC System of a DRAM Semiconductor Fabrication Plant",
    "journal": "IEEE Transactions on Semiconductor Manufacturing",
    "doi": "10.1109/TSM.2024.3398458",
    "doi_url": "https://doi.org/",
    "file_url": "#",
    "summary": "Deep Reinforcement Learning (DRL) optimized scheduling for cleanroom HVAC, reducing chiller plant power consumption by 18% compared to traditional PID.",
    "bluf": "Proposes an AI-driven, data-intensive framework replacing conventional PID logic, optimizing chiller sequence and water temperatures dynamically based on real-time fab thermal loads. Validated in a live DRAM fab.",
    "params": "Deep Reinforcement Learning (DRL), DQN, Real-time Fab Thermal Load, Surrogate Models",
    "control_insight": "Cloud-edge architecture allows local MAUs to pre-cool zones preemptively by analyzing lot-dispatching schedules from the MES (Manufacturing Execution System).",
    "takeaway": "Moving from static setpoints to dynamic AI-driven setpoints is the highest-ROI energy saving measure (18% reduction, payback < 1 year).",
    "tags": ["AI/ML Control", "Digital Twin", "Energy Optimization", "DRAM Fab"],
    "bibtex": "@article{Liao2024,\\n  author = {Liao, Y. C. et al.},\\n  title = {Energy Consumption and Carbon Emission Reduction in HVAC System of a DRAM Semiconductor Fabrication Plant},\\n  journal = {IEEE Transactions on Semiconductor Manufacturing},\\n  year = {2024}\\n}"
  },
  {
    "id": 992,
    "category": "Patent",
    "cat_class": "badge-warning",
    "year": 2024,
    "author": "Delta Electronics / TSMC (Assigned)",
    "title": "US20240184423A1: Cloud-Edge Collaborative Control System for Semiconductor Cleanroom HVAC",
    "journal": "US Patent & Trademark Office",
    "doi": "US20240184423A1",
    "doi_url": "https://patents.google.com/",
    "file_url": "#",
    "summary": "A patent covering edge-computing devices installed on local MAUs and FFU arrays that collaboratively sync with a centralized cloud AI.",
    "bluf": "Describes a hybrid network where latency-sensitive fan controls run on Edge AI, while heavy thermal load forecasting runs on Cloud AI. Prevents cleanroom temperature spikes when high-power EUV equipment activates.",
    "params": "Edge AI, Cloud Computing, FFU (Fan Filter Unit) Array sync, EUV thermal spike mitigation.",
    "control_insight": "The patent specifically protects the method of linking MES (Manufacturing Execution System) lot-tracking directly to local FFU fan speeds.",
    "takeaway": "Key fab operators are aggressively patenting the intersection of IT (MES/Yield data) and OT (HVAC/Facilities).",
    "tags": ["Patent", "Cloud-Edge", "Predictive Control", "Cleanroom", "TSMC"],
    "bibtex": "@patent{US20240184423A1,\\n  author = {Delta Electronics},\\n  title = {Cloud-Edge Collaborative Control System for Semiconductor Cleanroom HVAC},\\n  year = {2024},\\n  number = {US20240184423A1}\\n}"
  },
  {
    "id": 993,
    "category": "Liquid Cooling",
    "cat_class": "badge-fluid",
    "year": 2024,
    "author": "Bratukhin, A. et al.",
    "title": "Data-Intensive Energy Efficiency Modeling for Hybrid Cooling Architectures in Advanced Node Foundries",
    "journal": "Energy and Buildings, Vol. 302",
    "doi": "10.1016/j.enbuild.2024.113645",
    "doi_url": "https://doi.org/",
    "file_url": "#",
    "summary": "Evaluates the transition from pure air-side cleanroom cooling to hybrid direct-to-chip liquid cooling for AI-chip manufacturing.",
    "bluf": "As chip TDP (Thermal Design Power) exceeds 1000W, traditional cleanroom air conditioning cannot remove heat fast enough. This paper proposes a hybrid Liquid-Air architecture, routing 70% of heat directly to chilled water loops.",
    "params": "Direct-to-Chip (D2C) Liquid Cooling, Cleanroom sensible heat ratio, High-density rack cooling.",
    "control_insight": "By removing sensible heat directly via water, the MAU air volume is significantly reduced, yielding a 35% drop in total fan power.",
    "takeaway": "Future fabs will integrate liquid cooling pipes directly to process tools, permanently altering the traditional MAU-FFU cleanroom paradigm.",
    "tags": ["Liquid Cooling", "Direct-to-Chip", "Hybrid Chiller", "AI Foundries"],
    "bibtex": "@article{Bratukhin2024,\\n  author = {Bratukhin, A. et al.},\\n  title = {Data-Intensive Energy Efficiency Modeling for Hybrid Cooling Architectures in Advanced Node Foundries},\\n  journal = {Energy and Buildings},\\n  year = {2024}\\n}"
  },"""

# Insert into the JS array
import re
content = re.sub(r'(const papers = \[\s*)', r'\1' + new_papers + '\n', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected new papers and patents.")
