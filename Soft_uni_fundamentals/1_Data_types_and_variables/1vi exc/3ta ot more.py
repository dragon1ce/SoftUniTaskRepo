mylist = []
entry = input()
word = ""
for i in entry:
    if i == ",":
        mylist.append(word)
        word = ""
        continue
    if i.isalpha():
        word += i
else:
    mylist.append(word)
mylist.reverse()
for index, obje in enumerate(mylist):
    if obje == "wolf" and index == 0:
        print("Please go away and stop eating my sheep")
    elif obje == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
