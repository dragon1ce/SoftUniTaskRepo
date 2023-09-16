import re

pattern = r"([@#])([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1"
entry = input()
match = re.findall(pattern, entry)
palindromes = []
for m in match:
    if m[1] == m[2][::-1]:
        palindromes.append(f"{m[1]} <=> {m[2]}")

if len(match) > 0:
    print(f"{len(match)} word pairs found!")
else:
    print("No word pairs found!")

if len(palindromes) > 0:
    print("The mirror words are:")
    print(", ".join(palindromes))

else:
    print("No mirror words!")
