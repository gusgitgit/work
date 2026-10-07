import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_main = """
    <!-- Main Content -->
    <main class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pb-20">
        
        <!-- IHX Simulator Card -->
        <a href="./01_ihx/index.html" class="glass-card group block cursor-pointer hover:border-ihx/50 transition-all" style="text-decoration:none;">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-ihx/10 flex items-center justify-center text-ihx text-xl group-hover:scale-110 transition-transform"><i class="fas fa-desktop"></i></div>
                    <h2 class="text-xl font-bold text-text_main">IHX Simulator</h2>
                </div>
                <i class="fas fa-arrow-right text-text_muted group-hover:text-ihx transition-colors group-hover:translate-x-1"></i>
            </div>
            <p class="text-text_muted text-sm">내부 열교환기(Internal Heat Exchanger) 설계 및 성능 분석 시뮬레이터</p>
        </a>

        <!-- IHX Theory Card -->
        <a href="./01_ihx/docs/theory.html" class="glass-card group block cursor-pointer hover:border-ihx/50 transition-all" style="text-decoration:none;">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-ihx/10 flex items-center justify-center text-ihx text-xl group-hover:scale-110 transition-transform"><i class="fas fa-book"></i></div>
                    <h2 class="text-xl font-bold text-text_main">IHX Theory</h2>
                </div>
                <i class="fas fa-arrow-right text-text_muted group-hover:text-ihx transition-colors group-hover:translate-x-1"></i>
            </div>
            <p class="text-text_muted text-sm">내부 열교환기 열역학 이론 및 특허/기술 동향 포털</p>
        </a>

        <!-- HVAC BM Card -->
        <a href="./02_hvac_bm/index.html" class="glass-card group block cursor-pointer hover:border-hvac/50 transition-all" style="text-decoration:none;">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-hvac/10 flex items-center justify-center text-hvac text-xl group-hover:scale-110 transition-transform"><i class="fas fa-building"></i></div>
                    <h2 class="text-xl font-bold text-text_main">Semiconductor Fab HVAC</h2>
                </div>
                <i class="fas fa-arrow-right text-text_muted group-hover:text-hvac transition-colors group-hover:translate-x-1"></i>
            </div>
            <p class="text-text_muted text-sm">반도체 공장 공조 유틸리티 4대 핵심 기술(외조기, 칠러, 냉각탑, 신냉매) 심층 분석 및 기업별 BM</p>
        </a>

        <!-- Research Paper Card -->
        <a href="./03_research_paper/index.html" class="glass-card group block cursor-pointer hover:border-research/50 transition-all" style="text-decoration:none;">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-research/10 flex items-center justify-center text-research text-xl group-hover:scale-110 transition-transform"><i class="fas fa-file-alt"></i></div>
                    <h2 class="text-xl font-bold text-text_main">논문 및 특허 정리</h2>
                </div>
                <i class="fas fa-arrow-right text-text_muted group-hover:text-research transition-colors group-hover:translate-x-1"></i>
            </div>
            <p class="text-text_muted text-sm">LDAS, 액체제습, 고온냉수, 공조 제어 등 관련 논문 요약 및 리뷰 자료</p>
        </a>

        <!-- Psychrometric Calculator Card -->
        <a href="./04_psychrometrics/index.html" class="glass-card group block cursor-pointer hover:border-psy/50 transition-all" style="text-decoration:none;">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-psy/10 flex items-center justify-center text-psy text-xl group-hover:scale-110 transition-transform"><i class="fa-solid fa-temperature-half"></i></div>
                    <h2 class="text-xl font-bold text-text_main">습공기선도 계산기</h2>
                </div>
                <i class="fas fa-arrow-right text-text_muted group-hover:text-psy transition-colors group-hover:translate-x-1"></i>
            </div>
            <p class="text-text_muted text-sm">ASHRAE 표준 기반 실시간 습공기 상태량(RH, 절대습도, 노점, 엔탈피) 계산 도구</p>
        </a>

    </main>
"""

content = re.sub(r'<!-- Main Content -->\s*<main.*?</main>', new_main, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html to make cards clickable.")
