class HelloWorld
  def self.hello(*name)
    (name[0] != nil) ? ('Hello, ' + name[0] + '!') : ('Hello, World!') 
  end
end