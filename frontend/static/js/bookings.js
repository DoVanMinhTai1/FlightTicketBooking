function popup(element) {
    let ref = element.dataset.ref;
    document.querySelector("#cancel_ticket_btn").dataset.ref = ref;
    document.querySelector(".popup").style.display = 'block';
}

function remove_popup() {
    document.querySelector(".popup").style.display = 'none';
    document.querySelector("#cancel_ticket_btn").dataset.ref = "";
}

function cancel_tkt() {
    let ref = document.querySelector("#cancel_ticket_btn").dataset.ref;
    let formData = new FormData();
    formData.append('ref',ref)
    fetch('/booking/cancel/',{
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(response => {
        if (response.success === true) {
            remove_popup();
            document.querySelector(`[id='${ref}'] .ticket-action-div`).innerHTML = '';
            document.querySelector(`[id='${ref}'] .status-div`).innerHTML = `<div class="red">CANCELLED</div>`;
            document.querySelector(`[id='${ref}'] .booking-date-div`).innerHTML = '';
        }
        else {
            remove_popup();
            alert(`Error: ${response.error}`)
        }
    });
}

let timeLeft = 20 * 60; // thời gian đếm ngược
function startCountdown() {
    const timerDisplay = document.getElementById('countdown');
    function updateTimer() {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

        if (timeLeft > 0) {
            timeLeft--;
        } else {
            clearInterval(interval);

            document.querySelector(` .ticket-action-div`).innerHTML = '';
            document.querySelector(` .status-div`).innerHTML = `<div class="red">CANCELLED</div>`;
            document.querySelector(` .booking-date-div`).innerHTML = '';
        }
    }
    updateTimer();
    const interval = setInterval(updateTimer, 1000);
}

window.onload = startCountdown;

