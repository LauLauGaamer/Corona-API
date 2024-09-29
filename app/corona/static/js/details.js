let currentChartIDs = ['chart-main', 'chart1', 'chart2', 'chart3'];
let chartConfigs = {}
let charts = {};
let parsedData

window.onload = function() {
    initializeCharts();

    document.getElementById('date-update').addEventListener('click', function() {
        console.log("hhhhhh");
        var start = document.getElementById('start-date').value
        var end = document.getElementById('end-date').value
    
        window.location.href = `${window.location.origin}/corona/details/${parsedData["endpoint_id"]}?type=${parsedData["endpoint_type"]}&start=${start}&end=${end}` 
    });

    function initializeCharts() {
        var scriptTag = document.getElementById('data-json');
        var jsonData = scriptTag.textContent;
        parsedData = JSON.parse(jsonData);
        console.log(parsedData)

        // set start/end date
        document.getElementById('start-date').value = parsedData['start_date']
        document.getElementById('end-date').value = parsedData['end_date']

        chartConfigs['chart-main'] = createLineChartConfig('Corona-Fälle', parsedData['cases'], false)
        chartConfigs['chart1'] = createLineChartConfig('Genesen', parsedData['recovered'], true)
        chartConfigs['chart2'] = createLineChartConfig('Inzidenz', parsedData['incidence'], true)        
        chartConfigs['chart3'] = createLineChartConfig('Tode', parsedData['deaths'], true)

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

    function createLineChartConfig(label, data, isSideChart) {
        return {
            type: 'line',
            data: {
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
                            },
                            autoSkip: true,
                            maxTicksLimit: isSideChart ? 2 : 8
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

        chartConfigs[currentChartIDs[0]] = createLineChartConfig(chartConfigs[currentChartIDs[0]].data.datasets[0].label, chartConfigs[currentChartIDs[0]].data.datasets[0].data, true);
        chartConfigs[currentChartIDs[chartId]] = createLineChartConfig(chartConfigs[currentChartIDs[chartId]].data.datasets[0].label, chartConfigs[currentChartIDs[chartId]].data.datasets[0].data, false);

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