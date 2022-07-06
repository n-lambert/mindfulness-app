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
          },

          {
            label: 'Calmness',
            data: q2_data, 
          },

          {
            label: 'Care-Free',
            data: q3_data, 
          },

          {
            label: 'Energetic',
            data: q4_data, 
          },

          {
            label: 'Active',
            data: q5_data, 
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

