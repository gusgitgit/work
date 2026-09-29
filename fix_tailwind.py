import os
import re

for doc in os.listdir('02_hvac_bm/docs'):
    if doc.endswith('.html'):
        p = f'02_hvac_bm/docs/{doc}'
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        
        c = c.replace('bg-hvac/10', 'bg-accent/10')
        c = c.replace('text-hvac', 'text-accent')
        c = c.replace('border-hvac/30', 'border-accent/30')
        c = c.replace('hover:bg-hvac/20', 'hover:bg-accent/20')
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Fixed {p} tailwind colors.")
