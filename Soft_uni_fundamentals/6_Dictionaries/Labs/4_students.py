command = input()
students = {}
while ":" in command:
    name, id_number, major = command.split(":")
    students[int(id_number)] = [name, str(major)]
    command = input()
for key, value in students.items():

    students[key][1] = students[key][1].replace(" ","_")
    if command == students[key][1]:
        print(f"{students[key][0]} - {key}")
