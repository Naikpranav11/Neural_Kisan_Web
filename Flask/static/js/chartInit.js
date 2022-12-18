const colors=['#4723FF','#23CAFF','#FF008A','#FF7923','#1eff00']
let ctx = document.getElementById('TemperatureChart');
let width =.6;
let DataChart1=[]
i=0;

var TemperatureChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: DataChart1,
    datasets: [{
      borderColor:colors[i],
      data: DataChart1,
      borderWidth: width,
      
      tension: 0.5,
      pointStyle:false,
    }]
  },
  options: {
    animation: false,
    plugins:{
    legend:{
      display:false
    }},
    scales: {
      y: {
        display:false,
        beginAtZero: false
      },
      x:{
        display:false
      }
    }
  }
});




i++;



ctx = document.getElementById('MoistureChart');
Edata= [0]


var MoistureChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: Edata,
    datasets: [{
      borderColor:colors[i],
      data: Edata,
      borderWidth: width,
      
      tension: 0.5,
      pointStyle:false,
    }]
  },
  options: {
    animation: false,
    plugins:{
    legend:{
      display:false
    }},
    scales: {
      y: {
        display:false,
        beginAtZero: false
      },
      x:{
        display:false
      }
    }
  }
});

i++;



ctx = document.getElementById('pHChart');
Edata= [0]


var pHChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: Edata,
    datasets: [{
      borderColor:colors[i],
      data: Edata,
      borderWidth: width,
      
      tension: 0.5,
      pointStyle:false,
    }]
  },
  options: {
    animation: false,
    plugins:{
    legend:{
      display:false
    }},
    scales: {
      y: {
        display:false,
        beginAtZero: false
      },
      x:{
        display:false
      }
    }
  }
});

i++;



ctx = document.getElementById('HumidityChart');
Edata= [0]


var HumidityChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: Edata,
    datasets: [{
      borderColor:colors[i],
      data: Edata,
      borderWidth: width,
      
      tension: 0.5,
      pointStyle:false,
    }]
  },
  options: {
    animation: false,
    plugins:{
    legend:{
      display:false
    }},
    scales: {
      y: {
        display:false,
        beginAtZero: false
      },
      x:{
        display:false
      }
    }
  }
});

i++;



ctx = document.getElementById('AQIChart');
Edata= [0]


var AQIChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: Edata,
    datasets: [{
      borderColor:colors[i],
      data: Edata,
      borderWidth: width,
      
      tension: 0.5,
      pointStyle:false,
    }]
  },
  options: {
    animation: false,
    plugins:{
    legend:{
      display:false
    }},
    scales: {
      y: {
        display:false,
        beginAtZero: false
      },
      x:{
        display:false
      }
    }
  }
});