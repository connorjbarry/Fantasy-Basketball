'use strict';

const openFormbtn = document.querySelector('.openForm-btn');
openFormbtn.addEventListener('click', function() {
   openForm();
});

const closeFormbtn = document.querySelector(".cancel-btn");
closeFormbtn.addEventListener('click', function() {
    closeForm();
});

const submitLeague = document.querySelector(".submit-btn")
submitLeague.addEventListener('click', function() {
    checkLeaguePasswordMatch();
});

//Open and close new league form
function openForm() {
    document.getElementById("newLeague-form").style.display = "block";
}
function closeForm() {
    document.getElementById("newLeague-form").style.display = "none";
}

//Checks that passwords match
function checkLeaguePasswordMatch() {
    const p1 = document.getElementsByName("lPsw");
    const p2 = document.getElementsByName("lPswCon");
    if (p1 != p2) {
        alert("Passwords do not match");
        console.log(p1);
        console.log(p2);
    }
    else {
        alert("Passwords match");
        console.log(p1);
        console.log(p2);
    }
}