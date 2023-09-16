import re

names = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"


mathes = re.finditer(regex, names)
for m in mathes:
    print(m.group(),end = " ")