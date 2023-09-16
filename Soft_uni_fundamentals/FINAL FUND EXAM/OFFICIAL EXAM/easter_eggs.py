import re

entry = input()

pattern = r"[@#]+([a-z]{3,})[@#]+[\W]*\/(\d+)\/"
matches = re.findall(pattern, entry)
for match in matches:
    color = match[0]
    quantity = int(match[1])
    print(f"You found {quantity} {color} eggs!")

