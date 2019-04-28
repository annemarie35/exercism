function Gigasecond(dateOfBirth) {
	this.dateOfBirth= dateOfBirth;
	this.date = function() {
		gaBirthday = new Date(this.dateOfBirth.getTime() + 1000000000000);
		return gaBirthday;
	};
};

module.exports = Gigasecond;