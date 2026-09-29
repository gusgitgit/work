import re

html_path = '03_research_paper/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the custom back button div I added earlier, since we will put it properly
content = re.sub(r'<div class="mb-6 mt-6"><a href="\.\./index\.html" class="inline-flex.*?</a></div>', '', content, flags=re.DOTALL)

# Replace the <header> block with standard tailwind header
new_header = '''<header class="max-w-5xl mx-auto mb-12 text-center">
        <a href="../index.html" class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-900/30 text-primary border border-blue-500/30 text-sm font-semibold mb-6 hover:bg-blue-900/50 transition-colors" style="text-decoration:none;"><i class="fas fa-arrow-left"></i> 중앙 지식베이스</a>
        <br>
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-purple-900/30 text-purple-400 border border-purple-500/30 text-sm font-semibold mb-4">
            <i class="fa-solid fa-flask"></i> Literature Portal
        </div>
        <h1 class="text-4xl md:text-5xl font-extrabold hero-title mb-4">Advanced Cooling & DOAS Archive</h1>
        <p class="text-text_muted text-lg max-w-2xl mx-auto">액체제습(LD-DOAS), 첨단 냉각기술(액침냉각 등), AI 제어 관련 논문 및 특허 데이터베이스입니다.</p>
      </header>'''

content = re.sub(r'<header>.*?</header>', new_header, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated 03_research_paper header.")
