'use strict';

fetch('/sales_this_week.json')
  .then((response) => response.json())
  .then((responseJson) => {
    let data = [];
    for (const dailyTotal of responseJson.data) {
      data.push({x: dailyTotal.date, y: dailyTotal.melons_sold});
    }

    new Chart(document.querySelector('#myChart'), {
      type: 'line',
      data: {
        datasets: [
          {
            label: 'All Melons',
            data, // equivalent to data: data
          },
        ],
      },
      options: {
        scales: {
          x: {
            type: 'time',
            time: {
              tooltipFormat: 'LLLL dd', // Luxon format string
              unit: 'day',
            },
          },
        },
      },
    });
  });

