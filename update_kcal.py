import re

html_path = '04_psychrometrics/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Enthalpy HTML section
old_enth = """                    <!-- Enthalpy -->
                    <div class="prop-card">
                        <label class="text-sm font-semibold text-text_muted flex items-center gap-2">
                            <i class="fa-solid fa-bolt text-purple-400 w-4 text-center"></i> 엔탈피 (Enthalpy)
                        </label>
                        <div class="relative">
                            <input type="number" id="in-enth" value="50.22" step="0.1" oninput="calculate('enth')" class="input-field text-purple-400" />
                            <span class="absolute right-4 top-1/2 -translate-y-1/2 unit-label font-mono">kJ/kg</span>
                        </div>
                    </div>"""

new_enth = """                    <!-- Enthalpy -->
                    <div class="prop-card">
                        <label class="text-sm font-semibold text-text_muted flex items-center gap-2">
                            <i class="fa-solid fa-bolt text-purple-400 w-4 text-center"></i> 엔탈피 (Enthalpy)
                        </label>
                        <div class="relative">
                            <input type="number" id="in-enth" value="50.22" step="0.1" oninput="calculate('enth')" class="input-field text-purple-400" style="padding-right: 5.5rem;" />
                            <div class="absolute right-3 top-1/2 -translate-y-1/2 flex flex-col items-end pointer-events-none">
                                <span class="unit-label font-mono">kJ/kg</span>
                                <span id="out-enth-kcal" class="text-[0.65rem] font-mono text-purple-400/70 mt-0.5">12.00 kcal/kg</span>
                            </div>
                        </div>
                    </div>"""

content = content.replace(old_enth, new_enth)
if old_enth not in content and new_enth not in content:
    # try replacing loosely
    content = re.sub(r'<!-- Enthalpy -->.*?</div>\s*</div>\s*</div>', new_enth, content, flags=re.DOTALL)

# 2. Update input-field padding from 3.5rem to 4.5rem for better spacing globally
content = content.replace('padding: 1rem 3.5rem 1rem 1rem;', 'padding: 1rem 4.5rem 1rem 1rem;')

# 3. Add space in Chart.js tooltip
content = content.replace('return `Tdb: ${context.parsed.x.toFixed(1)}°C, HR: ${context.parsed.y.toFixed(1)}g/kg`;', 
                          'return `Tdb: ${context.parsed.x.toFixed(1)} °C, HR: ${context.parsed.y.toFixed(1)} g/kg`;')

# 4. Update the javascript calculate() to also update out-enth-kcal
old_js = "update('enth', res_enth, 2);"
new_js = "update('enth', res_enth, 2);\n                document.getElementById('out-enth-kcal').innerText = (res_enth / 4.184).toFixed(2) + ' kcal/kg';"
content = content.replace(old_js, new_js)

# Also update the init function or initial state to correctly show kcal for default 50.22 kJ/kg
# 50.22 / 4.184 = 12.00
# It will be auto updated on load anyway because window.onload = function() { calculate(); };

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Applied kcal/kg and spacing adjustments.")
