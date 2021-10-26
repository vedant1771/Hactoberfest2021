var secondsHand = document.querySelector('.sec-hand');
var minsHand = document.querySelector('.min-hand');
var hrHand = document.querySelector('.hour-hand');
function setDate(){

    var date = new Date();
    var seconds  = date.getSeconds();
    var secondsDegree = ((seconds/60)*360) + 90;
    secondsHand.style.transform = `rotate(${secondsDegree}deg)`;


    var mins = date.getMinutes();
    var minsDegree  = ((mins/60)*360)+90;
    minsHand.style.transform = `rotate(${minsDegree}deg)`;


    var hrs = date.getHours();
    var hrsDegree = ((hrs/12)*360)+90;
    hrHand.style.transform = `rotate(${hrsDegree}deg)`;


}
setInterval(setDate,1000);
