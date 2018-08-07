const HOURHAND = document.querySelector("#hour");
const MINUTEHAND = document.querySelector("#minute");
const SECONDHAND = document.querySelector("#second");

//getting data
function updateClock(){
  var date = new Date();
  var hours = date.getHours();
  var minutes = date.getMinutes() ;
  var seconds = date.getSeconds();
  let secPos = seconds * 360 / 60;
  let hrPos = hours *360/12 + minutes* 360/60/12;
  let minPos = minutes* 360/60 + (secPos/60);

  HOURHAND.style.transform = "rotate(" + hrPos + "deg)";
  MINUTEHAND.style.transform = "rotate(" + minPos + "deg)";
  SECONDHAND.style.transform = "rotate(" + secPos + "deg)";
}

var interval = setInterval(updateClock, 1000);
