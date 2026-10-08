import re

html_path = '02_hvac_bm/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I need to add pillar 5 to the tailwind config first so `pillar5` exists
content = content.replace("pillar4: '#f59e0b'", "pillar4: '#f59e0b', pillar5: '#c084fc'")

# Also inject the card inside the <main> grid.
# Look for the last card (04_refrigerants.html) and add after its </a>

new_card = """
        <!-- Tech Pillar 5: AI & Predictive Control -->
        <a href="./docs/05_ai_control.html" class="glass-card group hover:!border-pillar5" style="text-decoration:none;">
            <div class="flex flex-col h-full">
                <div class="flex items-center justify-between mb-4">
                    <div class="w-12 h-12 rounded-lg bg-pillar5/10 flex items-center justify-center text-pillar5 text-xl group-hover:scale-110 transition-transform"><i class="fas fa-brain"></i></div>
                    <i class="fas fa-arrow-right text-text_muted group-hover:text-pillar5 transition-colors group-hover:translate-x-1"></i>
                </div>
                <h2 class="text-xl font-bold text-text_main mb-2">Pillar 05.<br><span class="text-2xl text-pillar5">AI & Predictive Control</span></h2>
                <p class="text-text_muted text-sm flex-grow mb-4">강화학습 및 디지털 트윈을 활용한 예측 제어, MES 생산 일정 연동 시스템, Cloud-Edge 분산 처리</p>
                <div class="pt-4 border-t border-surface_border mt-auto">
                    <span class="text-xs font-semibold text-text_muted uppercase tracking-wider">Key Players</span>
                    <p class="text-sm text-text_main mt-1">TSMC, Delta Electronics, JCI, Schneider</p>
                </div>
            </div>
        </a>
"""

# Let's insert the new card just before </main>
content = re.sub(r'(\s*</main>)', r'\n' + new_card + r'\1', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated HVAC Tech Pillars index.")
