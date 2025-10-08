"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def is_contained(list_one, list_two):
    list_1_lenghth = len(list_one)
    list_2_length = len(list_two)
    for index in range(list_1_lenghth - list_2_length + 1):
        if not list_two or list_two == list_one[index: index + list_2_length]:
            return True
    return False
    # Alternative
    # Approach: list manipulation
    # n1 = len(list_one)
    # n2 = len(list_two)
    # return any(list_two[i:i + n1] == list_one for i in range(n2 - n1 + 1))

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if is_contained(list_one, list_two):
        return SUPERLIST
    if is_contained(list_two, list_one):
        return SUBLIST
    else:
        return UNEQUAL
    # https://exercism.org/tracks/python/exercises/sublist/approaches/using-strings