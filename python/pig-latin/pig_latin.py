def translate(text):
    vowels = 'aeiou'

    def translate_word(text):
        langage_suffixe = 'ay'
        text_first_letter = text[0]
        two_beginning_letters = text[0:2]
        three_beginning_letters = text[0:3]

        consonant_cluster_treated_like_vowels = ('xr', 'yr', 'yt', 'zr')

        is_in_vowel_cluster = text_first_letter in vowels or two_beginning_letters in consonant_cluster_treated_like_vowels
        is_in_consonant_cluster = text_first_letter not in vowels

        if is_in_vowel_cluster:
            return text + langage_suffixe

        if is_in_consonant_cluster:
            consonant_clusters = ('sch', 'thr', 'ch', 'qu', 'th')
            for consonant_cluster in consonant_clusters:
                beginning_letters_to_check = two_beginning_letters  if len(consonant_cluster) == 2 else three_beginning_letters
                if beginning_letters_to_check == consonant_cluster:
                    cutting_index = text.index(consonant_cluster) + len(consonant_cluster)
                    return text[cutting_index:] + consonant_cluster + langage_suffixe

            if two_beginning_letters == 'yt' or two_beginning_letters == 'xr':
                # like wovels !
                return text + langage_suffixe

            if 'y' in text and text_first_letter != 'y':
                y_letter_index = text.index("y")
                # Can generate ValueError: substring not found so we check that there is 'y' in text before
                letters_before_y = text[0:y_letter_index]
                return text[y_letter_index:] + letters_before_y + langage_suffixe

            return text[1:] + text_first_letter + langage_suffixe

    words = text.split()
    translated_phrase = ''
    for word in words:
        translated_word = translate_word(word)
        translated_phrase = translated_phrase + translated_word + ' '


    return translated_phrase.strip()


