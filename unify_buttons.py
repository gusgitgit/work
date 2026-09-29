import os
import re

# 1. 01_ihx/index.html
html_path = '01_ihx/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    ihx = f.read()
if '중앙 지식베이스' not in ihx:
    ihx = ihx.replace('<div class="spacer"></div>', '<div class="spacer"></div>\n  <a href="../index.html" class="btn" style="text-decoration:none;"><i class="fas fa-arrow-left"></i> 중앙 지식베이스</a>')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(ihx)
    print("Fixed 01_ihx/index.html")

# 2. 02_hvac_bm/index.html
html_path = '02_hvac_bm/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    hvac = f.read()
hvac = re.sub(
    r'<a href="\.\./index\.html" class="inline-flex.*?</a>',
    r'<a href="../index.html" class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-900/30 text-primary border border-blue-500/30 text-sm font-semibold mb-6 hover:bg-blue-900/50 transition-colors"><i class="fas fa-arrow-left"></i> 중앙 지식베이스</a>',
    hvac, flags=re.DOTALL
)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(hvac)
print("Fixed 02_hvac_bm/index.html")

# 3. 03_research_paper/index.html
html_path = '03_research_paper/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    research = f.read()
research = re.sub(
    r'<div class="top-nav" style="justify-content: flex-start; padding: 1rem 0; border: none; margin-bottom: 0;">.*?</div>',
    r'<div class="mb-6 mt-6"><a href="../index.html" class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-900/30 text-primary border border-blue-500/30 text-sm font-semibold hover:bg-blue-900/50 transition-colors" style="text-decoration:none;"><i class="fas fa-arrow-left"></i> 중앙 지식베이스</a></div>',
    research, flags=re.DOTALL
)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(research)
print("Fixed 03_research_paper/index.html")

# 4. 02_hvac_bm/docs/*.html
for doc in os.listdir('02_hvac_bm/docs'):
    if doc.endswith('.html'):
        p = f'02_hvac_bm/docs/{doc}'
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        
        # Replace existing back button with the new dual breadcrumb
        c = re.sub(
            r'<a href="\.\./index\.html" class="px-4 py-2 rounded-lg border border-surface_border hover:bg-surface_card text-text_muted hover:text-text_main transition-colors shrink-0">.*?</a>',
            r'''<div class="flex gap-3 shrink-0">
            <a href="../../index.html" class="px-4 py-2 rounded-full border border-surface_border hover:bg-surface_card text-text_muted hover:text-text_main transition-colors text-sm font-semibold flex items-center gap-2">
                <i class="fas fa-home"></i> 홈
            </a>
            <a href="../index.html" class="px-4 py-2 rounded-full bg-hvac/10 text-hvac border border-hvac/30 hover:bg-hvac/20 transition-colors text-sm font-semibold flex items-center gap-2">
                <i class="fas fa-arrow-left"></i> 상위 메뉴
            </a>
        </div>''',
            c, flags=re.DOTALL
        )
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Fixed {p}")

# 5. 01_ihx/docs/theory.html
html_path = '01_ihx/docs/theory.html'
with open(html_path, 'r', encoding='utf-8') as f:
    theory = f.read()
theory = re.sub(
    r'<div class="flex gap-4">.*?</div>',
    r'''<div class="flex gap-3 shrink-0">
            <a href="../../index.html" class="px-4 py-2 rounded-full border border-surface_border hover:bg-surface_card text-text_muted hover:text-text_main transition-colors text-sm font-semibold flex items-center gap-2">
                <i class="fas fa-home"></i> 홈
            </a>
            <a href="../index.html" class="px-4 py-2 rounded-full bg-ihx/10 text-ihx border border-ihx/30 hover:bg-ihx/20 transition-colors text-sm font-semibold flex items-center gap-2">
                <i class="fas fa-arrow-left"></i> 상위 메뉴
            </a>
        </div>''',
    theory, flags=re.DOTALL
)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(theory)
print("Fixed 01_ihx/docs/theory.html")

