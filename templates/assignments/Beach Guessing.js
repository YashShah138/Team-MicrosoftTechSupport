
let ccdisplay = document.querySelector('.crrDisplay');
let incdisplay = document.querySelector('.incDisplay');
let guess = document.querySelector('#character');
let textForm = document.querySelector('.textForm');

var commonWords = [
    "Surfing", "Volleyball", "Dogs", "Sunbathing", "Picnic", "Bonfire", "Running", "Walking", "Tanning", "Sandcastle", "Relaxing", "Snorkeling"

var chooseRandomWord = function(array) {
    return array[Math.floor(Math.random() * array.length)];

    var counter = 10;
    var triedCharacters = [];
    var correctCharacters = [];

    for (choenWord.length)
}

var scrambleWord = function(word) {
    var myword = "picnic"
    var scrambled = myword.split('').sort(function(){return 0.5-Math.random()}).join('')
    return scrambled;
}

