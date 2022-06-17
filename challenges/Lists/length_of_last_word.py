def length_of_last_word(phrase):
    words = phrase.split()
    if len(words) == 0:
        return 0
    else:
        return len(words[-1])

print(length_of_last_word(ph))