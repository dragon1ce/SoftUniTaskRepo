import re


def text_filter():
    banned_words = input().split(', ')
    text = input()
    for i in range(len(banned_words)):
        x = len(banned_words[i])

        text = re.sub(banned_words[i], "*" * x, text)
    return text


print(text_filter())
