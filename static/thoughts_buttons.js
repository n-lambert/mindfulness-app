'use strict';
// putting event listeners on each edit button for the thoughts timecapsule
for (const button of document.querySelectorAll('.save_edits')) { // loops through all buttons with class save_edits
    button.addEventListener('click', (evt) => {                  // adds event listener
        // evt.preventDefault();
    
        const formInputs = {                                     // creates js object with key value 
        journal_id: button.id,
        edits: document.querySelector(`#edit_${button.id}`).value,
        };
    
        fetch('/journal', {                                      // makes the request to the journal route
        method: 'POST',                                          // defines the method the data is being requested
        body: JSON.stringify(formInputs),                        // turns the json object into a string
        headers: {
            'Content-Type': 'application/json',
        },
        })
        .then((response) => response.text())                    // turns the data back into text
        // .then((responseJson) => { 
        //     alert("Saved!");                                     // local host alerts user that edits were saved
            // alert(responseJson.status);
        // });
    }); }