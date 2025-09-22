def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    result = number
    counter = 0

    while result != 1:
        if result % 2 == 0:
            result //= 2
        else:
            result = result * 3 + 1
        counter +=1

    return counter
