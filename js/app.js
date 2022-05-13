'use strict';

const openFormbtn = document.querySelector('.openForm-btn');
openFormbtn.addEventListener('click', function() {
   openForm();
});

const closeFormbtn = document.querySelector(".cancel-btn");
closeFormbtn.addEventListener('click', function() {
    closeForm();
});

//Open and close new league form
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

//Checks that passwords match
function checkLeaguePasswordMatch() {
    const p1 = document.getElementsByName("lPsw");
    const p2 = document.getElementsByName("lPswCon");
    if (p1 != p2) {
        alert("Passwords do not match");
    }
}