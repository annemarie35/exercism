"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes based on 'PREPARATION_TIME' for a layer.

    Function that takes the numbers of layers in the lasagna and returns how long it takes to prepare the lasagna based on the constant 'PREPARATION_TIME' that tells how long it takes to make one layer.
    """

    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(layers, time_in_minutes):
    """ Calculate total elapsed cooking time (prep + bake) in minutes

    :param layers: int - number of layers in the lasagna.
    :param time_in_minutes: int - total cooking time in minutes.
    :return: int - total elapsed cooking time in minutes.

    Function that takes the number of layers and the total cooking time as arguments and returns the total
    """

    preparation_time = preparation_time_in_minutes(layers)
    return preparation_time + time_in_minutes


