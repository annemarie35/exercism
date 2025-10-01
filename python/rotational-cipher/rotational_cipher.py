ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text, key):
    rotated_text = ""
    for letter in text:
        rotated_text += find_rot_letter(letter, key)
    return rotated_text


def find_rot_letter(letter, key):
    if letter.isalpha():
        rot_index = ALPHABET.index(letter.lower()) + key
        if rot_index >= len(ALPHABET):
            rot_index = rot_index - len(ALPHABET)
        # % 26 can be used instead

        return ALPHABET[rot_index].upper() if letter.isupper() else ALPHABET[rot_index]
    else:
        return letter