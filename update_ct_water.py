import re
import json

# 1. Update 02_hvac_bm/docs/03_cooling_tower.html
html_path = '02_hvac_bm/docs/03_cooling_tower.html'
with open(html_path, 'r', encoding='utf-8') as f:
    ct_content = f.read()

# We want to add new content to the Engineering Analysis section (under <div class="space-y-6 text-text_muted">)
# Find where the 2nd point ends, before the infographic.
target_str = """                <div>
                    <h3 class="text-xl font-semibold text-text_main mb-2">2. 첨단 수자원 절감 하드웨어 (증발수 포집 기술)</h3>
                    <p>물을 증발시켜 열을 빼앗는 기본 원리는 유지하되, <strong>백연(Plume) 형태로 날아가는 수분을 물리적으로 다시 포집(Plume Abatement)</strong>하거나 응축(Condensation)시켜 냉각탑 내부로 되돌리는 기술이 도입되고 있습니다. 공기-공기 열교환기(Air-to-Air Heat Exchanger)를 활용해 덥고 습한 배기를 차가운 외기로 식혀 수분을 응결시키는 하이브리드 냉각탑이 대표적입니다.</p>
                </div>"""

new_content = """                <div>
                    <h3 class="text-xl font-semibold text-text_main mb-2">2. 첨단 수자원 절감 및 포집 하드웨어 (Vapor Capture)</h3>
                    <p>물을 증발시켜 열을 빼앗는 기본 원리는 유지하되, <strong>백연(Plume) 형태로 날아가는 기체 상태의 수분(수증기)을 다시 포집</strong>하여 냉각탑 내부로 되돌리는 기술이 적극 도입되고 있습니다. 기존에는 열교환기를 이용한 물리적 응결 방식을 썼으나, 최근에는 <strong>정전기적 액적 포집(Electrostatic Vapor Capture)</strong> 기술이 부상하고 있습니다. 방출되는 수증기 입자에 이온(Ion)을 쏴 전하를 띠게 한 뒤 쿨링타워 배기구에 설치된 전기장 메쉬(Mesh)로 수분을 빨아들여 극순수(Demineralized Water) 급의 물을 10~20%가량 회수하는 원리입니다.</p>
                </div>
                
                <div>
                    <h3 class="text-xl font-semibold text-text_main mb-2">3. 반도체 폐수 및 초순수(UPW) Reject 재활용</h3>
                    <p>반도체 팹은 막대한 양의 초순수(Ultra-Pure Water)를 사용합니다. 이 과정에서 발생하는 <strong>초순수 정수 필터링 잔수(RO Reject)나 화학적 기계 연마(CMP) 공정의 폐수</strong>를 정수(Ultrafiltration, PFRO) 처리하여 냉각탑의 <strong>보충수(Makeup Water)</strong>로 재활용하는 'Zero Liquid Discharge (ZLD)' 시스템이 필수적입니다. 공정 용수로는 부적합하지만, 냉각탑 용수로는 충분히 사용 가능한 수질을 활용해 팹 전체의 상수(Fresh Water) 의존도를 획기적으로 낮춥니다.</p>
                </div>"""

ct_content = ct_content.replace(target_str, new_content)

# Add reference for Infinite Cooling and Wastewater to the references section at the bottom
ref_target = """<li>ASHRAE TC 9.11 (Clean Spaces) - 대규모 클린룸 냉각탑 수처리(Water Treatment) 및 블로우다운 최적화 가이드</li>"""
new_refs = """<li>ASHRAE TC 9.11 (Clean Spaces) - 대규모 클린룸 냉각탑 수처리(Water Treatment) 및 블로우다운 최적화 가이드</li>
                <li><a href="../../03_research_paper/index.html" class="hover:text-primary transition-colors underline decoration-surface_border underline-offset-2">US Patent (Infinite Cooling / MIT)</a> - 정전기적 수증기(Plume) 포집 및 냉각수 회수 기술</li>
                <li>TSMC / Intel Water Conservation Reports - 반도체 초순수 정수 잔여수(UPW Reject) 및 폐수 처리를 통한 냉각탑 보충수(Makeup) 100% 재활용 (ZLD) 실증 사례</li>"""

ct_content = ct_content.replace(ref_target, new_refs)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(ct_content)
    
# 2. Update 03_research_paper/index.html
paper_path = '03_research_paper/index.html'
with open(paper_path, 'r', encoding='utf-8') as f:
    paper_content = f.read()

new_patent = """
  {
    "id": 994,
    "category": "Patent",
    "cat_class": "badge-warning",
    "year": 2021,
    "author": "Varanasi, K. K., Damak, M. (MIT / Infinite Cooling)",
    "title": "US10926194B2: System and Method for Electrostatic Water Recovery from Cooling Tower Plumes",
    "journal": "US Patent & Trademark Office",
    "doi": "US10926194B2",
    "doi_url": "https://patents.google.com/patent/US10926194B2",
    "file_url": "#",
    "summary": "Uses ionization and an electrostatic mesh to capture and condense vapor droplets from cooling tower exhaust, recovering 10-20% of evaporated water.",
    "bluf": "A breakthrough MIT-spinoff technology that charges water droplets in the cooling tower plume and collects them using an electric field. The recovered water is highly pure (demineralized) and can be immediately reused.",
    "params": "Electrostatic collection, Ion Emitters, Plume Abatement, Demineralized Water Recovery",
    "control_insight": "Eliminates the visible plume (백연) while simultaneously reducing makeup water demand without obstructing cooling tower airflow.",
    "takeaway": "Crucial for semiconductor fabs facing severe water scarcity regulations (e.g., TSMC in Arizona). Transforms the cooling tower from a 'water consumer' to a partial 'water generator'.",
    "tags": ["Patent", "Water Recovery", "Electrostatic Capture", "Plume Abatement"],
    "bibtex": "@patent{US10926194B2,\\n  author = {Varanasi, K. K. and Damak, M.},\\n  title = {System and Method for Electrostatic Water Recovery from Cooling Tower Plumes},\\n  year = {2021},\\n  number = {US10926194B2}\\n}"
  },"""

paper_content = re.sub(r'(const papers = \[\s*)', r'\1' + new_patent + '\n', paper_content)

with open(paper_path, 'w', encoding='utf-8') as f:
    f.write(paper_content)

print("Updated Cooling Tower BM and added Infinite Cooling patent.")
