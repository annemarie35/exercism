def two_fer(*name):
    message = 'One for you, one for me.'

    if name:
        message = f'One for {name[0]}, one for me.'

    return message



