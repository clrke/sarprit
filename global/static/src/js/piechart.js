$(document).ready(function () {
    Highcharts.setOptions({
        colors: ['#0F0', '#F00', '#EEE']
    });

    var navActivate = function (i) {
        $("#positive").removeClass("active");
        $("#negative").removeClass("active");
        $("#neutral").removeClass("active");
        switch(i) {
            case 0:
                $("#positive").addClass("active");
                break;
            case 1:
                $("#negative").addClass("active");
                break;
            case 2:
                $("#neutral").addClass("active");
                break;
        }
    }

    $('#piechart').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'Sentiment Analysis of ' + restaurant[0].toUpperCase() + restaurant.substring(1, restaurant.length) + ' in Twitter'
        },
        tooltip: {
    	    pointFormat: '<b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    color: '#000000',
                    connectorColor: '#000000',
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
            },series: {
                cursor: 'pointer',
                point: {
                    events: {
                        click: function() {
                            var chart = $('#piechart').highcharts();
                            for (var i = 0; i <  chart.series[0].data.length; i++){
                                if (chart.series[0].data[i] == this){
                                    navActivate(i);
                                    return;
                                }
                            }

                        }
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            data: [
                ['Positive', positive],
                ['Negative', negative],
                ['Neutral', neutral]
            ]
        }]
    });
    var chart = $('#piechart').highcharts();
    $("#positive").click(function () {
        chart.series[0].data[0].select();
        navActivate(0);
    });
    $("#negative").click(function () {
        chart.series[0].data[1].select();
        navActivate(1);
    });
    $("#neutral").click(function () {
        chart.series[0].data[2].select();
        navActivate(2);
    });
});
