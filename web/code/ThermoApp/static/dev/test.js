function myFunction() {
	var x, text;
	
	//get the value of the input field with id='numb'
	x = document.getElementById('numb').value;
	// if x is not a number or less than or greater than 10
	if (isNaN(x) || x < 1 || x > 10) {
		text = 'Input not valid';
	} else {
		text = 'Input OK';
	}
	document.getElementById('demo').innerHTML = text;
}