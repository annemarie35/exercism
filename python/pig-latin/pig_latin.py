def translate(text):
    vowels = 'aeiou'

    def translate_word(text):
        langage_suffixe = 'ay'
        if text[0] in vowels or text[0:1] == 'xr' or text[0:1] == 'yr' or text[0:1] == 'yt' or text[0:1] == 'zr':
            return text + langage_suffixe

        is_in_consonant_cluster = text[0] not in vowels

        if is_in_consonant_cluster:
            two_beginning_letters = text[0:2]
            three_beginning_letters = text[0:3]

            if three_beginning_letters == 'sch':
                toto = text.index("sch") + len("sch")
                return text[toto:] + 'sch' + langage_suffixe

            if two_beginning_letters == 'ch':
                toto = text.index("ch") + len("ch")
                return text[toto:] + 'ch' + langage_suffixe

            if two_beginning_letters == 'qu':
                toto = text.index("qu") + len("qu")
                return text[toto:] + 'qu' + langage_suffixe

            if three_beginning_letters == 'thr':
                toto = text.index("thr") + len("thr")
                return text[toto:] + 'thr' + langage_suffixe

            if two_beginning_letters == 'th':
                toto = text.index("th") + len("th")
                return text[toto:] + 'th' + langage_suffixe

            if two_beginning_letters == 'yt' or two_beginning_letters == 'xr':
                return text + langage_suffixe

            first_letter = text[0]

            if text[-1] == 'y' or text[1] == 'y':
                tata = text[1:] + text[0] + langage_suffixe
                return tata

            if 'y' in text and text[0] != 'y':
                toto = text.index("y")
                letters_before_y = text[0:toto]
                return text[toto:] + letters_before_y + langage_suffixe

            return text[1:] + first_letter + langage_suffixe

    words = text.split()
    translated_phrase = ''
    for word in words:
        lala = translate_word(word)
        translated_phrase = translated_phrase + lala + ' '


    return translated_phrase.strip()


