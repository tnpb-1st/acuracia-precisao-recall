function generateData(accuracy, precision, resolution) {
    let points = Math.round(resolution);
    let data = [];
    let spread = 5 - accuracy; // Maior acurácia significa menor deslocamento do centro
    let tightness = 1 / precision; // Maior precisão significa menor dispersão
    
    for (let i = 0; i < points; i++) {
        data.push({ x: (Math.random() - 0.5) * spread * tightness, y: (Math.random() - 0.5) * spread * tightness });
    }
    return data;
}

function updatePlot() {
    let accuracy = parseFloat(document.getElementById('accuracy').value);
    let precision = parseFloat(document.getElementById('precision').value);
    let resolution = parseFloat(document.getElementById('resolution').value);
    
    document.getElementById('accuracy-value').textContent = accuracy.toFixed(1);
    document.getElementById('precision-value').textContent = precision.toFixed(1);
    document.getElementById('resolution-value').textContent = resolution;
    
    let data = generateData(accuracy, precision, resolution);

    let trace = {
        x: data.map(p => p.x),
        y: data.map(p => p.y),
        mode: 'markers',
        marker: { color: 'red', size: 10, opacity: 0.8, line: { width: 2, color: 'black' } }
    };

    let circles = [];
    for (let i = 1; i <= 6; i++) {
        circles.push({
            type: 'circle',
            xref: 'x',
            yref: 'y',
            x0: -i,
            y0: -i,
            x1: i,
            y1: i,
            line: { color: 'rgba(0, 0, 0, 0.3)', width: 1 }
        });
    }

    let layout = {
        title: 'Distribuição dos Tiros',
        xaxis: { range: [-6, 6], title: 'X', gridcolor: 'rgba(255,255,255,0.3)' },
        yaxis: { range: [-6, 6], title: 'Y', gridcolor: 'rgba(255,255,255,0.3)' },
        showlegend: false,
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(255,255,255,0.1)',
        width: 800, // Tamanho maior do gráfico
        height: 800, // Tamanho maior do gráfico
        shapes: circles
    };

    Plotly.newPlot('plot', [trace], layout);
}

document.getElementById('accuracy').addEventListener('input', updatePlot);
document.getElementById('precision').addEventListener('input', updatePlot);
document.getElementById('resolution').addEventListener('input', updatePlot);

updatePlot();
