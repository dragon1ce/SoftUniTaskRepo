students = {}
courses = {}
while True:
    command = input().split(" -> ")
    if command[0] == "no more time":
        break
    username, course, points = command
    points = int(points)
    if course not in courses:
        courses[course] = {}
        courses[course][username] = points
    elif course in courses.keys():
        if username not in courses[course].keys():
            courses[course][username] = points
        elif username in courses[course].keys():
            if points > courses[course][username]:
                courses[course][username] = points

for tuple_students in courses.values():
    for name, point in tuple_students.items():
        if name not in students.keys():
            students[name] = point
        else:
            students[name] += point
sorted_contest = {}
for course_name, contest in courses.items():
    sorted_values = dict(sorted(contest.items(), key=lambda y: (-y[1],y[0])))
    sorted_contest[course_name] = sorted_values
for contest_name, v in sorted_contest.items():
    print(f"{contest_name}: {len(v.keys())} participants")
    x = 0
    for name, pts in v.items():
        x += 1
        print(f"{x}. {name} <::> {pts}")

ordered = dict(sorted(students.items(), key=lambda z: (-z[1],z[0])))
print("Individual standings:")
for i, (k, v) in enumerate(ordered.items()):
    print(f"{i + 1}. {k} -> {v}")
