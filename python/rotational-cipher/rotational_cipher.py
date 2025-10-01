def rotate(text, key):
    rotated_text = ""
    for letter in text:
        rotated_text += find_rot_letter(letter, key)
    return rotated_text


def find_rot_letter(letter, key):
    if not letter.isalpha():
        return letter
    if letter.isdigit():
        return letter
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    valid_key = key
    if key > len(alphabet):
        valid_key = len(alphabet) - key
    rot_index = alphabet.index(letter.lower()) + valid_key

    valid_index = rot_index

    if rot_index >= len(alphabet):
        valid_index = rot_index - len(alphabet)

    return alphabet[valid_index].upper() if letter.isupper() else alphabet[valid_index]