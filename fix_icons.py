import re

html_path = '03_research_paper/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('?? View', '<i class="fa-solid fa-file-lines mr-1"></i> View')
content = content.replace('?? DOI', '<i class="fa-solid fa-up-right-from-square mr-1"></i> DOI')
content = content.replace('?? Open Note', '<i class="fa-solid fa-file-lines mr-1"></i> Open Note')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed corrupted icons.")
