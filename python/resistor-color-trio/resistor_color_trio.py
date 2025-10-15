RESISTORS_COLOR = {
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

def label(colors):
    ohms = int(RESISTORS_COLOR[colors[0]] + RESISTORS_COLOR[colors[1]] + (int(RESISTORS_COLOR[colors[2]]) * '0'))
    prefix = ''

    if ohms > 1_000_000_000:
        prefix = 'giga'
        ohms = ohms // 1_000_000_000
    if ohms > 1_000_000:
        prefix = 'mega'
        ohms = ohms // 1_000_000
    if ohms > 1_000:
        prefix = 'kilo'
        ohms = ohms // 1_000

    return f"{ohms} {prefix}ohms"

