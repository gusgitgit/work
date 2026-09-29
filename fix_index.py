import os

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# IHX Card
content = content.replace(
    '<a href="./01_ihx/index.html" class="glass-card group block">',
    '<div class="glass-card group block">'
)
# HVAC Card
content = content.replace(
    '<a href="./02_hvac_bm/index.html" class="glass-card group block">',
    '<div class="glass-card group block">'
)
# Research Card
content = content.replace(
    '<a href="./03_research_paper/index.html" class="glass-card group block">',
    '<div class="glass-card group block">'
)

# For each card, we need to replace its closing </a> which is before the next card or </main>
# We can find the card by its heading and then replace the appropriate </a>
content = content.replace(
    '''            <div class="flex gap-2">
                <span class="text-xs font-medium px-2 py-1 rounded bg-surface_border text-text_muted">Simulator</span>
                <a href="./01_ihx/docs/theory.html" class="text-xs font-medium px-2 py-1 rounded bg-ihx/20 text-ihx hover:bg-ihx/30 transition-colors">Theory & Thermodynamics</a>
            </div>
        </a>''',
    '''            <div class="flex gap-2">
                <a href="./01_ihx/index.html" class="text-xs font-medium px-2 py-1 rounded bg-surface_border text-text_muted hover:text-text_main">Go to Simulator</a>
                <a href="./01_ihx/docs/theory.html" class="text-xs font-medium px-2 py-1 rounded bg-ihx/20 text-ihx hover:bg-ihx/30 transition-colors">Theory & Thermodynamics</a>
            </div>
        </div>'''
)

content = content.replace(
    '''            <div class="flex gap-2">
                <span class="text-xs font-medium px-2 py-1 rounded bg-surface_border text-text_muted">Fab Utility</span>
                <span class="text-xs font-medium px-2 py-1 rounded bg-surface_border text-text_muted">ESG Engineering</span>
            </div>
        </a>''',
    '''            <div class="flex gap-2">
                <a href="./02_hvac_bm/index.html" class="text-xs font-medium px-2 py-1 rounded bg-surface_border text-text_muted hover:text-text_main">View Tech Pillars</a>
            </div>
        </div>'''
)

content = content.replace(
    '''            <div class="flex gap-2">
                <span class="text-xs font-medium px-2 py-1 rounded bg-surface_border text-text_muted">Research</span>
            </div>
        </a>''',
    '''            <div class="flex gap-2">
                <a href="./03_research_paper/index.html" class="text-xs font-medium px-2 py-1 rounded bg-surface_border text-text_muted hover:text-text_main">View Papers</a>
            </div>
        </div>'''
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed index.html structure.")
