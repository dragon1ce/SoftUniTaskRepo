import re

pattern = r"\d+"
matches = []
while True:
    entry = input()
    if entry == "":
        break
    match = re.findall(pattern, entry)
    matches += match
print(" ".join(matches))