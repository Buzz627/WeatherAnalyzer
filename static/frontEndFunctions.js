var output = document.getElementById("output");


function nope(err){
	output.innerHTML="<br>Blocked"
}

function rateWeather(num){
	navigator.geolocation.getCurrentPosition(pos=>sendRating(pos, num), nope);
}
function sendRating(pos, num){
	var data={"num":num, "latitude":pos.coords.latitude, "longitude": pos.coords.longitude}
	var settings = {
	  "async": true,
	  "url": "/rateWeather",
	  "method": "POST",
	  "headers": {
	    "Content-Type": "application/json",

	  },
	  "processData": false,
	  "data": JSON.stringify(data)
	}
	$.ajax(settings).done(function (response) {
		output.innerHTML = "<br>"+response.text
	});
}

function showInfo(path){
	navigator.geolocation.getCurrentPosition(pos=>current(pos, path), nope);
}
function current(pos, path){

	var data={"latitude":pos.coords.latitude, "longitude": pos.coords.longitude}
	var settings = {
	  "async": true,
	  "url": path,
	  "method": "POST",
	  "headers": {
	    "Content-Type": "application/json",
	  },
	  "processData": false,
	  "data": JSON.stringify(data)
	}

	$.ajax(settings).done(function (response) {
		// console.log(response);
		output.innerHTML = response.text;
	});
}