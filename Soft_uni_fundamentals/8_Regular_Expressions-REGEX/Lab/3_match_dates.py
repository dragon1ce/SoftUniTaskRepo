import re

names = input()
regex = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"


mathes = re.findall(regex, names)
for mat in mathes:
    day= mat[0]
    month = mat[2]
    year = mat[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")