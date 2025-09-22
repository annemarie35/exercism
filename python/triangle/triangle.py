def equilateral(sides):
    is_equilateral = True
    if 0 in sides:
        is_equilateral = False
    else:
        for i in range(0, 2):
            if sides[i] != sides[i + 1]:
                is_equilateral = False

    return is_equilateral

def is_a_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    return a + b >= c and b + c >= a and a + c >= b and not 0 in sides


def isosceles(sides):
    if not is_a_triangle(sides):
        is_isocele = False
    else:
        is_isocele = sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
        # len(set(sides)) == 1
        # the set build in function remove duplicates and transform list in a set so set([4,4,4]) will be {4}
    return is_isocele

def scalene(sides):
    return not isosceles(sides) and is_a_triangle(sides)
    # duplication using is_a_triangle here and inside isosceles function
    # it can be solved by using validation function with an annotation before function declaration @is_a_triangle

