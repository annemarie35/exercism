var Pangram = function(pangram) {
	this.pangram = pangram.toLowerCase();
	var missingLetters = 0;
	var alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
	
	this.isPangram = function() {

		for (var i = 0; i < 26; i++) {
			console.log(pangram.indexOf(alphabet[i]));
			if (pangram.toLowerCase().indexOf(alphabet[i]) == -1) {
				missingLetters += 1;
				console.log ("missin : " + missingLetters == 0);
			}
		}
		return missingLetters == 0;

	};
};

module.exports = Pangram;