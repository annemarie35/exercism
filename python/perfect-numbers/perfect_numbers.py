def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = []
    for divisor in range(1, number):
        if number % divisor == 0:
            factors.append(divisor)

    if sum(factors) == number:
        return 'perfect'

    if number < sum(factors):
        return 'abundant'

    if number > sum(factors):
        return 'deficient'



