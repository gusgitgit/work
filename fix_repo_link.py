import re

html_path = '03_research_paper/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('https://github.com/gusgitgit/research_paper/blob/main/', 'https://github.com/gusgitgit/work/blob/main/')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed github repo link in modal.")
