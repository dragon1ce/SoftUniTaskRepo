import re
pattern = r"w{3}\.[a-zA-Z0-9\-]+\.[a-z][a-z\.]+"
token = input()
matches = []
while token:
    match = re.findall(pattern, token)
    if match:
        matches.append(match[0])


    token=input()
for x in matches:
    print(x)