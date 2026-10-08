import re

html_path = '04_psychrometrics/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add Chart.js to head
if 'chart.js' not in content:
    content = content.replace('</head>', '    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\n</head>')

# Add Canvas HTML below the first glass-card
canvas_html = """
        <!-- Psychrometric Chart Visualizer -->
        <div class="glass-card mt-6">
            <h2 class="text-xl sm:text-2xl font-bold text-text_main mb-4 border-b border-surface_border pb-4"><i class="fa-solid fa-chart-line text-primary mr-2"></i> Psychrometric Chart</h2>
            <div class="w-full bg-slate-900 rounded-lg p-2 sm:p-4 border border-surface_border" style="position: relative; height: 50vh; min-height: 400px;">
                <canvas id="psyChart"></canvas>
            </div>
        </div>
"""
# Insert after the closing div of the first glass-card, before </main>
content = re.sub(r'(</div>\n    </main>)', r'</div>\n' + canvas_html + r'\n    </main>', content)

# Add Chart.js logic script
script_logic = """
        let chartInstance = null;
        let lastDrawnPress = 0;

        function getRhCurve(rh, press) {
            let data = [];
            for(let t = 0; t <= 50; t += 1) {
                try {
                    let hr = psychrolib.GetHumRatioFromRelHum(t, rh, press) * 1000.0;
                    data.push({x: t, y: hr});
                } catch(e) {}
            }
            return data;
        }

        function getTwbLine(twb, press) {
            let data = [];
            for(let t = twb; t <= 50; t += 2) {
                try {
                    let hr = psychrolib.GetHumRatioFromTWetBulb(t, twb, press) * 1000.0;
                    if(hr >= 0) data.push({x: t, y: hr});
                } catch(e) {}
            }
            return data;
        }

        function initChart(press) {
            const ctx = document.getElementById('psyChart').getContext('2d');
            const datasets = [];
            
            datasets.push({
                label: 'Current State',
                data: [{x: 25, y: 9.88}],
                backgroundColor: '#f43f5e',
                borderColor: '#ffffff',
                borderWidth: 2,
                pointRadius: 6,
                pointHoverRadius: 8,
                showLine: false,
                order: 0
            });

            datasets.push({
                label: '100% RH',
                data: getRhCurve(1.0, press),
                borderColor: 'rgba(56, 189, 248, 0.8)',
                borderWidth: 2,
                showLine: true,
                pointRadius: 0,
                fill: false,
                tension: 0.4,
                order: 1
            });

            [0.8, 0.6, 0.4, 0.2].forEach(rh => {
                datasets.push({
                    label: `${rh*100}% RH`,
                    data: getRhCurve(rh, press),
                    borderColor: 'rgba(56, 189, 248, 0.3)',
                    borderWidth: 1,
                    borderDash: [5, 5],
                    showLine: true,
                    pointRadius: 0,
                    fill: false,
                    tension: 0.4,
                    order: 2
                });
            });

            [5, 10, 15, 20, 25, 30, 35].forEach(twb => {
                datasets.push({
                    label: `Twb ${twb}°C`,
                    data: getTwbLine(twb, press),
                    borderColor: 'rgba(16, 185, 129, 0.2)',
                    borderWidth: 1,
                    showLine: true,
                    pointRadius: 0,
                    fill: false,
                    order: 3
                });
            });

            chartInstance = new Chart(ctx, {
                type: 'scatter',
                data: { datasets: datasets },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    animation: { duration: 200 },
                    scales: {
                        x: {
                            type: 'linear', position: 'bottom', min: 0, max: 50,
                            title: { display: true, text: 'Dry Bulb Temperature (°C)', color: '#94a3b8' },
                            grid: { color: 'rgba(30, 41, 59, 0.5)' }, ticks: { color: '#94a3b8' }
                        },
                        y: {
                            type: 'linear', position: 'right', min: 0, max: 30,
                            title: { display: true, text: 'Humidity Ratio (g/kg)', color: '#94a3b8' },
                            grid: { color: 'rgba(30, 41, 59, 0.5)' }, ticks: { color: '#94a3b8' }
                        }
                    },
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    if(context.datasetIndex === 0) return `Tdb: ${context.parsed.x.toFixed(1)}°C, HR: ${context.parsed.y.toFixed(1)}g/kg`;
                                    return context.dataset.label;
                                }
                            }
                        }
                    }
                }
            });
            lastDrawnPress = press;
        }

        function updateChart(tdb, hr, press) {
            if (!chartInstance) {
                initChart(press);
            } else if (Math.abs(press - lastDrawnPress) > 10) {
                chartInstance.destroy();
                initChart(press);
            }
            chartInstance.data.datasets[0].data = [{x: tdb, y: hr}];
            chartInstance.update('none'); // Update without full animation for responsiveness
        }
"""

content = content.replace('// Default secondary constraint parameter is RH', script_logic + '\n        // Default secondary constraint parameter is RH')

# Add updateChart to calculate()
content = content.replace("update('vp', res_vp, 0);", "update('vp', res_vp, 0);\n                \n                updateChart(tdb, res_hr, press);")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html with Psychrometric Chart.")
