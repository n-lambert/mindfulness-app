
for (const button of document.querySelectorAll('.save_edits')) {
    button.addEventListener('click', (evt) => {
        // evt.preventDefault();
    
        const formInputs = {
        journal_id: button.id,
        edits: document.querySelector(`#edit_${button.id}`).value,
        };
    
        fetch('/journal', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
            'Content-Type': 'application/json',
        },
        })
        .then((response) => response.text())
        .then((responseJson) => { 
            alert("Saved!");
            // alert(responseJson.status);
        });
    }); }