def is_armstrong_number(number):
    number_of_digits = len(str(number))
    sum = 0
    digits = str(number)
    for digit in digits:
        sum += int(digit)**number_of_digits
    return sum == number
