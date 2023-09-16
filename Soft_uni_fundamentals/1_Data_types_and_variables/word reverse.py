sente = "hey there warrriors"


def spin_words(sentence):
    a = sentence.split(" ")
    for i, words in enumerate(a):
        if len(words) >= 5:
            a[i] = words[::-1]

    return " ".join(a)


print(spin_words(sente))
