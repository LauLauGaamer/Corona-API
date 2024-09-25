let currentChartIDs = ['chart-main', 'chart1', 'chart2', 'chart3'];
let chartConfigs = {}
let charts = {};

window.onload = function() {
    initializeCharts();

    function initializeCharts() {
        chartConfigs['chart-main'] = createLineChartConfig('Hauptmetrik', [12, 19, 3, 5, 2, 3])
        chartConfigs['chart1'] = createLineChartConfig('Metrik 1', [10, 15, 5, 6, 8, 10])
        chartConfigs['chart2'] = createLineChartConfig('Metrik 2', [6, 8, 12, 9, 10, 15])        
        chartConfigs['chart3'] = createLineChartConfig('Metrik 3', [4, 5, 7, 8, 9, 6])

        charts['chart-main'] = new Chart(
            document.getElementById('chart-main').getContext('2d'),
            chartConfigs['chart-main']
        );
        charts['chart1'] = new Chart(
            document.getElementById('chart1').getContext('2d'),
            chartConfigs['chart1']
        );
        charts['chart2'] = new Chart(
            document.getElementById('chart2').getContext('2d'),
            chartConfigs['chart2']
        );
        charts['chart3'] = new Chart(
            document.getElementById('chart3').getContext('2d'),
            chartConfigs['chart3']
        );
    }

    function createLineChartConfig(label, data) {
        return {
            type: 'line',
            data: {
                labels: ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni'],
                datasets: [{
                    label: label,
                    data: data,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 2,
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: true,
                        labels: {
                            color: 'white',
                            font: {
                                size: 14
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            color: 'white',
                            font: {
                                size: 12
                            }
                        }
                    },
                    y: {
                        ticks: {
                            color: 'white',
                            font: {
                                size: 12
                            }
                        }
                    }
                }
            }
        };
    }

    window.moveToCenter = function(chartId) {
        // delete old charts
        if (charts['chart-main']) {
            charts['chart-main'].destroy();
            clearCanvas(0);
        }

        if (charts['chart' + String(chartId)]) {
            charts['chart' + String(chartId)].destroy();
            clearCanvas(chartId);
        }

        // Create new Charts
        charts['chart-main'] = new Chart(
            getSideChartContext(0).getContext('2d'),
            chartConfigs[currentChartIDs[chartId]]
        );
        charts['chart' + String(chartId)] = new Chart(
            getSideChartContext(chartId).getContext('2d'),
            chartConfigs[currentChartIDs[0]]
        );

        // update chart IDs
        var mainChart = currentChartIDs[0];
        currentChartIDs[0] = currentChartIDs[chartId]
        currentChartIDs[chartId] = mainChart;
    };

    function clearCanvas(chartId) {
        const canvas = getSideChartContext(chartId);
        const context = canvas.getContext('2d');
        context.clearRect(0, 0, canvas.width, canvas.height);
    }

    function getSideChartContext(chartId){
        switch(chartId){
            case 0:
                return document.getElementById('chart-main');
            case 1:
                return document.getElementById('chart1');
            case 2:
                return document.getElementById('chart2');
            case 3:
                return document.getElementById('chart3');
        }
    }
};

function updateCharts(){}