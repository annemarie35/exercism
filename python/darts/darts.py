from math import sqrt

def score(x, y):
    inner_circle = 1
    middle_circle = 5
    outer_circle = 10

    try:
        radius = sqrt(x ** 2 + y ** 2)
    except:
        raise ValueError("wrong inputs")

    if radius > outer_circle:
        return 0
    elif radius > middle_circle:
        return 1
    elif radius > inner_circle:
        return 5
    elif radius >= 0:
        return 10
