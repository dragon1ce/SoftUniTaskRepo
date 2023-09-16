import re

entry = input()
search_word = input()
pattern = r"\b"+search_word+r"\b"
words = re.findall(pattern, entry, flags=re.IGNORECASE)

print(len(words))