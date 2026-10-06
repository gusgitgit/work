import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add psy color to tailwind config
content = content.replace("research: '#c084fc' }", "research: '#c084fc', psy: '#f43f5e' }")

# Add the 4th card before </main>
new_card = """
        <!-- Psychrometric Calculator Card -->
        <div class="glass-card group block">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-psy/10 flex items-center justify-center text-psy text-xl group-hover:scale-110 transition-transform"><i class="fa-solid fa-temperature-half"></i></div>
                    <h2 class="text-2xl font-bold text-text_main">습공기선도 계산기</h2>
                </div>
                <i class="fas fa-arrow-right text-text_muted group-hover:text-psy transition-colors"></i>
            </div>
            <p class="text-text_muted mb-4">ASHRAE 표준 기반 실시간 습공기 상태량(RH, 절대습도, 노점, 엔탈피) 계산 도구</p>
            <div class="flex gap-2">
                <a href="./04_psychrometrics/index.html" class="inline-flex items-center px-3 py-1.5 rounded-full bg-surface_border/50 text-text_muted hover:text-text_main hover:bg-surface_border transition-colors text-xs font-semibold">Open Calculator</a>
            </div>
        </div>
"""

content = content.replace("    </main>", new_card + "\n    </main>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
