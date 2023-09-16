string = input()
mylist = []
for i, j in enumerate(string):
    if j.isupper():
        mylist.append(i)
print(mylist)
