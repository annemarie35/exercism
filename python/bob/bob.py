def response(hey_bob):
    answer = 'Whatever.'

    cleaned_hey_bob = hey_bob.strip()

    if len(cleaned_hey_bob) == 0:
        answer = 'Fine. Be that way!'

    if cleaned_hey_bob.isupper():
        if cleaned_hey_bob.endswith('?'):
            answer = "Calm down, I know what I'm doing!"
        else:
            answer = "Whoa, chill out!"

    if cleaned_hey_bob.endswith('?') and not cleaned_hey_bob.isupper():
        answer = "Sure."

    return answer
