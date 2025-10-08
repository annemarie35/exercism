RESISTORS_COLOR_DUO = {
    "black": '0',
    "brown": '1',
    "red": '2',
    "orange": '3',
    "yellow": '4',
    "green": '5',
    "blue": '6',
    "violet": '7',
    "grey": '8',
    "white": '9',
}

def value(colors):
    encoded = ''
    for color in colors:
        encoded += RESISTORS_COLOR_DUO[color]

    return int(encoded[0:2])

