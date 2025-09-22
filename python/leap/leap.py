def leap_year(year):
    is_leap = False
    if year % 4 == 0:
        is_leap = True
        if year % 100 == 0 and year % 400 != 0:
            is_leap = False
    return is_leap

    # Chain of Boolean Expressions
    # return not year % 4 and (year % 100 != 0 or not year % 400)
    # Ternary Operator of Boolean Expressions
    # return (not year % 400 if not year % 100 else not year % 4)
