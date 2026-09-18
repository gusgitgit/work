import os

css_to_add = """
    <style>
        /* HTML/CSS Infographic Dashboards */
        .infographic { display: flex; align-items: center; justify-content: center; gap: 1.5rem; padding: 2.5rem 1.5rem; background: #0b1121; border-radius: 12px; border: 1px solid #1e293b; margin: 2rem 0; flex-wrap: wrap; box-shadow: inset 0 2px 15px rgba(0,0,0,0.4); }
        .infographic.scrollable { flex-wrap: nowrap; overflow-x: auto; justify-content: flex-start; padding: 2.5rem; }
        .ig-node { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 1.25rem 1.5rem; border-radius: 16px; min-width: 170px; text-align: center; gap: 0.85rem; box-shadow: 0 8px 20px rgba(0,0,0,0.3); transition: transform 0.2s; position: relative; }
        .ig-node:hover { transform: translateY(-5px); }
        .ig-node i { font-size: 2.5rem; }
        .ig-node span { font-size: 1.1rem; font-weight: 800; line-height: 1.3; }
        .ig-desc { font-size: 0.85rem; opacity: 0.85; font-weight: 500; font-family: monospace; }
        
        .ig-arrow { color: #94a3b8; font-size: 1.8rem; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.5rem; }
        .ig-arrow span { font-size: 0.85rem; color: #f8fafc; font-weight: 700; white-space: nowrap; background: #131d33; padding: 0.2rem 0.6rem; border-radius: 20px; border: 1px solid #1e293b; }
        .ig-arrow i { filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5)); }

        /* Thematic Node Colors */
        .node-hot { background: linear-gradient(135deg, #7f1d1d, #b91c1c); color: #fecaca; border: 1px solid #f87171; }
        .node-hot i { color: #fca5a5; }
        .node-hot-2 { background: linear-gradient(135deg, #9a3412, #c2410c); color: #fed7aa; border: 1px solid #fb923c; }
        .node-hot-2 i { color: #fdba74; }
        
        .node-cold { background: linear-gradient(135deg, #0c4a6e, #0369a1); color: #bae6fd; border: 1px solid #38bdf8; }
        .node-cold i { color: #7dd3fc; }
        .node-cold-2 { background: linear-gradient(135deg, #1e3a8a, #1d4ed8); color: #bfdbfe; border: 1px solid #60a5fa; }
        .node-cold-2 i { color: #93c5fd; }
        
        .node-machine { background: linear-gradient(135deg, #1e293b, #334155); color: #f8fafc; border: 1px solid #64748b; }
        .node-machine i { color: #cbd5e1; }
        
        .node-purify { background: linear-gradient(135deg, #3b0764, #6b21a8); color: #e9d5ff; border: 1px solid #c084fc; }
        .node-purify i { color: #d8b4fe; }

        .node-eco { background: linear-gradient(135deg, #14532d, #166534); color: #bbf7d0; border: 1px solid #4ade80; }
        .node-eco i { color: #86efac; }
        
        .ig-group { display: flex; flex-direction: column; gap: 1.5rem; }
    </style>
</head>"""

def inject_diagram(file_path, diagram_html, insert_after_text):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # inject CSS
    if ".infographic {" not in content:
        content = content.replace('</head>', css_to_add)
        modified = True
    
    # inject Diagram
    if insert_after_text in content and "div class=\"infographic" not in content:
        content = content.replace(insert_after_text, insert_after_text + '\n' + diagram_html)
        modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected into {file_path}")
    else:
        print(f"Already injected or insertion point not found for {file_path}")

base_dir = '02_hvac_bm/docs'

# 1. MAU Diagram
mau_html = """
        <!-- Scrollable Flow Diagram for MAU -->
        <div class="infographic scrollable">
          <div class="ig-node node-machine">
            <i class="fa-solid fa-cloud"></i>
            <span>외기 (OA)</span>
            <div class="ig-desc">100% Outdoor Air</div>
          </div>
          <div class="ig-arrow"><i class="fa-solid fa-chevron-right"></i></div>
          
          <div class="ig-node node-cold">
            <i class="fa-solid fa-temperature-arrow-down"></i>
            <span>Cooling Coil</span>
            <div class="ig-desc">강제 냉각/감습</div>
          </div>
          <div class="ig-arrow"><i class="fa-solid fa-chevron-right"></i></div>
          
          <div class="ig-node node-cold-2">
            <i class="fa-solid fa-shower"></i>
            <span>Air Washer</span>
            <div class="ig-desc">수용성 AMC 세정 (UPW)</div>
          </div>
          <div class="ig-arrow"><i class="fa-solid fa-chevron-right"></i></div>
          
          <div class="ig-node node-purify">
            <i class="fa-solid fa-filter"></i>
            <span>Chemical Filter</span>
            <div class="ig-desc">VOCs 및 산성 가스 차단</div>
          </div>
          <div class="ig-arrow"><i class="fa-solid fa-chevron-right"></i></div>
          
          <div class="ig-node node-eco">
            <i class="fa-solid fa-microchip"></i>
            <span>Cleanroom</span>
            <div class="ig-desc">공정 챔버 공급</div>
          </div>
        </div>
"""
inject_diagram(f'{base_dir}/01_mau_oac.html', mau_html, '<h3 class="text-xl font-semibold text-text_main mb-2">1. MAU (Make-up Air Unit)의 역할과 병목</h3>')


# 2. Chiller Diagram
chiller_html = """
        <!-- Beautiful HTML Infographic for HRC -->
        <div class="infographic">
          <div class="ig-node node-hot">
            <i class="fa-solid fa-fire"></i>
            <span>PCW 폐열</span>
            <div class="ig-desc">25~30°C 환수</div>
          </div>
          
          <div class="ig-arrow">
            <span>열원 회수</span>
            <i class="fa-solid fa-arrow-right"></i>
          </div>
          
          <div class="ig-node node-machine">
            <i class="fa-solid fa-fan"></i>
            <span>열회수 냉동기<br>(HRC)</span>
            <div class="ig-desc">히트펌프 사이클 승온</div>
          </div>
          
          <div class="ig-arrow">
            <div style="display:flex; flex-direction:column; gap: 1rem;">
              <span><i class="fa-solid fa-arrow-up-right"></i> 응축 발열</span>
              <span><i class="fa-solid fa-arrow-down-right"></i> 증발 냉각</span>
            </div>
          </div>
          
          <div class="ig-group">
            <div class="ig-node node-hot-2">
              <i class="fa-solid fa-temperature-arrow-up"></i>
              <span>난방 온수 공급</span>
              <div class="ig-desc">50~65°C (MAU 난방)</div>
            </div>
            <div class="ig-node node-cold">
              <i class="fa-solid fa-droplet"></i>
              <span>PCW 냉수 재공급</span>
              <div class="ig-desc">10~15°C (초순수 팹 투입)</div>
            </div>
          </div>
        </div>
"""
inject_diagram(f'{base_dir}/02_chiller.html', chiller_html, '<h3 class="text-xl font-semibold text-text_main mb-2">2. 폐열 회수 칠러 (Heat Recovery Chillers)</h3>')

# 3. Cooling Tower Diagram
tower_html = """
        <!-- Hybrid Cooling Tower Switch Graphic -->
        <div class="infographic">
          <div class="ig-node node-machine">
            <i class="fa-solid fa-industry"></i>
            <span>하이브리드 냉각탑</span>
            <div class="ig-desc">모드 자동 전환형 PACT</div>
          </div>
          
          <div class="ig-arrow">
            <span>계절/외기 온도</span>
            <i class="fa-solid fa-code-branch"></i>
          </div>
          
          <div class="ig-group">
            <div class="ig-node node-cold" style="border: 2px solid #38bdf8;">
              <i class="fa-solid fa-cloud-showers-heavy"></i>
              <span>하절기 (습식 모드)</span>
              <div class="ig-desc">증발 잠열 냉각 (용수 소모 발생)</div>
            </div>
            <div class="ig-node node-eco" style="border: 2px solid #4ade80;">
              <i class="fa-solid fa-leaf"></i>
              <span>동절기 (건식 모드)</span>
              <div class="ig-desc">외기 현열 핀튜브 냉각 (용수 소모 Zero)</div>
            </div>
          </div>
        </div>
"""
inject_diagram(f'{base_dir}/03_cooling_tower.html', tower_html, '<h3 class="text-xl font-semibold text-text_main mb-2">2. 첨단 수자원 절감 하드웨어 (증발수 포집 기술)</h3>')
