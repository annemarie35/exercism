var dnaTranscriber = function() {};
dnaTranscriber.prototype.toRna = function(dnaStrand) {
var trans = {
G: "C",
C: "G",
T: "A",
A: "U"
}


return dnaStrand.replace(/C|G|T|A/g, dna => trans[dna]);
};

module.exports = dnaTranscriber;