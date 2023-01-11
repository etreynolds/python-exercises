"use strict";

let score = 0;

//set countdown timer until endgame
let time = 60;
$("#timer").html(time);

//create empty set where correct words from the board are stored
let words = new Set()


$("form").on("submit", handleSubmit);

async function handleSubmit(evt) {
    evt.preventDefault();
    //create a variable that equals the word submitted through the form
    let word = $("input").val();
    //do nothing if the form is empty
    if (!word) return;
    //send this word to the "server" to have it check if it is an appropriate response
    const res = await axios.get("/check-word", { params: { word: word } });
    //set the response from the "server" to a variable
    let response = res.data.response
    console.log(response);
    //display response in DOM
    $("#response").html(response);
    //reset form
    $("form").trigger("reset");
    //if server determines ok word, update score value and update score in DOM
    if (response === "ok") {
        if (words.has(word)) {
            return;
        }
        words.add(word);
        score += word.length;
        $("#score").html(`Score: ${score}`);
    }
}


let countDown = setInterval(function () {
    //every second, decrese time by one and update time displayed in DOM
    time--;
    $("#timer").html(time);
    //run this function that only fully executes when time is up
    stopTimer();
}, 1000);

function stopTimer() {
    //if time has run out, stop countdown and replace the form with words "GAME OVER"
    if (time < 1) {
        clearInterval(countDown);
        $("form").hide();
        $(".container").append($("<span>").html("GAME OVER!"));
        endGame();
    }
}


async function endGame() {
    //post score to server to see if high score needs updating
    await axios.post("/end-game", { score: score });
}