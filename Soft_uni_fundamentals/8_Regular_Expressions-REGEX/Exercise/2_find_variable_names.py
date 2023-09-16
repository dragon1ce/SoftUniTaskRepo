import re

entry = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
match = re.findall(pattern, entry)
print(",".join(match))
