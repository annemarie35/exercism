def convert(number):
    raindrops = ""
    if number % 3 == 0:
        raindrops += "Pling"

    if number % 5 == 0:
        raindrops += "Plang"

    if number % 7 == 0:
        raindrops += "Plong"

    return raindrops or str(number)
    # '' or 'value' returns 'value' !

#
# See others approaches on https://exercism.org/tracks/python/exercises/raindrops/dig_deeper
# If too many if statement, use a loop
#
# For performance deep dive look at https://exercism.org/tracks/python/exercises/raindrops/articles/performance
#
# def convert(number):
#     #This is clear and easily added to.  Unless the factors get
#     # really long, this won't take up too much memory.
#     sounds = {3: 'Pling',
#               5: 'Plang',
#               7: 'Plong'}
#
#     results = (sound for
#                divisor, sound in sounds.items()
#                if number % divisor == 0)
#
#     return ''.join(results) or str(number)