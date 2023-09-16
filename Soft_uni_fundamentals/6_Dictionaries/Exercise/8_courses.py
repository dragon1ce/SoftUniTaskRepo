courses = {}
while True:
    entry = input()
    if entry == "end":
        break
    else:
        entry = entry.split(" : ")
    course, name = entry

    if course not in courses.keys():
        courses[course] = []
    if course in courses.keys():
        courses[course].append(name)

for course_name, names in courses.items():
    print(f"{course_name}: {len(names)}")
    for name in names:
        print(f"-- {name}")