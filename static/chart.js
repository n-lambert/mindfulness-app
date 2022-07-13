'use strict';

fetch('/survey_answers_this_week.json')
  .then((response) => response.json())
  .then((responseJson) => {
    let q1_data = [];
    let q2_data = [];
    let q3_data = [];
    let q4_data = [];
    let q5_data = [];
    for (const dailyTotal of responseJson.data) {
      q1_data.push({x: dailyTotal.date, y: dailyTotal.q1_answer})
      q2_data.push({x: dailyTotal.date, y: dailyTotal.q2_answer})
      q3_data.push({x: dailyTotal.date, y: dailyTotal.q3_answer})
      q4_data.push({x: dailyTotal.date, y: dailyTotal.q4_answer})
      q5_data.push({x: dailyTotal.date, y: dailyTotal.q5_answer});
    }

console.log(q1_data)
console.log(q2_data)
console.log(q3_data)
console.log(q4_data)
console.log(q5_data)

    new Chart(document.querySelector('#myChart'), {
      type: 'line',
      data: {
        datasets: [
          {
            label: 'Mood',
            data: q1_data,
            borderColor: randomColor(),
          },

          {
            label: 'Calmness',
            data: q2_data, 
            borderColor: randomColor(),
          },

          {
            label: 'Care-Free',
            data: q3_data, 
            borderColor: randomColor(),
          },

          {
            label: 'Energetic',
            data: q4_data, 
            borderColor: randomColor(),
          },

          {
            label: 'Rested',
            data: q5_data, 
            borderColor: randomColor(),
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
            title: {
              display: true,
              text: 'Date'
            },
          },
          y: {
            title: {
              display: true,
              text: 'Answers'
            },
            min: 0,
            suggestedMax: 5,
            ticks: {
              stepSize: 1
            }
          }
        },
      },
    });
  });

