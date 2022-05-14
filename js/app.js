'use strict';

const openFormbtn = document.querySelector('.openForm-btn');
openFormbtn.addEventListener('click', function() {
   openForm();
});

const closeFormbtn = document.querySelector(".cancel-btn");
closeFormbtn.addEventListener('click', function() {
    closeForm();
});

function openForm() {
    document.getElementById("newLeague-form").style.display = "block";
}
function closeForm() {
    document.getElementById("newLeague-form").style.display = "none";
}

const submitLeague = document.querySelector(".submit-btn")
submitLeague.addEventListener('click', function() {
    checkLeaguePasswordMatch();
});

function checkLeaguePasswordMatch() {
    const password = document.querySelector('input[name=league-pass]');
    const confirm = document.querySelector('input[name=league-pass-confirm]');
    if (confirm.value === password.value) {
        confirm.setCustomValidity('');
    } else {
        confirm.setCustomValidity('Passwords do not match');
    }
}