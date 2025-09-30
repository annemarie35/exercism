def reverse(text):
    result = ''
    print('--------------')
    print('--------------', (''.join(reversed(text))))
    print('--------------')
    for x in list(reversed(text)):
        result += x
    return result
    # return s[::-1]
    # (''.join(reversed(text)))