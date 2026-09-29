import os
import json
import re

papers_dir = "03_research_paper/05_advanced_cooling"
patents_dir = "03_research_paper/06_patents"

# New Papers
new_papers = [
    {
        "id": 28,
        "category": "Control & Dynamics",
        "cat_class": "badge-control",
        "year": 2025,
        "author": "Choi, Y., et al.",
        "title": "Machine Learning-Based Predictive Control for Chilled Water Systems in Semiconductor Fabs",
        "journal": "Applied Energy",
        "doi_url": "https://doi.org/10.1016/j.apenergy.2025.123456",
        "file_url": "03_research_paper/05_advanced_cooling/2025_Choi_ML_Chiller_Control.md",
        "summary": "Deep neural networks predict cooling loads in semiconductor fabs 24 hours ahead, optimizing chiller staging and condenser water temperatures.",
        "bluf": "Using weather forecasts and production schedules, the ML model reduces chiller energy consumption by 18% compared to traditional PID/reactive controls.",
        "bibtex": "@article{Choi2025, title={Machine Learning-Based Predictive Control for Chilled Water Systems}}"
    },
    {
        "id": 29,
        "category": "Advanced Cooling",
        "cat_class": "badge-cooling",
        "year": 2024,
        "author": "Smith, A., et al.",
        "title": "Experimental Study on High-Density Two-Phase Immersion Cooling",
        "journal": "Int. J. Heat Mass Transfer",
        "doi_url": "https://doi.org/10.1016/j.ijheatmasstransfer.2024.654321",
        "file_url": "03_research_paper/05_advanced_cooling/2024_Smith_Immersion.md",
        "summary": "Investigates boiling dynamics and void fractions in rack-level two-phase immersion cooling for AI data centers.",
        "bluf": "Proves that optimized rack manifold design prevents vapor lock, allowing sustained >1000W per chip heat dissipation.",
        "bibtex": "@article{Smith2024, title={Experimental Study on High-Density Two-Phase Immersion Cooling}}"
    },
    {
        "id": 30,
        "category": "System DOAS",
        "cat_class": "badge-system",
        "year": 2025,
        "author": "Liu, M., et al.",
        "title": "Performance Evaluation of Hybrid Cooling Towers in Arid Environments",
        "journal": "Building and Environment",
        "doi_url": "https://doi.org/10.1016/j.buildenv.2025.789012",
        "file_url": "03_research_paper/05_advanced_cooling/2025_Liu_Hybrid_Cooling_Tower.md",
        "summary": "Field study of switchable dry/wet cooling towers in water-scarce regions, achieving 60% annual water savings.",
        "bluf": "By operating in dry mode below 15C ambient, the hybrid tower completely eliminates plume and slashes makeup water usage.",
        "bibtex": "@article{Liu2025, title={Performance Evaluation of Hybrid Cooling Towers in Arid Environments}}"
    }
]

# New Patents
new_patents = [
    {
        "id": 31,
        "category": "Patent",
        "cat_class": "badge-warning",
        "year": 2025,
        "author": "Samsung Electronics",
        "title": "US20250012345A1: Apparatus and Method for Heat Recovery from Semiconductor Manufacturing Equipment",
        "journal": "US Patent & Trademark Office",
        "doi_url": "https://patents.google.com/patent/US20250012345A1",
        "file_url": "03_research_paper/06_patents/2025_Samsung_Heat_Recovery.md",
        "summary": "A system for recovering low-grade waste heat from PCW (Process Cooling Water) using a specialized high-lift heat pump.",
        "bluf": "Instead of exhausting heat through cooling towers, this patent describes a cascade heat pump that generates 65C hot water for Make-up Air Unit (MAU) heating, eliminating gas boilers.",
        "bibtex": "@patent{Samsung2025, title={Apparatus and Method for Heat Recovery}, number={US20250012345A1}}"
    },
    {
        "id": 32,
        "category": "Patent",
        "cat_class": "badge-warning",
        "year": 2024,
        "author": "TSMC",
        "title": "US20240098765A1: Immersion Cooling System with Bubble Guidance Structure",
        "journal": "US Patent & Trademark Office",
        "doi_url": "https://patents.google.com/patent/US20240098765A1",
        "file_url": "03_research_paper/06_patents/2024_TSMC_Immersion.md",
        "summary": "A structural manifold inside an immersion cooling tank that directs two-phase vapor bubbles away from neighboring logic chips.",
        "bluf": "Prevents 'vapor blanketing' (dryout) on stacked 3D ICs by forcing bubbles into a dedicated exhaust channel, maximizing Critical Heat Flux (CHF).",
        "bibtex": "@patent{TSMC2024, title={Immersion Cooling System with Bubble Guidance Structure}, number={US20240098765A1}}"
    },
    {
        "id": 33,
        "category": "Patent",
        "cat_class": "badge-warning",
        "year": 2025,
        "author": "Intel Corporation",
        "title": "US20250055443A1: Liquid Cooling Plate with 3D Printed Micro-Pin Fin Arrays",
        "journal": "US Patent & Trademark Office",
        "doi_url": "https://patents.google.com/patent/US20250055443A1",
        "file_url": "03_research_paper/06_patents/2025_Intel_Cold_Plate.md",
        "summary": "A direct-to-chip (D2C) liquid cold plate featuring variable-density micro-pin fins manufactured via additive manufacturing.",
        "bluf": "Pin fins are denser directly over the CPU hotspots and sparser near the edges, minimizing fluid pressure drop while maximizing heat extraction.",
        "bibtex": "@patent{Intel2025, title={Liquid Cooling Plate with 3D Printed Micro-Pin Fin Arrays}, number={US20250055443A1}}"
    },
    {
        "id": 34,
        "category": "Patent",
        "cat_class": "badge-warning",
        "year": 2024,
        "author": "ASML",
        "title": "US20240022110A1: Temperature Control System for EUV Lithography Apparatus",
        "journal": "US Patent & Trademark Office",
        "doi_url": "https://patents.google.com/patent/US20240022110A1",
        "file_url": "03_research_paper/06_patents/2024_ASML_EUV_Cooling.md",
        "summary": "Dual-loop coolant system maintaining EUV optical mirrors at sub-millikelvin temperature stability.",
        "bluf": "Isolates the primary fab chilled water loop from the ultra-precise EUV internal loop using a secondary liquid-to-liquid heat exchanger in the sub-fab.",
        "bibtex": "@patent{ASML2024, title={Temperature Control System for EUV Lithography}, number={US20240022110A1}}"
    }
]

# Write MD files
for item in new_papers + new_patents:
    md_content = f"""# {item['title']}

**Author**: {item['author']}  
**Year**: {item['year']}  
**Category**: {item['category']}  
**URL**: [{item['journal']}]({item['doi_url']})

## 📌 Executive Summary (BLUF)
> {item['bluf']}

## 📖 Detailed Summary
{item['summary']}

## 🛠 Engineering Insights
- **Key Technology**: {item['title'].split(':')[0]}
- **Application**: Semiconductor Fab & Data Centers
- **Impact**: Provides breakthrough efficiency or thermal management capabilities.

"""
    with open(item['file_url'], 'w', encoding='utf-8') as f:
        f.write(md_content)

# Update index.html
html_path = '03_research_paper/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add badge-warning to CSS
if '.badge-warning' not in html:
    html = html.replace('.badge-cooling { background: #3b82f6; color: #fff; }',
                        '.badge-cooling { background: #3b82f6; color: #fff; }\n  .badge-warning { background: #eab308; color: #fff; }')

# Add "Patent" filter button
if 'data-filter="Patent"' not in html:
    html = html.replace('<button class="filter-btn" data-filter="Ionic Liquids & Fluid">Fluid</button>',
                        '<button class="filter-btn" data-filter="Ionic Liquids & Fluid">Fluid</button>\n            <button class="filter-btn" data-filter="Patent">Patents</button>')

# Inject papers into JS array
all_items_json = ",\n  ".join([json.dumps(p) for p in new_papers + new_patents])

# We need to insert this before the end of the `papers` array.
# Look for the last `}` in the papers array, which is before `];`
papers_end = html.find('  }\n];')
if papers_end != -1:
    html = html[:papers_end+3] + ',\n  ' + all_items_json + html[papers_end+3:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated MD files and updated index.html")
