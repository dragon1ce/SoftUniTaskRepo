soft_uni = {}
language_check = {}
name, language, score = "", "", ""
while True:
    entry = input()
    if entry == "exam finished":
        break
    if "banned" in entry:
        name = entry.split("-")[0]
        soft_uni[f"banned - {name}"] = soft_uni[name]
        del soft_uni[name]
        continue
    else:
        name, language, score = entry.split("-")
        score = int(score)

    if name not in soft_uni.keys():
        soft_uni[name] = score
    elif name in soft_uni.keys():
        if score > soft_uni[name]:
            soft_uni[name] = score

    if language not in language_check:
        language_check[language] = 0
    language_check[language] += 1
print("Results:")
for name_student,points in soft_uni.items():
    if "banned" not in name_student:
        print(f"{name_student} | {points}")
print("Submissions:")
for lang, count in language_check.items():
    print(f"{lang} - {count}")