import re

entry = input()
pattern = r"\s(([a-zA-Z]+[\w\.\-]*)@([a-z][a-z\-]+)(\.[a-z][a-z\-]+)+)\b"
match = re.findall(pattern, entry)
for extr in match:
    print(extr[0])
