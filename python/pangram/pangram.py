def is_pangram(sentence):
    counter = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower().replace(".", "").strip()
    for letter in alphabet:
        if letter in sentence:
            counter += 1
    if counter == 26:
        return True
    else:
        return False
