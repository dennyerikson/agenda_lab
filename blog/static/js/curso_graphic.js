
$(document).ready(function() {
    var url = "/curso_json/";

    $.getJSON(url, function(res){
      var data = res.cursos.map(function(v){
        return [v.curso, v.quantidade]
      })  

      Highcharts.setOptions({
        lang: {
          drillUpText: '<< Voltar '
        }
      });
    
      Highcharts.chart('container', {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Cursos mais agendados'
        },
        subtitle: {
          text: 'Agendamento por curso no 1º semestre 2019'
        },
        xAxis: {
          type: 'category'
        },
        yAxis: {
          title: {
            text: 'Quantidade'
          }
        },
        legend: {
          enabled: false
        },
        plotOptions: {
          series: {
            borderWidth: 5,
            dataLabels: {
              enabled: true,
              format: '{point.y}'
            }
          }
        },
        tooltip: {
          headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
          pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}</b> do total<br/>'
          // pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> do total<br/>'
        },    
    
        series: [{
          name: 'Curso',
          colorByPoint: true,
  
          data: data
        }],
        // drilldown: {
        //   series: [{
        //       name: 'EAD',
        //       id: 'EAD',
        //       data: [
        //         ['Setembro', 3.0],
        //         ['Outubro', 2.0],
        //       ]
        //     },
        //     {
        //       name: 'Administração',
        //       id: 'Administração',
        //       data: [
        //         ['v40.0', 30.0],
        //         ['v41.0', 20.8],    
        //       ]
        //     }
        //   ]
        // }
      });
    });

    
  });
  