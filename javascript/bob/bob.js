var Bob = function() {};

Bob.prototype.hey = function(input) {
	var result
	if (input == input.toUpperCase() && input != input.toLowerCase()) {
		result = 'Whoa, chill out!'	
	} else if (input[input.length - 1] == '?'){
		result = 'Sure.'
	} else if (input.trim() == "" ){
		result = 'Fine. Be that way!'
	} else {
		result = 'Whatever.'
	}
	 	 	
 	return result 
		
};

module.exports = Bob;