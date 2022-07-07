'use strict';

const button = document.querySelector('#new_activity_button'); 
console.log(button);
button.addEventListener('click', (evt) => {
    evt.preventDefault();

    fetch('/get-recenter')
        .then((response) => response.text())
        .then((responseString) => { ;
        const activity = document.querySelector('#random_activity');
        activity.innerHTML = responseString;
    });
});

