import re

def insert_before_main_end(html_path, content_to_insert):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "<!-- References -->" in content:
        return # already added
        
    content = re.sub(r'(</main>)', r'\n' + content_to_insert + r'\n\1', content)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. MAU
mau_refs = """
        <!-- References -->
        <section class="mt-8 p-6 bg-surface/50 border border-surface_border rounded-lg">
            <h3 class="text-lg font-bold text-text_muted mb-3"><i class="fas fa-book-open mr-2"></i> 관련 출처 및 참고문헌</h3>
            <ul class="list-disc list-inside text-sm text-text_dim space-y-1.5">
                <li><a href="../../03_research_paper/index.html" class="hover:text-primary transition-colors underline decoration-surface_border underline-offset-2">Jeong et al. (2014), "Annual operating energy savings of liquid desiccant... 100% outdoor air system"</a> - 잠열/현열 분리(LD-DOAS)를 통한 51% 에너지 절감 입증</li>
                <li>TSMC Sustainability Report 2023 - MAU 응축수 100% 포집 및 재활용 라인 전면 도입</li>
                <li>Samsung Electronics Sustainability Report 2024 - 동절기 외기 냉수 냉방(Free Cooling) 시스템 확대 적용</li>
            </ul>
        </section>
"""
insert_before_main_end('02_hvac_bm/docs/01_mau_oac.html', mau_refs)

# 2. Chiller
chiller_refs = """
        <!-- References -->
        <section class="mt-8 p-6 bg-surface/50 border border-surface_border rounded-lg">
            <h3 class="text-lg font-bold text-text_muted mb-3"><i class="fas fa-book-open mr-2"></i> 관련 출처 및 참고문헌</h3>
            <ul class="list-disc list-inside text-sm text-text_dim space-y-1.5">
                <li><a href="../../03_research_paper/index.html" class="hover:text-primary transition-colors underline decoration-surface_border underline-offset-2">Liao et al. (2024), "Energy Consumption and Carbon Emission Reduction in HVAC System of a DRAM..."</a> - AI 강화학습 기반 칠러 플랜트 스케줄링</li>
                <li>SK Hynix ESG Report 2023 - 칠러 응축기 폐열 회수(Heat Recovery) 및 히트펌프 연계 운영 사례</li>
                <li>SEMI S23 Guide - 반도체 제조 설비의 에너지 및 유틸리티 절감 기준 (Right-sizing 및 VFD 적용 권장)</li>
            </ul>
        </section>
"""
insert_before_main_end('02_hvac_bm/docs/02_chiller.html', chiller_refs)

# 3. Cooling Tower
ct_refs = """
        <!-- References -->
        <section class="mt-8 p-6 bg-surface/50 border border-surface_border rounded-lg">
            <h3 class="text-lg font-bold text-text_muted mb-3"><i class="fas fa-book-open mr-2"></i> 관련 출처 및 참고문헌</h3>
            <ul class="list-disc list-inside text-sm text-text_dim space-y-1.5">
                <li>SEMI F21 / SEMI S23 Standards - 반도체 팹 냉각수 시스템 및 수자원 보존(Water Conservation) 가이드라인</li>
                <li>CXMT Environmental Impact Assessment (EIA) Report - 신규 팹 백연 저감(Plume Abatement) 설비 및 밀폐형 냉각탑 도입 규제</li>
                <li>ASHRAE TC 9.11 (Clean Spaces) - 대규모 클린룸 냉각탑 수처리(Water Treatment) 및 블로우다운 최적화 가이드</li>
            </ul>
        </section>
"""
insert_before_main_end('02_hvac_bm/docs/03_cooling_tower.html', ct_refs)

# 4. Refrigerants
ref_refs = """
        <!-- References -->
        <section class="mt-8 p-6 bg-surface/50 border border-surface_border rounded-lg">
            <h3 class="text-lg font-bold text-text_muted mb-3"><i class="fas fa-book-open mr-2"></i> 관련 출처 및 참고문헌</h3>
            <ul class="list-disc list-inside text-sm text-text_dim space-y-1.5">
                <li>EU F-Gas Regulation & US EPA SNAP - 기존 HFC(R-134a, R-410A) 규제 및 차세대 HFO 냉매(R-1234ze, R-514A) 전환 로드맵</li>
                <li><a href="../../03_research_paper/index.html" class="hover:text-primary transition-colors underline decoration-surface_border underline-offset-2">Bratukhin et al. (2024), "Data-Intensive Energy Efficiency Modeling for Hybrid Cooling Architectures..."</a> - 고발열 AI 칩셋 대비 액침/직접 냉각(Direct-to-Chip) 하이브리드 아키텍처</li>
                <li>Intel / ASML Sustainability Memos - 극자외선(EUV) 설비 냉각을 위한 초정밀 칠러 및 친환경 냉매 채택 현황</li>
            </ul>
        </section>
"""
insert_before_main_end('02_hvac_bm/docs/04_refrigerants.html', ref_refs)

# 5. AI Control
ai_refs = """
        <!-- References -->
        <section class="mt-8 p-6 bg-surface/50 border border-surface_border rounded-lg">
            <h3 class="text-lg font-bold text-text_muted mb-3"><i class="fas fa-book-open mr-2"></i> 관련 출처 및 참고문헌</h3>
            <ul class="list-disc list-inside text-sm text-text_dim space-y-1.5">
                <li><a href="../../03_research_paper/index.html" class="hover:text-primary transition-colors underline decoration-surface_border underline-offset-2">US Patent US20240184423A1 (Delta Electronics)</a> - Cloud-Edge Collaborative Control System for Semiconductor Cleanroom HVAC</li>
                <li><a href="../../03_research_paper/index.html" class="hover:text-primary transition-colors underline decoration-surface_border underline-offset-2">Liao et al. (2024), IEEE Transactions on Semiconductor Manufacturing</a> - 강화학습(DRL) 적용 실증 논문</li>
                <li>Johnson Controls OpenBlue / Schneider EcoStruxure Whitepapers - 머신러닝 대리 모델(Surrogate Model) 기반 공조 디지털 트윈 기술 백서</li>
            </ul>
        </section>
"""
insert_before_main_end('02_hvac_bm/docs/05_ai_control.html', ai_refs)

print("Injected references into all 5 BM docs.")
