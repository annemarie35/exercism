def translate(text):
    words = text.split()
    translated_phrase = ''
    for word in words:
        translated_word = translate_word(word)
        translated_phrase = translated_phrase + translated_word + ' '

    return translated_phrase.strip()

VOWELS = 'aeiou'
LANGUAGE_SUFFIX = 'ay'
CONSONANT_CLUSTER_VOWELS = ('xr', 'yr', 'yt', 'zr')
CONSONANT_CLUSTERS = ('sch', 'thr', 'ch', 'qu', 'th')
SPECIAL_LETTERS = ('yt', 'xr')

def translate_word(text):
    text_first_letter = text[0]
    two_beginning_letters = text[0:2]
    three_beginning_letters = text[0:3]

    is_in_vowel_cluster = text_first_letter in VOWELS or two_beginning_letters in CONSONANT_CLUSTER_VOWELS or two_beginning_letters in SPECIAL_LETTERS
    is_in_consonant_cluster = text_first_letter not in VOWELS

    if is_in_vowel_cluster:
        return text + LANGUAGE_SUFFIX

    if is_in_consonant_cluster:
        for consonant_cluster in CONSONANT_CLUSTERS:
            beginning_letters_to_check = two_beginning_letters if len(consonant_cluster) == 2 else three_beginning_letters

            if beginning_letters_to_check == consonant_cluster:
                cutting_index = text.index(consonant_cluster) + len(consonant_cluster)
                return text[cutting_index:] + consonant_cluster + LANGUAGE_SUFFIX

            if text[1:3] == 'qu':
                return text[3:] + three_beginning_letters + LANGUAGE_SUFFIX

        if 'y' in text and text_first_letter != 'y':
            y_letter_index = text.index("y")
            # text.index("y") can generate ValueError: substring not found so we check that there is 'y' in text before
            letters_before_y = text[0:y_letter_index]
            return text[y_letter_index:] + letters_before_y + LANGUAGE_SUFFIX

        return text[1:] + text_first_letter + LANGUAGE_SUFFIX
