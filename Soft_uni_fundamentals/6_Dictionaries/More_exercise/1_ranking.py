contests = {}
students = {}
while True:
    command = input().split(":")
    if command[0] == "end of contests":
        break
    contest, password = command
    contests[contest] = password

while True:
    command = input().split("=>")
    if command[0] == "end of submissions":
        break
    contest, password, student, points = command
    points = int(points)
    if contest not in contests.keys():
        continue
    elif contest in contests.keys():
        if contests[contest] != password:
            continue
    if student not in students.keys():
        students[student] = {}
        students[student][contest] = points
    elif student in students.keys():
        if contest in students[student].keys() and points > students[student][contest]:
            students[student][contest] = points
        elif contest not in students[student].keys():
            students[student][contest] = points
best = [0, ""]
for name, course in students.items():
    total = 0
    for point_value in course.values():
        total += point_value
    if total > best[0]:
        best[0] = total
        best[1] = name
print(f"Best candidate is {best[1]} with total {best[0]} points.")
print("Ranking:")
sorted_students = dict(sorted(students.items(), key=lambda x: x[0]))

for key, value in sorted_students.items():
    sorted_values = dict(sorted(value.items(), key=lambda x: -x[1]))
    sorted_students[key] = sorted_values
for name in sorted_students.keys():
    print(f"{name}")
    for key, value in sorted_students[name].items():
        print(f"#  {key} -> {value}")
