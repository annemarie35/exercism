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
    for index in range(len(list_one) - len(list_two) + 1):
        if not list_two or list_two == list_one[index: index + len(list_two)]:
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if is_contained(list_one, list_two):
        return SUPERLIST
    if is_contained(list_two, list_one):
        return SUBLIST
    else:
        return UNEQUAL
