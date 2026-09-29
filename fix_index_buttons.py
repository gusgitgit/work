import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace button styles
content = content.replace(
    'class="text-xs font-medium px-2 py-1 rounded bg-surface_border text-text_muted hover:text-text_main"',
    'class="inline-flex items-center px-3 py-1.5 rounded-full bg-surface_border/50 text-text_muted hover:text-text_main hover:bg-surface_border transition-colors text-xs font-semibold"'
)
content = content.replace(
    'class="text-xs font-medium px-2 py-1 rounded bg-ihx/20 text-ihx hover:bg-ihx/30 transition-colors"',
    'class="inline-flex items-center px-3 py-1.5 rounded-full bg-ihx/10 text-ihx hover:bg-ihx/20 transition-colors text-xs font-semibold"'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html card buttons.")
