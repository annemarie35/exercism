var TwoFer = function () {};

TwoFer.prototype.twoFer = function (who) {
  let oneWho = 'One for you, one for me.';
  if (who) {
    oneWho = `One for ${who}, one for me.`
  }
  return oneWho;
};

module.exports = TwoFer;