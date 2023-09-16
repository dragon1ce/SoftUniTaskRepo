dark_lord_named = False
while True:
    name = input()
    if name == "Welcome!":
        break
    if name == "Voldemort":
        print("You must not speak of that name!")
        dark_lord_named = True
        break
    if len(name) <5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) >6:
        print(f"{name} goes to Hufflepuff.")
if not dark_lord_named:
    print("Welcome to Hogwarts.")