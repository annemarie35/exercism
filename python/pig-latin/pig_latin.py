def translate(text):
    words = text.split()
    translated_phrase = ''
    for word in words:
        translated_word = translate_word(word)
        translated_phrase = translated_phrase + translated_word + ' '

    return translated_phrase.strip()

VOWELS = 'aeiou'
LANGUAGE_SUFFIX = 'ay'
CONSONANT_CLUSTERS = ('sch', 'thr', 'ch', 'qu', 'th')
SPECIAL_LETTERS = ('yt', 'xr')

def translate_word(text):
    first_beginning_letter = text[0]
    two_beginning_letters = text[0:2]
    three_beginning_letters = text[0:3]

    is_in_vowel_cluster = first_beginning_letter in VOWELS or two_beginning_letters in SPECIAL_LETTERS
    is_in_consonant_cluster = first_beginning_letter not in VOWELS

    if is_in_vowel_cluster:
        return text + LANGUAGE_SUFFIX

    if is_in_consonant_cluster:
        for consonant_cluster in CONSONANT_CLUSTERS:
            beginning_letters_to_check = text[0:len(consonant_cluster)]

            if beginning_letters_to_check == consonant_cluster:
                cutting_index = len(consonant_cluster)
                return text[cutting_index:] + consonant_cluster + LANGUAGE_SUFFIX

            if text[1:3] == 'qu':
                cutting_index = text.index("u") + 1
                return text[cutting_index:] + three_beginning_letters + LANGUAGE_SUFFIX

        if 'y' in text and first_beginning_letter != 'y':
            y_letter_index = text.index("y")
            # text.index("y") can generate ValueError: substring not found so we check that there is 'y' in text before
            letters_before_y = text[0:y_letter_index]
            return text[y_letter_index:] + letters_before_y + LANGUAGE_SUFFIX

        return text[1:] + first_beginning_letter + LANGUAGE_SUFFIX



# Below, a really nice solution https://exercism.org/tracks/python/exercises/pig-latin/dig_deeper
# Cut consonants before a found vowel expect for special cases
# VOWELS = {"a", "e", "i", "o", "u"}
# VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
# SPECIALS = {"xr", "yt"}
# def translate(text):
#     piggyfied = []
#
#     for word in text.split():
#         if word[0] in VOWELS or word[0:2] in SPECIALS:
#             piggyfied.append(word + "ay")
#             continue
#
#         for pos in range(1, len(word)):
#             if word[pos] in VOWELS_Y:
#                 pos += 1 if word[pos] == 'u' and word[pos - 1] == "q" else 0
#                 piggyfied.append(word[pos:] + word[:pos] + "ay")
#                 break
#
#     return " ".join(piggyfied)
