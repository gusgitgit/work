import re

html_path = '04_psychrometrics/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

if '.error-state #out-enth-kcal' not in content:
    content = content.replace('.error-state .input-field { color: #ef4444 !important; border-color: rgba(239, 68, 68, 0.5); }', 
                              '.error-state .input-field { color: #ef4444 !important; border-color: rgba(239, 68, 68, 0.5); }\n        .error-state #out-enth-kcal { color: #ef4444 !important; opacity: 1 !important; }')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated error state for kcal/kg.")
