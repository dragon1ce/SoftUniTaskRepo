capitals = ("CODING", "DOG", "CAT", "MOVIE")
lowers = ("coding", "dog", "cat", "movie")
total_coffees = 0
while True:
    entry = input()
    if entry == "END":
        break
    if entry in capitals:
        total_coffees += 2
    elif entry in lowers:
        total_coffees += 1
if total_coffees > 5:
    print("You need extra sleep")
else:
    print(total_coffees)
