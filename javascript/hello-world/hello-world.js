var HelloWorld = function() {};
HelloWorld.prototype.hello = function(input) {
   input == '' ? input = 'World' : input = input ;
   return 'Hello, ' + input + '!';
  };

module.exports = HelloWorld;