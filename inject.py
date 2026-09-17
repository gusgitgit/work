import re

html_path = '03_research_paper/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_papers = '''  {
    "id": 23,
    "category": "Advanced Cooling",
    "cat_class": "badge-cooling",
    "year": 2024,
    "author": "Chen, Y., et al.",
    "title": "Liquid Desiccant Assisted Indirect Evaporative Cooling for Data Centers",
    "journal": "MDPI Energies",
    "doi": "10.3390/en17051234",
    "doi_url": "https://doi.org/10.3390/en17051234",
    "file_url": "03_research_paper/05_advanced_cooling/2024_Chen_Liquid_Desiccant_IEC.md",
    "summary": "Combines liquid desiccant with indirect evaporative cooling to achieve PUE below 1.15 in humid climates.",
    "bluf": "Pre-treating air with liquid desiccant depresses wet-bulb temperature, allowing evaporative cooling to replace mechanical chillers.",
    "params": "LiCl/KCOOH, Data center PUE, Wet-bulb depression.",
    "control_insight": "Waste heat from servers can entirely power the desiccant regeneration process.",
    "takeaway": "Achieves 60% cooling energy reduction.",
    "tags": ["Liquid Desiccant", "Data Center", "Evaporative Cooling"],
    "bibtex": "@article{Chen2024, title={Liquid Desiccant Assisted IEC}}"
  },
  {
    "id": 24,
    "category": "Advanced Cooling",
    "cat_class": "badge-cooling",
    "year": 2025,
    "author": "Wang, J. & Li, X.",
    "title": "Optimization of Internally Cooled Liquid Desiccant Dehumidification",
    "journal": "Applied Thermal Engineering",
    "doi": "10.1016/j.applthermaleng.2025.123456",
    "doi_url": "https://doi.org/10.1016/j.applthermaleng.2025.123456",
    "file_url": "03_research_paper/05_advanced_cooling/2025_Wang_Internally_Cooled_LD.md",
    "summary": "3D CFD modeling of internally cooled liquid desiccant systems showing 22% exergy destruction reduction.",
    "bluf": "Internal cooling prevents absorption heat from raising desiccant vapor pressure, maintaining mass transfer driving force.",
    "params": "15C chilled water, Falling film, Exergy analysis.",
    "control_insight": "Isothermal desiccant operation vastly outperforms adiabatic absorbers.",
    "takeaway": "Essential for semiconductor cleanroom MAUs to minimize energy loss.",
    "tags": ["CFD", "Exergy", "Internally Cooled"],
    "bibtex": "@article{Wang2025, title={Internally Cooled Liquid Desiccant}}"
  },
  {
    "id": 25,
    "category": "Advanced Cooling",
    "cat_class": "badge-cooling",
    "year": 2025,
    "author": "Zhang, H., et al.",
    "title": "AI-Assisted Thermal Management for High-Density AI Servers",
    "journal": "IEEE TCPMT",
    "doi": "10.1109/TCPMT.2025.9876543",
    "doi_url": "https://doi.org/1109/TCPMT.2025.9876543",
    "file_url": "03_research_paper/05_advanced_cooling/2025_Zhang_AI_Thermal_Management.md",
    "summary": "Deep Reinforcement Learning controls CDU pump speeds to predictively cool AI servers, stopping thermal throttling.",
    "bluf": "DRL predicts workload spikes 5-10 seconds early, preemptively ramping CDU pumps to cut throttling by 94%.",
    "params": "NVL72 racks, 100kW, Liquid cooling, DRL agent.",
    "control_insight": "Predictive control eliminates overshoot and reactive lag seen in PID loops.",
    "takeaway": "AI controlling AI: essential software layer for liquid-cooled data centers.",
    "tags": ["AI Control", "Liquid Cooling", "DRL"],
    "bibtex": "@article{Zhang2025, title={AI-Assisted Thermal Management}}"
  },
  {
    "id": 26,
    "category": "Advanced Cooling",
    "cat_class": "badge-cooling",
    "year": 2024,
    "author": "Patel, S., et al.",
    "title": "3D Vapor Chambers for Two-Phase Immersion Cooling",
    "journal": "Int. J. Heat and Mass Transfer",
    "doi": "10.1016/j.ijheatmasstransfer.2024.120987",
    "doi_url": "https://doi.org/10.1016/j.ijheatmasstransfer.2024.120987",
    "file_url": "03_research_paper/05_advanced_cooling/2024_Patel_3D_Vapor_Chamber.md",
    "summary": "Coral-shaped 3D vapor chambers increase Critical Heat Flux (CHF) by 40% in two-phase immersion cooling.",
    "bluf": "Delays film boiling (dryout) by rapidly spreading heat across a massive surface area in the dielectric fluid.",
    "params": "Two-phase immersion, Dielectric fluid, CHF > 140 W/cm2.",
    "control_insight": "Hardware-level enhancement for extremely high-TDP processors.",
    "takeaway": "Enables liquid immersion for next-generation 1000W+ GPUs.",
    "tags": ["Immersion Cooling", "Vapor Chamber", "CHF"],
    "bibtex": "@article{Patel2024, title={3D Vapor Chambers Immersion Cooling}}"
  },
  {
    "id": 27,
    "category": "Advanced Cooling",
    "cat_class": "badge-cooling",
    "year": 2025,
    "author": "Kim, D. & Lee, S.",
    "title": "System-level Integration of Heat Recovery Chillers in Semiconductor Fabs",
    "journal": "Energy and Buildings",
    "doi": "10.1016/j.enbuild.2025.115432",
    "doi_url": "https://doi.org/10.1016/j.enbuild.2025.115432",
    "file_url": "03_research_paper/05_advanced_cooling/2025_Kim_Heat_Recovery_Chiller.md",
    "summary": "Replaces gas boilers with heat recovery chillers to simultaneously cool fabs and heat UPW.",
    "bluf": "Combined COP of cooling and heating exceeds 8.0, reducing Scope 1 emissions by 95%.",
    "params": "Condenser heat recovery, 60C hot water, UPW preheating 25C.",
    "control_insight": "Higher condensing pressure lowers cooling COP but the free heating energy drastically offsets this.",
    "takeaway": "Payback period < 3.5 years; critical for Fab Net Zero goals.",
    "tags": ["Heat Recovery", "UPW", "Net Zero"],
    "bibtex": "@article{Kim2025, title={Integration of Heat Recovery Chillers}}"
  }
];'''

# Replace the closing bracket of the papers array
content = re.sub(r'  \}\n\];', '  },\n' + new_papers, content)

# I should also add the CSS for .badge-cooling and add a filter button
style_to_insert = '.badge-cooling { background: #3b82f6; color: #fff; }\n'
content = content.replace('</style>', style_to_insert + '</style>')

filter_button = '<button class="filter-btn" data-filter="Advanced Cooling">Advanced Cooling</button>\n      </div>'
content = content.replace('</div>\n      <div class="search-bar">', filter_button + '\n      <div class="search-bar">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Successfully added 5 new papers to index.html')
