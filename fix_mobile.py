import re

html_path = '04_psychrometrics/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the CDN link
content = content.replace('https://cdn.jsdelivr.net/npm/psychrolib@2.5.0/src/psychrolib.js', 'https://cdn.jsdelivr.net/npm/psychrolib@1.1.1/psychrolib.js')

# Fix body padding for mobile
content = content.replace('class="min-h-screen p-6 md:p-12"', 'class="min-h-screen p-4 sm:p-6 md:p-12"')

# Fix h1 font size for mobile
content = content.replace('class="text-4xl md:text-5xl font-extrabold', 'class="text-3xl md:text-5xl font-extrabold')

# Fix result-box responsive style
result_box_css = """
        .result-box { background: #0f172a; border: 1px solid #1e293b; border-radius: 0.75rem; padding: 1rem; display: flex; flex-direction: column; align-items: flex-start; gap: 0.25rem; }
        @media (min-width: 640px) {
            .result-box { padding: 1.25rem; flex-direction: row; align-items: center; justify-content: space-between; gap: 0; }
        }
"""
content = re.sub(r'\.result-box \{ background: #0f172a;.*?; \}', result_box_css.strip(), content)

# Fix glass-card padding for mobile
content = content.replace('padding: 2rem;', 'padding: 1.25rem;')
content = content.replace('.glass-card { background', '.glass-card { \n            background')
content = content.replace('padding: 1.25rem;', 'padding: 1.25rem; \n        }\n        @media (min-width: 640px) { .glass-card { padding: 2rem; } }')

# Make inputs more touch friendly
content = content.replace('padding: 0.75rem 1rem;', 'padding: 0.85rem 1rem;')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html for mobile and fixed CDN.")
