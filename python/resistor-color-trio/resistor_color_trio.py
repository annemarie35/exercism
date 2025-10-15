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
    result = RESISTORS_COLOR[colors[0]] + RESISTORS_COLOR[colors[1]] + (int(RESISTORS_COLOR[colors[2]]) * '0')
    resultLinted = str(int(result))

    if result == '00':
        return '0 ohms'

    if len(result) <= 3:
        return resultLinted + ' ohms'

    if 4 <= len(result) <= 6:
        return str((int(result)//1000)) + ' kiloohms'

    if 6 <= len(result) <= 9:
        return str((int(result)//1000000)) + ' megaohms'

    if len(result) > 9:
        return str((int(result)//1000000000)) + ' gigaohms'

