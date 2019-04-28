# https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne

class Sieve
	def initialize(number)
		@number = number
	end

def primes
	result = []
	list = [*2..@number]

	if @number > 1 && @number <= 2
		result = [@number]
	elsif @number > 2
		j = 2
		for j in list
			break if j*j > @number

			for i in list				
				if  i > j && i%j == 0
					list = list - [i]
				end
				result = list
			end 
		end 
	end
	result
end
end