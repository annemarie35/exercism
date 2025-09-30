def is_isogram(text):
    result = True
    for char in text:
        if text.lower().count(char) > 1 and char.isalpha():
            result = False
    return result


# def is_isogram(word):
#     word = word.lower().replace(" ","").replace("-","")
#     return len(word) == len(set(word))
# set remove duplicates !!