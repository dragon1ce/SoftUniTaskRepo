students = {}
n = int(input())
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for names, grades in students.items():
    avg_grade = sum(students[names]) / len(students[names])
    if avg_grade >= 4.5:
        print(f"{names} -> {avg_grade:.2f}")