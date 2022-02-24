function selectTime(){
	var service = document.getElementById('timing')
	var serVal = service.value
	console.log(serVal)
	if (serVal == "1"){
		document.getElementById("myAnchor").href = "./first.html"
	}
	else if (serVal == "2"){
		document.getElementById("myAnchor").href = "./second.html"
	}
	else if (serVal == "3"){
		document.getElementById("myAnchor").href = "./third.html"
	}
	else if (serVal == "4"){
		document.getElementById("myAnchor").href = "./fourth.html"
	}	
};


function seatBooked(){
	document.getElementById('confirm').style.display = "flex";
	document.getElementById('blur').style.opacity = "20%";
	document.getElementById('blur').style.pointerEvents = "none";
};


function checkSeats(){
	var seat = document.getElementById('sNo')
	var numSeat = seat.value
	console.log(numSeat)
	if (numSeat == "1"){
		document.getElementById('seat').style.display = "none";
		document.getElementById('en1').style.display = "block";
		document.getElementById('submit').style.display = "block";
	}
	else if (numSeat == "2"){
		document.getElementById('seat').style.display = "none";
		document.getElementById('en1').style.display = "block";
		document.getElementById('en2').style.display = "block";
		document.getElementById('submit').style.display = "block";
	}
	else if (numSeat == "3"){
		document.getElementById('seat').style.display = "none";
		document.getElementById('en1').style.display = "block";
		document.getElementById('en2').style.display = "block";
		document.getElementById('en3').style.display = "block";
		document.getElementById('submit').style.display = "block";
	}
	else if (numSeat == "4"){
		document.getElementById('seat').style.display = "none";
		document.getElementById('en1').style.display = "block";
		document.getElementById('en2').style.display = "block";
		document.getElementById('en3').style.display = "block";
		document.getElementById('en4').style.display = "block";
		document.getElementById('submit').style.display = "block";
	}
}

