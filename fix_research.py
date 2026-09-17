import re

html_path = '03_research_paper/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace top-nav with back button
top_nav_pattern = re.compile(r'<div class="top-nav">.*?</div>', re.DOTALL)
back_btn = '''<div class="top-nav" style="justify-content: flex-start; padding: 1rem 0; border: none; margin-bottom: 0;">
      <a href="../index.html" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; border-radius: 999px; background: rgba(56, 189, 248, 0.1); color: #38bdf8; text-decoration: none; font-weight: 600; border: 1px solid rgba(56,189,248,0.3); transition: all 0.2s;">
        <i class="fa-solid fa-arrow-left"></i> 중앙 대시보드로 돌아가기
      </a>
    </div>'''
content = top_nav_pattern.sub(back_btn, content)

# Remove VIEW 2 completely
view2_pattern = re.compile(r'<!-- VIEW 2: SEMICONDUCTOR HVAC BENCHMARK -->.*?(?=<!-- Hidden Modals -->)', re.DOTALL)
content = view2_pattern.sub('', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Successfully removed HVAC BM and added back button.')
